import unittest
import time
from blockchain import Blockchain, Block

class TestBlockchain(unittest.TestCase):
    
    def test_genesis_block(self):
        blockchain = Blockchain()
        self.assertEqual(blockchain.chain[0].data, "Genesis Block")

    def test_add_block(self):
        blockchain = Blockchain()
        blockchain.add_block("Test Data")
        self.assertEqual(blockchain.chain[1].data, "Test Data")

    def test_chain_validity(self):
        blockchain = Blockchain()
        blockchain.add_block("Test Data")
        self.assertTrue(blockchain.is_chain_valid())

    def test_invalid_hash_after_modification(self):
        blockchain = Blockchain()
        blockchain.add_block("Test Data")
        blockchain.add_block("Another Test Data")
        
        blockchain.chain[1].data = "Malicious Data"
        
        self.assertNotEqual(blockchain.is_chain_valid(), "Blockchain is valid")

    def test_proof_of_work(self):
        blockchain = Blockchain()
        blockchain.add_block("Test Data")
        
        last_block = blockchain.get_latest_block()
        self.assertTrue(last_block.hash.startswith("0" * Blockchain.difficulty))
    
    def test_timestamp_order(self):
        blockchain = Blockchain()
        blockchain.add_block("Test Data")
        blockchain.add_block("Another Test Data")
        
        previous_block = blockchain.chain[1]
        current_block = blockchain.chain[2]
        self.assertTrue(current_block.timestamp > previous_block.timestamp)

if __name__ == '__main__':
    unittest.main()
