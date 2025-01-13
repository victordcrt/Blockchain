from blockchain import Blockchain

if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_block("First Block")
    blockchain.add_block("Second Block")

    for block in blockchain.chain:
        print(f"Index: {block.index}, Hash: {block.hash}, Previous: {block.previous_hash}, Data: {block.data}")
