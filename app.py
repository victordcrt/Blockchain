from flask import Flask, request, jsonify
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = [{"index": block.index, "previous_hash": block.previous_hash, "timestamp": block.timestamp, "trasnsactions": [tx.to_dict() for tx in block.transactions], "nonce": block.nonce, "hash":block.hash} for block in blockchain.chain]
    return jsonify({"length": len(chain_data), "chain": chain_data})

@app.route('/mine', methods=['POST'])
def mine_block():
    if not blockchain.current_transactions:
        return jsonify({"error": "No transactions to mine"}), 400
    
    mined_block = blockchain.mine_pending_transactions()
    return jsonify({
        "message": "Block mined!",
        "block": {"index": mined_block.index, "previous_hash": mined_block.previous_hash, "timestamp": mined_block.timestamp, "transactions": [tx.to_dict() for tx in mined_block.transactions], "nonce": mined_block.nonce, "hash": mined_block.hash}
})
    
@app.route('/transaction/pending', methods=['POST'])
def get_pending_transactions():
    pending_transactions = [tx.to_dict() for tx in blockchain.current_transactions]
    return jsonify({"pending_transactions": pending_transactions}),

@app.route('/transaction/new', methods=['POST'])
def add_transactions():
    data = request.get_json()
    required_fields = ["sender", "recipient", "amount"]
    if not all(field in data for field in required_fields):
        return jsonify({"error" : "Missing values"}), 400
    
    transactions = blockchain.new_transaction(sender=data["sender"], recipient=data["recipient"], amount=data["amount"])
    return jsonify({"transaction": transactions.to_dict()}), 201
    

@app.route('/block/<int:index>', methods=['GET'])
def get_block_by_index(index):
    block = blockchain.get_block_by_index(index)
    if block:
        return jsonify({
            "index": block.index,
            "previous_hash": block.previous_hash,
            "timestamp": block.timestamp,
            "transactions": [tx.to_dict() for tx in block.transactions],
            "nonce": block.nonce,
            "hash": block.hash
        }), 200
    return jsonify({"error": "Block not found"}), 404
 
@app.route('/block/hash/<string:hash_value>', methods=['GET'])
def get_block_by_hash(hash_value):
    block = blockchain.get_block_by_hash(hash_value)
    if block:
        return jsonify({
            "index": block.index,
            "previous_hash": block.previous_hash,
            "timestamp": block.timestamp,
            "transactions": [tx.to_dict() for tx in block.transactions],
            "nonce": block.nonce,
            "hash": block.hash
        }), 200
    return jsonify({"error": "Block not found"}), 404
 
@app.route('/hashes', methods=['GET'])
def list_all_hashes():
    hashes = blockchain.list_all_hashes()
    return jsonify({"hashes": hashes}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)