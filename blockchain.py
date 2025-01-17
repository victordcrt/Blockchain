import hashlib
import time

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_dict(self):
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount
        }

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{[tx.to_dict() for tx in self.transactions]}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    difficulty = 1
    
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.current_transactions = []

    def create_genesis_block(self):
        return Block(0, "0", time.time(), [], 0)

    def get_latest_block(self):
        return self.chain[-1]
    
    def new_transaction(self, sender, recipient, amount):
        transaction = Transaction(sender, recipient, amount)
        self.current_transactions.append(transaction)
        return transaction
    
    def mine_pending_transactions(self):
        if not self.current_transactions:
            return "No transactions to mine"
        
        new_block = Block(
            len(self.chain),
            self.get_latest_block().hash,
            time.time(),
            self.current_transactions
        )
        mined_block = self.proof_of_work(new_block)
        self.chain.append(mined_block)
        self.current_transactions = []
        return mined_block
    
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

    def get_block_by_index(self, index):
        if 0 <= index < len(self.chain):
            return self.chain[index]
        return None
    
    def get_block_by_hash(self, hash_value):
        for block in self.chain:
            if block.hash == hash_value:
                return block
        return None
    
    def list_all_hashes(self):
        return [block.hash for block in self.chain]
    
class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
    
    def to_dict(self):
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount
        }

