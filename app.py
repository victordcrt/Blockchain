from flask import Flask, request, jsonify
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = [{"index": block.index, "data": block.data, "hash": block.hash} for block in blockchain.chain]
    return jsonify({"length": len(chain_data), "chain": chain_data})

@app.route('/mine', methods=['POST'])
def mine_block():
    data = request.get_json().get("data", "Empty Data")
    blockchain.add_block(data)
    return jsonify({"message": "Block mined!", "chain": [{"index": block.index, "hash": block.hash} for block in blockchain.chain]})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

@app.route('/block/<int:index>', methods=['GET'])
def get_block_by_index(index):
    block = blockchain.get_block_by_index(index)
    if block:
        return jsonify({"index": block.index, "previous_hash": block.previous_hash, "timestamp": block.timestamp, "data": block.data, "nonce": block.nonce, "hash": block.hash}), 200 # 200 make me cry...
    return jsonify({"error": "Block not found"}), 404
 
@app.route('/block/hash/<string:hash>', methods=['GET'])
def get_block_by_hash(hash_value):
    block = blockchain.get_block_by_hash(hash_value)
    if block:
        return jsonify({"index": block.index, "previous_hash": block.previous_hash, "timestamp": block.timestamp, "data": block.data, "nonce": block.nonce, "hash": block.hash}), 200
    return jsonify({"error": "Block not found"}), 404
 
@app.route('/hashes', methods=['GET'])
def list_all_hashes():
    return jsonify({"hashes": hashes}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)