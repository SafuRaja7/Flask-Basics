from flask import Flask,request,jsonify

app = Flask(__name__)

players =[
    {"id":0,"name":"Player 1","coach":"Coach 1"},
    {"id":1,"name":"Player 2","coach":"Coach 2"},
    {"id":2,"name":"Player 3","coach":"Coach 3"},
    {"id":3,"name":"Player 4","coach":"Coach 4"},
]

@app.route('/players',methods = ['GET','POST'])
def books():
    if request.method == 'GET':
        if len(players)>0:
            return jsonify(players)
        else:
            'Nothing found',404
    if request.method == 'POST':
        new_title = request.form['name']
        new_author = request.form['coach']
        newId = players[-1]['id'] +1

        new_obj = {
            'id': newId,
            'name': new_title,
            'coach': new_author,
        }
        players.append(new_obj)
        return jsonify(players),201
    
@app.route('/player/<int:id>',methods = ['GET','PUT','DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in players:
            if book['id'] == id:
                return jsonify(book)
            pass

    if request.method == 'PUT':
        for book in players:
            if book['id'] == id:
                book['coach'] = request.form['coach']
                book['name'] = request.form['name']
                updated_book = {
                    'id' : id,
                    'name': book['name'],
                    'coach' : book['coach'],
                }
                return jsonify(updated_book)
            
    if request.method == 'DELETE':
        for index,book in enumerate(players):
            if book['id'] == id:
                players.pop(index)
                return jsonify(players)


    
if __name__ == '__main__':
    app.run(debug=True)
   
