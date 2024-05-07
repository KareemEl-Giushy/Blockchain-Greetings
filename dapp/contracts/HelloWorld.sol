// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

contract HelloWorld {
    /**
     * @dev Prints Hello World string
     */

    string public greeting = "hello";

    function greeter() public {
        greeting = "Hello";
    }

    function setGreeting(string memory _greeting) public {
        greeting = _greeting;
    }

    function addTwoNumbers(int256  x, int256 y) public pure returns(int256) {
        return (x + y);
    }

    function greet() public view returns (string memory) {
        return greeting;
    }

    function print() public pure returns (string memory) {
        return "Hello World!";
    }
}
