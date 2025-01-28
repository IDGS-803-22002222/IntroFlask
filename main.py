from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "Hola mundo!!!"


@app.route("/hola")
def hola():
    return "Holaa"

@app.route("/user/<string:user>")
def usr(user):
    return f"hola {user}!!"


@app.route("/numero/<int:n>")
def numero(n):
    return "numero {}".format(n)


@app.route("/user/<string:user>/<int:id>")
def userName(user,id):
    return "nombre {} id {}".format(user,id)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    resul=n1+n2
    return "la suma de {} mas {} es igual a {}".format(n1,n2,resul)

@app.route("/default")
@app.route("/default/<string:nom>")
def fun(nom="pedro"):
    return "el nombre de nom es "+ nom


if __name__ == '__main__':
    app.run(debug=True, port=3000)