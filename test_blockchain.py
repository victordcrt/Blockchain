import unittest
from blockchain import Blockchain

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

if __name__ == '__main__':
    unittest.main()
