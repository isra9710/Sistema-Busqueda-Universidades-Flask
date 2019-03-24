from flask import Flask, render_template, request, session, flash, redirect, url_for, logging
import pymysql
app = Flask(__name__)
app.secret_key = "123"
conexion = pymysql.connect("localhost", "root", "", "base")
cur = conexion.cursor()
@app.route('/')
def hello():
   return render_template('index.html', name='Isra')


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    cur.execute("select nombre_universidad from Universidad")
    listat = cur.fetchall()
    lista = list(sum(listat, ()))
    if lista is None:
        flash("No hay universidades registradas, pidele al administrador que registre alguna")
    else:
        for e in lista:
            print(e)
    return render_template('registroLogin.html', listaU=lista)


@app.route('/registrandote', methods=['GET', 'POST'])
def registrado():
    nombreUni = request.form.get("nombreUni")
    nombre = request.form.get("nombre")
    contra = request.form.get("contra")
    nombreAux=None
    id_universidad=None
    print(nombreUni)
    print(nombre)
    print(contra)
    consulta=("select nombre_usuario from Usuario where nombre_usuario=%s;")
    cur.execute(consulta, (nombre))
    lista=cur.fetchone()
    if lista!= None:
        for e in lista:
            nombreAux=e
    print(nombreAux)
    consulta="select id_universidad from Universidad where nombre_universidad = %s;"
    cur.execute(consulta, (nombreUni))
    lista=cur.fetchone()
    if lista!= None:
        for e in lista:
            id_universidad=e
    print(id_universidad)
    if request.method =="POST":
        if nombreAux != nombre:
                consulta = ("insert into Usuario (id_universidad, nombre_usuario, contra_usuario) values(%s, %s, %s);")
                cur.execute(consulta, (id_universidad, nombre, contra))
                conexion.commit()
                print("terminado")
                return render_template('registrado.html')
        else:
            print("entra al else")
            flash("Ese correo ya esta registrado")
            return redirect(url_for('registro'))


@app.route('/iniciandoSesion', methods=['GET', 'POST'])
def sesionIniciada():

        nombre = request.form.get("nombreInicio")
        contra = request.form.get("contraInicio")
        nombreAux=None
        contraAux=None
        print(nombre)
        print(contra)
        consulta = ("select nombre_usuario from Usuario where nombre_usuario=%s;")
        cur.execute(consulta, (nombre))
        lista=cur.fetchone()
        if lista != None:
            for e in lista:
                nombreAux=e

        consulta = ("select contra_usuario from Usuario where contra_usuario=%s;")
        cur.execute(consulta, (contra))
        lista=cur.fetchone()
        if lista!= None:
            for e in lista:
                contraAux=e

        print(nombreAux)
        print(contraAux)
        if nombre == nombreAux and contra == contraAux:
            return render_template('sesionIniciada.html')
        else:
            print("No se inicio sesion")
            return redirect(url_for('registro'))



if __name__ == "__main__":
    app.run(debug = True, host= '0.0.0.0')