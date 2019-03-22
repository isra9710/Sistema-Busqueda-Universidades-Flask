from flask import Flask, render_template
import pymysql
app = Flask(__name__)
con = pymysql.connect("localhost", "root", "", "base")
cur = con.cursor()
@app.route('/')
def hello():
   return render_template('index.html', name='Isra')


@app.route('/user/<nombre>')
def usuario(nombre='Israel'):
    edad = 21
    mi_lista = [1, 2, 3, 4]
    return render_template('registro.html', nom=nombre, edad=edad, lista=mi_lista)


@app.route('/cliente')
def cliente():
    lista_nombres = ['Prueba1', 'Prueba2', 'Prueba3']
    return render_template('cliente.html',  lista=lista_nombres)


@app.route('/registro')
def registro():
    consulta=cur.execute("select nombre_universidad from Universidad")
    listat = cur.fetchall()
    lista = list(sum(listat, ()))
    for e in lista:
        print(e)
    return render_template('registro.html', listaU=lista)


@app.route('/registrado')
def registrado():
    return render_template('registrado.html')


@app.route('/iniciarSesion')
def iniciarSesion():
    return render_template('registro.html')


@app.route('/sesionIniciada')
def sesionIniciad():
    return render_template('sesionIniciada.html')


if __name__ == "__main__":
    app.run(debug = True, host= '0.0.0.0')