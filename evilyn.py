from flask import Flask, jsonify, request

app = Flask(__name__)
 
filmes = [
    {
        'id': 1,
        'titulo': 'Madagascar',
        'autor': 'Eric Darnell e Tom McGrath'
    },
    {
        'id': 2,
        'titulo': 'Aladdin',
        'autor': ' Ron Clements e John Musker'
    },
    {
        'id': 3,
        'titulo': 'Carros',
        'autor': 'John Lasseter'
    }
]

#Consultar(todos)
@app.route('/filmes',methods=['GET'])
def obter_filmes():
    return jsonify(filmes)
#Consultar(ID)
@app.route('/filmes/<int:id>', methods=['GET'])
def obter_filmes_por_id(id):
    for filme in filmes:
        if filme.get('id') == id:
            return jsonify(filme)

#Editar
@app.route('/filmes/<int:id>', methods=['PUT'])
def editar_filme_por_id(id):
    filme_alterado = request.get_json()
    for indice, filme in enumerate(filmes):
        if filme.get('id') == id:
            filmes[indice].updatefilme_alterado
            return jsonify(filmes[indice])  
#Criar     
@app.route('/filmes', methods=['POST'])   
def incluir_novo_filme():
    novo_filme = request.get_json()
    filmes.append(novo_filme)
    return jsonify(filmes)

#Excluir
@app.route('/filmes/<int:id>', methods=['DELETE'])
def excluir_filme(id):
    for indice, filme in enumerate(filmes):
        if filme.get('id') == id:
            del filmes[indice]

    return jsonify(filmes)

app.run(port=5000,host='localhost',debug=True)