from flask import Flask, render_template

app = Flask(__name__)


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
    return render_template('registro.html')


if __name__ == "__main__":
    app.run(debug = True, host= '0.0.0.0')