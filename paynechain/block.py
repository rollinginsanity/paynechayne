import hashlib as hash
from datetime import datetime
import json

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        hash_sha = hash.sha256()
        data = str(self.index)+str(self.timestamp)+str(self.data)+str(self.previous_hash)
        hash_sha.update(data.encode())
        return hash_sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.blockchain = []
        self.blockchain.append(self.make_genesis_block())

    def make_genesis_block(self):
        return Block(0, datetime.now(), "The first friggin block", "12345")

    def make_next_block(self, block_data):
        previous_block = self.blockchain[-1]
        index = previous_block.index+1
        timestamp = datetime.now()
        data = block_data
        last_hash = previous_block.hash
        self.blockchain.append(Block(index, timestamp, data, last_hash))

    def show_blockchain(self):
       for block in self.blockchain:
           print(block.index)
           print(block.timestamp)
           print(block.data)
           print(block.previous_hash)


