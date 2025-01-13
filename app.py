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
