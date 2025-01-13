import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    difficulty = 1
    
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), previous_block.hash, time.time(), data)
        new_block = self.proof_of_work(new_block)
        self.chain.append(new_block)

    def proof_of_work(self, block):
        block.nonce = 0
        while not block.hash.startswith("0" * Blockchain.difficulty):
            block.nonce += 1
            block.hash = block.compute_hash()
        return block

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.compute_hash():
                return f"Invalid hash for block {current_block.index}"
            if current_block.previous_hash != previous_block.hash:
                return f"Invalid previous hash for block {current_block.index}"
            if not current_block.hash.startswith("0" * Blockchain.difficulty):
                return f"Block {current_block.index} is not mined"
            if current_block.timestamp <= previous_block.timestamp:
                return f"Block {current_block.index} has an invalid timestamp"
        return "Blockchain is valid"
    