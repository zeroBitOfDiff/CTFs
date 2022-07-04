this smart contract has an error in its constructor

solution:
```
contract.Fal1out()
```

then check if you've become the owner
```
await contract.owner()
```
