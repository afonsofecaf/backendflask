from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulando um banco de dados
# Na prática, você usaria um banco de dados real
itens = [
    {"id": 1, "nome": "Item 1", "descricao": "Descrição do item 1"},
    {"id": 2, "nome": "Item 2", "descricao": "Descrição do item 2"}
]

# Rota para obter todos os itens
@app.route('/itens', methods=['GET'])
def get_itens():
    return jsonify(itens)

# Rota para obter um item por ID
@app.route('/itens/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in itens if item['id'] == item_id), None)
    if item is None:
        return jsonify({"mensagem": "Item não encontrado"}), 404
    return jsonify(item)

# Rota para criar um novo item
@app.route('/itens', methods=['POST'])
def create_item():
    novo_item = {
        "id": len(itens) + 1,
        "nome": request.json['nome'],
        "descricao": request.json['descricao']
    }
    itens.append(novo_item)
    return jsonify(novo_item), 201

# Rota para atualizar um item
@app.route('/itens/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in itens if item['id'] == item_id), None)
    if item is None:
        return jsonify({"mensagem": "Item não encontrado"}), 404
    
    item['nome'] = request.json.get('nome', item['nome'])
    item['descricao'] = request.json.get('descricao', item['descricao'])
    
    return jsonify(item)

# Rota para excluir um item
@app.route('/itens/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global itens
    itens = [item for item in itens if item['id'] != item_id]
    return jsonify({"mensagem": "Item excluído com sucesso"})

if __name__ == '__main__':
    app.run(debug=True)
