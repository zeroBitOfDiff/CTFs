# 0.Hello Ethernaut

This is the tutorial for the CTF

Solution:

step 9 gives you hint to run in console
```
await contract.info()
"You will find what you need in info1()."`

```

run next command
```
await contract.info1()
"try info2(), but with "hello" as a parameter"
```

info2 
```
await contract.info2("hello")
"The property infoNum holds the number of the next info method to call."await contract.infoNum()
t {s: 1, e: 1, c: Array(1)}
c: [42]
e: 1
s: 1
__proto__: Object
```

info42
```
await contract.info42()
"theMethodName is the name of the next method."
```

theMethodName
```
await contract.theMethodName()
"The method name is method7123949."
```

method7123949
```
await contract.method7123949()
"If you know the password, submit it to authenticate()."
```

call the password function to get the the password 
```
await contract.password()
"ethernaut0"

contract.authenticate("ethernaut0")
```









