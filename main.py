from flask import Flask, render_template ,request
from flask import g
from flask_wtf.csrf import CSRFProtect
from flask import flash 
import forms

app=Flask(__name__)

app.secret_key = "123Tamarindo"
csrf=CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.before_request
def before_request():
    g.nombre="Mario"
    print("Before request 1")

@app.after_request
def after_request(response):
    print("after request 3")
    return response


@app.route('/')
def index():
    grupo="IDGS803"
    lista=["Juan","Eduardo","mario"]
    print("index 2")
    print("Hola {}".format(g.nombre))
    return render_template("index.html",grupo=grupo, lista=lista)

@app.route("/Alumnos", methods=["GET", "POST"])
def Alumnos():
    matricula=""
    edad=""
    nombre=""
    apellidos=""
    correo=""
    alumno_clase=forms.UserForm(request.form)
    if request.method == "POST" and alumno_clase.validate():
        matricula=alumno_clase.matricula.data
        nombre=alumno_clase.nombre.data
        edad=alumno_clase.edad.data
        apellidos=alumno_clase.apellidos.data
        correo=alumno_clase.correo.data
        mensaje="Bienvenido : {}".format(nombre)
        flash(mensaje)
    return render_template("Alumnos.html", form=alumno_clase, matricula=matricula, nombre=nombre, edad=edad, apellidos=apellidos, correo=correo)





@app.route('/ejemplo1')
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route('/ejemplo2')
def ejemplo2():
    return render_template("ejemplo2.html")


@app.route('/OperasBas')
def OperasBas():
    return render_template("OperasBas.html")


@app.route('/OperasBas', methods = ["GET", "POST"])
def funcionResultado():
    if request.method == "POST":    
        n1=int(request.form.get("n1"))
        n2=int(request.form.get("n2"))
        operacion = request.form.get("operacion")
        if operacion == "suma":
            res="La suma de {} mas {} es: {}".format(n1,n2,(n1+n2))
        if operacion == "resta":
            res="La resta de {} menos {} es: {}".format(n1,n2,(n1-n2))
        if operacion == "multi":
            res="La multiplicacion de {} por {} es: {}".format(n1,n2,(n1*n2))
        if operacion == "divicion":
            res="La divicion de {} entre {} es: {}".format(n1,n2,(n1/n2))
            
    return render_template("OperasBas.html",res=res)
       
    
@app.route('/Cinepolis', methods=["GET", "POST"])
def Cinepolis():
    proceso = ""
    boletosPorPersona = 7
    precioBoleto = 12  
    descuento_5_boletos = 0.15  
    descuento_3_5_boletos = 0.10  
    descuentoTarjeta = 0.10  

    if request.method == "POST":
        nombre = request.form.get("nombre")
        cantidadCompradores = int(request.form.get("cantidadCompradores"))
        tarjeta = request.form.get("tarjeta")
        cantidadBoletos = int(request.form.get("cantidadBoletos"))

        if (cantidadBoletos > cantidadCompradores * boletosPorPersona):
            proceso = "No se pueden vender mas de {} boletos por persona".format(boletosPorPersona)
        else:
            total = cantidadBoletos * precioBoleto

            if cantidadBoletos > 5:
                total -= total * descuento_5_boletos
                proceso = "se desconto un 15% de descuento"
            elif 3 <= cantidadBoletos <= 5:
                total -= total * descuento_3_5_boletos
                proceso = "se desconto un 10% de descuento"
            else:
                proceso = "no hubo descuento"

            if tarjeta == "Si":
                total -= total * descuentoTarjeta
                proceso += " y se aplicó un 10% de descuento mas por la tarjeta"

            proceso += " total a pagar: ${}".format(total)

    return render_template("Cinepolis.html", proceso=proceso)

  

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


@app.route("/form1")
def form1():
    return '''
    <form>
    <label>Nombre: </label>
    <br>
    <input type= "text" name="nombre" placeholder="Nombre ">
    <br><br>
    <label>Nombre: </label>
    <input type= "text" name="nombre" placeholder="Nombre ">
    <br>
    </form>

'''




if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True, port=3000)