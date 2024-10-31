'''
swordfish@Hriteshs-MacBook-Pro:~/Documents/Projects/cy6120|⇒  nc 35.209.254.29 36001
>> ls
ls
An error occured. But which...

>> print(open('flag.txt').read())
print(open('flag.txt').read())
An error occured. But which...
>> print(__import__('os').listdir('.'))
print(__import__('os').listdir('.'))
An error occured. But which...
>> print('flag.txt' in __import__('os').listdir('.'))
print('flag.txt' in __import__('os').listdir('.'))
An error occured. But which...
>> print(__import__('os').popen('cat flag.txt').read())
print(__import__('os').popen('cat flag.txt').read())
An error occured. But which...
>> print(__import__('os').system('cat flag.txt'))
print(__import__('os').system('cat flag.txt'))
An error occured. But which...
>> exec("print(open('flag.txt').read())")
exec("print(open('flag.txt').read())")
You're trying something fancy aren't u ?
>> 

>> print(open('./flag.txt').read())
print(open('./flag.txt').read())
An error occured. But which...
>> print((lambda x: open(x).read())('flag.txt'))
print((lambda x: open(x).read())('flag.txt'))
An error occured. But which...
>> print([open('flag.txt').read()])
print([open('flag.txt').read()])
An error occured. But which...
>> print(globals()['open']('flag.txt').read())
print(globals()['open']('flag.txt').read())
An error occured. But which...
>> print(__import__('builtins').open('flag.txt').read())
print(__import__('builtins').open('flag.txt').read())
An error occured. But which...
>> print("Hello, World!")
print("Hello, World!")
Hello, World!
>> exec("print(open('flag.txt').read())")
exec("print(open('flag.txt').read())")
You're trying something fancy aren't u ?

>> print(eval("open('flag.txt').read()"))
print(eval("open('flag.txt').read()"))
You're trying something fancy aren't u ?
>> print(globals().get('__builtins__').get('open')('flag.txt').read())
print(globals().get('__builtins__').get('open')('flag.txt').read())
An error occured. But which...
>> print((lambda: __builtins__.open('flag.txt').read())())
print((lambda: __builtins__.open('flag.txt').read())())
An error occured. But which...
>> f = __builtins__.open; print(f('flag.txt').read())
f = __builtins__.open; print(f('flag.txt').read())
An error occured. But which...

'''