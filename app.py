from flask import Flask,request,jsonify

app = Flask(__name__)

books_list =[
    {"id":0,"title":"Book 1","author":"Author 1"},
    {"id":1,"title":"Book 1","author":"Author 1"},
    {"id":2,"title":"Book 1","author":"Author 1"},
    {"id":3,"title":"Book 1","author":"Author 1"},
]

@app.route('/books',methods = ['GET','POST'])
def books():
    if request.method == 'GET':
        if len(books_list)>0:
            return jsonify(books_list)
        else:
            'Nothing found',404
    if request.method == 'POST':
        new_title = request.form['title']
        new_author = request.form['author']
        newId = books_list[-1]['id'] +1

        new_obj = {
            'id': newId,
            'title': new_title
            ,'author': new_author
        }
        books_list.append(new_obj)
        return jsonify(books_list),201
    
@app.route('/book/<int:id>',methods = ['GET','PUT','DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in books_list:
            if book['id'] == id:
                return jsonify(book)
            pass

    if request.method == 'PUT':
        for book in books_list:
            if book['id'] == id:
                book['author'] = request.form['author']
                book['title'] = request.form['title']
                updated_book = {
                    'id' : id,
                    'title': book['title'],
                    'author' : book['author'],
                }
                return jsonify(updated_book)
            
    if request.method == 'DELETE':
        for index,book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)
                return jsonify(books_list)


    
if __name__ == '__main__':
    app.run(debug=True)
   
