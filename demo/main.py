import json
from web3 import Web3

ganache = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache))

web3.eth.default_account = web3.eth.accounts[0]

abi = json.loads("""
[
    {
      "inputs": [
        {
          "internalType": "int256",
          "name": "x",
          "type": "int256"
        },
        {
          "internalType": "int256",
          "name": "y",
          "type": "int256"
        }
      ],
      "name": "addTwoNumbers",
      "outputs": [
        {
          "internalType": "int256",
          "name": "",
          "type": "int256"
        }
      ],
      "stateMutability": "pure",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "greet",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "greeter",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "greeting",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "print",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "pure",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "_greeting",
          "type": "string"
        }
      ],
      "name": "setGreeting",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]
""")

address = web3.to_checksum_address("0x5FbDB2315678afecb367f032d93F642f64180aa3")

contract = web3.eth.contract(abi=abi, address=address)

print(web3.is_connected())

print(contract.functions.greet().call())

tx_hash = contract.functions.setGreeting("Howdy").transact()

print(tx_hash)

web3.eth.wait_for_transaction_receipt(tx_hash)

print(contract.functions.greet().call())

print(contract.functions.addTwoNumbers(5, 5).call())

