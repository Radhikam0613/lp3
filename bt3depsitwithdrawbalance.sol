pragma solidity ^0.8.12;
contract Banking {
    mapping(address => uint) public balance;
    mapping(address => bool) public exists;
    function create_account() public {
        require(!exists[msg.sender], "Account already exists");
        exists[msg.sender] = true;
    }
    function deposit() public payable {
        require(exists[msg.sender], "Create account first");
        require(msg.value > 0, "Invalid amount");
        balance[msg.sender] += msg.value;
    }
    function withdraw(uint amount) public {
        require(exists[msg.sender], "Create account first");
        require(amount > 0 && amount <= balance[msg.sender],"Invalid amount");
        balance[msg.sender] -= amount;
        (bool success, ) = payable(msg.sender).call{value: amount}("");
        require(success, "Withdrawal failed");
    }
    function transfer(address to, uint amount) public {
        require(exists[msg.sender], "Create account first");
        require(exists[to], "Recipient account not found");
        require(amount > 0 && amount <= balance[msg.sender],"Invalid amount");
        balance[msg.sender] -= amount;
        balance[to] += amount;
    }
}










Solidity is a programming language used to write smart contracts that run 
on Ethereum-compatible blockchains. A smart contract is a program deployed 
on a blockchain. It executes its programmed rules when someone interacts with it.
Remix IDE is the tool you use to write, compile, deploy, and test the contract. 
In your practical, Remix VM simulates the blockchain, so you can test everything 
with fake Ether.

// SPDX-License-Identifier: MIT
// pragma specifies a compiler directive
// solidity identifies the language to which the directive applies.
pragma solidity ^0.8.12;

contract Banking {
    // call reads data without changing persistent blockchain state.
    // A mapping is a Solidity data structure that stores values associated with keys.
    // A public mapping automatically provides a getter function, which is why Remix displays
    // balance(address) as a separate callable entry.
    mapping(address => uint) public balance;
    mapping(address => bool) public exists;

    function create_account() public {
        require(!exists[msg.sender], "Account already exists");
        // since the mapping value of msg.sender's exists is set to true acc exists
        exists[msg.sender] = true;
    }

    // The function has no explicit parameter, but it receives Ether through a special 
    transaction property called (msg.value). payable allows the function to receive Ether 
    from msg.value
    function deposit() public payable {
        require(exists[msg.sender], "Create account first");
        require(msg.value > 0, "Invalid amount");
        balance[msg.sender] += msg.value;
    }

      // withdraw sends deposited wei's of solidity contract back to remix wallet
      function withdraw(uint amount) public {
        require(exists[msg.sender], "Create account first");
        require(amount > 0 && amount <= balance[msg.sender],"Invalid amount");
        balance[msg.sender] -= amount;
        // msg.sender — the address calling the function.
        // payable(msg.sender).call{value: amount}("") — sends Ether to that address.
        # (bool success, )	Stores the success status and ignores the returned data.
        # payable(msg.sender)	Converts the caller's address into a payable address that can receive Ether.
        # .call{value: amount}	Sends amount wei to the caller.
        # ("")	Sends empty calldata because no function on the recipient is being explicitly called
        (bool success, ) = payable(msg.sender).call{value: amount}("");
        require(success, "Withdrawal failed");
    }

    function transfer(address to, uint amount) public {
        require(exists[msg.sender], "Create account first");
        require(exists[to], "Recipient account not found");
        require(amount > 0 && amount <= balance[msg.sender],"Invalid amount");
        balance[msg.sender] -= amount;
        balance[to] += amount;
    }
}