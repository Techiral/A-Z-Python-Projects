Simple Blockchain in Python

This is a simple implementation of a blockchain in Python. A blockchain is a distributed ledger that consists of a chain of blocks, where each block contains data and a cryptographic hash of the previous block. This readme file provides an overview of the code and how to use it.

Code Overview

The code consists of three main components:

hashGenerator(data): This function takes a string data as input and returns its SHA-256 hash in hexadecimal format using the hashlib library.
Block class: This class represents a single block in the blockchain. Each block has three attributes:
data: The data stored in the block.
hash: The cryptographic hash of the current block's data and the previous block's hash.
prev_hash: The cryptographic hash of the previous block's data.
Blockchain class: This class represents the entire blockchain and provides methods to create and add new blocks to the chain. It has the following methods:
__init__(self): Initializes the blockchain with a genesis block.
add_block(self, data): Adds a new block to the blockchain with the provided data.
Getting Started

To use this simple blockchain implementation, follow these steps:

Ensure you have Python installed on your system.
Clone or download the code repository to your local machine.
Open a terminal and navigate to the directory containing the code.
Run the code by executing the Python script:
   python blockchain.py
This will create an instance of the Blockchain class and add three blocks with the data '1', '2', and '3' to the blockchain.
After running the code, you will see the details of each block in the blockchain printed to the console, including the data, hash, and previous hash.
Notes

This implementation is simplified for educational purposes and does not include features like mining, consensus algorithms, or peer-to-peer networking, which are essential in real-world blockchain systems.
The cryptographic hashing used here is SHA-256, but in practice, blockchain systems may use different hashing algorithms.
This code is meant for educational purposes and should not be used for production blockchain systems.