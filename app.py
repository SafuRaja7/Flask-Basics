from flask import Flask,request,jsonify

app = Flask(__name__)

players =[
    {"id":0,"name":"Player 1","coach":"Coach 1"},
    {"id":1,"name":"Player 2","coach":"Coach 2"},
    {"id":2,"name":"Player 3","coach":"Coach 3"},
    {"id":3,"name":"Player 4","coach":"Coach 4"},
]

@app.route('/players',methods = ['GET','POST'])
def players():
    if request.method == 'GET':
        if len(players)>0:
            return jsonify(players)
        else:
            'Nothing found',404
    if request.method == 'POST':
        new_name = request.form['name']
        new_coach = request.form['coach']
        newId = players[-1]['id'] +1

        new_obj = {
            'id': newId,
            'name': new_name,
            'coach': new_coach,
        }
        players.append(new_obj)
        return jsonify(players),201
    
@app.route('/player/<int:id>',methods = ['GET','PUT','DELETE'])
def single_player(id):
    if request.method == 'GET':
        for player in players:
            if player['id'] == id:
                return jsonify(player)
            pass

    if request.method == 'PUT':
        for player in players:
            if player['id'] == id:
                player['coach'] = request.form['coach']
                player['name'] = request.form['name']
                updated_player = {
                    'id' : id,
                    'name': player['name'],
                    'coach' : player['coach'],
                }
                return jsonify(updated_player)
            
    if request.method == 'DELETE':
        for index,player in enumerate(players):
            if player['id'] == id:
                players.pop(index)
                return jsonify(players)


    
if __name__ == '__main__':
    app.run(debug=True)
   
