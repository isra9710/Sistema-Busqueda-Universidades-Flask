from flask import Flask, render_template, request, session, flash, redirect, url_for, logging
import pymysql
app = Flask(__name__)
app.secret_key = "123"
conexion = pymysql.connect("localhost", "root", "", "base")
cur = conexion.cursor()
nombreUniversidad=None


@app.route('/buscar_universidad', methods=['GET', 'POST'])
def buscarUniversidad():
    nombreUniversidad=request.form.get("nombreUniversidad")
    nombre=None
    promedio=None
    consulta="select *from Universidad where nombre_universidad=%s"
    cur.execute(consulta, nombreUniversidad)
    tupla=cur.fetchone()
    if tupla is None:
        flash("No hay ninguna universidad con ese nombre")
        return redirect(url_for('hello'))
    else:
        consulta = "select nombre_universidad from Universidad where nombre_universidad=%s"
        cur.execute(consulta, nombreUniversidad)
        lista=cur.fetchone()
        for e in lista:
            nombre=e
        consulta = "select promedio from Universidad where nombre_universidad=%s"
        cur.execute(consulta, nombreUniversidad)
        lista=cur.fetchone()
        for e in lista:
            promedio=e
        return render_template('busquedaUniversidad.html', nombre=nombre, promedio=promedio)


@app.route('/buscar_universidades', methods=['GET', 'POST'])
def buscarUniversidades():
    universidad1=request.form.get("universidad1")
    universidad2=request.form.get("universidad2")
    print(universidad1)
    print(universidad2)
    if universidad1 != None and universidad2 != None:
        promedio1=None
        promedio2=None
        print("Se han ingresado dos nombres")
        consulta = ("select promedio from Universidad where nombre_universidad=%s;")
        cur.execute(consulta, universidad1)
        tupla1=cur.fetchone()
        consulta = ("select promedio from Universidad where nombre_universidad=%s;")
        cur.execute(consulta, universidad2)
        tupla2=cur.fetchone()
        if tupla1 is None or tupla2 is None:
            flash("Una de las universidades que ingresaste no existe")
            return redirect(url_for('hello'))
        else:
            for e in tupla1:
                promedio1=e
            for e in tupla2:
                promedio2=e
            print(promedio1)
            print(promedio2)
            return render_template('Index.html', universidad1=universidad1, universidad2=universidad2, promedio1=promedio1, promedio2=promedio2)
    else:
        return redirect((url_for('hello')))

@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template('Index.html')


@app.route('/registroLogin', methods=['GET', 'POST'])
def registroLogin():
    cur.execute("select nombre_universidad from Universidad")
    listat = cur.fetchall()
    lista = list(sum(listat, ()))
    if lista is None:
        flash("No hay universidades registradas, pidele al administrador que registre alguna")
        return render_template('registroLogin.html')
    else:
        for e in lista:
            print(e)
    return render_template('registroLogin.html', listaU=lista)


@app.route('/registrandote', methods=['GET', 'POST'])
def registrado():
    nombreUni = request.form.get("nombreUni")
    nombre = request.form.get("nombre")
    contra = request.form.get("contra")
    if nombreUni != "novalido":
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
        else:
            flash("Nombre de usuario ya registrado")
            redirect(url_for('registroLogin'))
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
                return redirect(url_for('registroLogin'))
    else:
        print("entra al else")
        print(nombreUni)
        return redirect(url_for('registroLogin'))


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
        else:
            flash("Ese nombre de usuario no esta registrado")
            return redirect(url_for('registroLogin'))
        consulta = ("select contra_usuario from Usuario where contra_usuario=%s;")
        cur.execute(consulta, (contra))
        lista=cur.fetchone()
        if lista!= None:
            for e in lista:
                contraAux=e
        else:
            flash("Contraseña no valida")
            return redirect(url_for('registroLogin'))

        print(nombreAux)
        print(contraAux)
        if nombre == nombreAux and contra == contraAux:
            return render_template('sesionIniciada.html')
        else:
            print("No se inicio sesion")
            flash("Falla al iniciar sesion")
            return redirect(url_for('registroLogin'))


@app.route('/crud_universidades')
def crud_universidades():
    return render_template('admin/Crud_Universidades.html')


@app.route('/mostrar_universidades')
def mostrar_universidades():
    consulta = ("select * from Universidad;")
    cur.execute(consulta)
    lista=cur.fetchall()
    consulta = ("select nombre_admin from Administrador;")
    cur.execute(consulta)
    tupla = cur.fetchall()
    administradores = list(sum(tupla, ()))
    for e in administradores:
        print(e)
    for e in lista:
        print(e[0], e[1], e[2], e[3])
    return render_template('admin/mostrar_universidades.html', universidades=lista, administradores=administradores)


@app.route('/mostrar_talleres')
def mostrar_talleres():
    consulta=("select * from Taller")
    cur.execute(consulta)
    talleres=cur.fetchall()
    consulta = ("select * from Universidad;")
    cur.execute(consulta)
    universidades = cur.fetchall()
    return render_template("admin/mostrar_talleres.html", talleres=talleres, universidades=universidades)

@app.route('/universidades')
def universidades():
    return render_template('Universidades.html')


@app.route('/top10')
def top10():
    return render_template('Top10.html')


@app.route('/home')
def home():
    return render_template('admin/home.html')


@app.route('/crud_top10')
def crud_top10():
    return render_template('admin/Crud_Top10.html')


@app.route('/universidades_admin')
def universidades_admin():
    return render_template('admin/Universidades_admin.html')


@app.route('/top10_admin')
def top10_admin():
    return render_template('admin/Top10_admin.html')




#Parte logica del CRUD de universidades
@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    nombreAdmin = request.form.get("nombreAdmin")
    nombreUniversidad = request.form.get("nombreNuevo")
    nombreAux=None
    id_admin=None
    print(nombreAdmin)
    print(nombreUniversidad)
    if nombreAdmin is not None:
        consulta = ("select nombre_universidad from Universidad where nombre_universidad=%s;")
        cur.execute(consulta, nombreUniversidad)
        lista=cur.fetchone()
        print(lista)
        if lista is not None:
            for e in lista:
                print(e)
                nombreAux=e
    else:
        flash("Selecciona el nombre de un administrador, no se agrego la universidad")
        return redirect(url_for('mostrar_universidades'))
    if nombreUniversidad==nombreAux:
        print("Esa universidad ya esta registrada")
        flash("Esa universidad ya existe!")
        return redirect(url_for('mostrar_universidades'))
    else:
        print("Estas procediendo a registrarla")
        consulta = ("select id_administrador from Administrador where nombre_admin=%s;")
        cur.execute(consulta, nombreAdmin)
        lista = cur.fetchall()
        print(lista)
        for e in lista:
            id_admin = e
            print(e)
        consulta = ("insert into Universidad (id_administrador, nombre_universidad, promedio) values(%s, %s, %s);")
        cur.execute(consulta, (id_admin, nombreUniversidad, 0.0))
        conexion.commit()
        flash("Se agrego universidad con exito")
        return redirect(url_for('mostrar_universidades'))

@app.route('/llenareditar/<string:id>', methods=['GET', 'POST'])#esta parte es para llenar el formulario con los datos traidos de "mostrar universiadades"
def llenareditar(id):
    nombreAdmin=None
    id_administrador=None
    nombreAnterior=None
    consulta="select * from Universidad where id_universidad=%s"
    cur.execute(consulta, (id))
    tupla=cur.fetchall()
    for e in tupla:
        id_administrador=e[1]
        nombreAnterior=e[1]
    print(id_administrador)
    consulta = ("select nombre_admin from Administrador;")
    cur.execute(consulta)
    tupla2 = cur.fetchall()
    administradores = list(sum(tupla2, ()))
    consulta = ("select nombre_admin from Administrador where id_administrador=%s;")
    cur.execute(consulta, id_administrador)
    tupla3=cur.fetchone()
    for e in tupla3:
        nombreAdmin=e
    print(nombreAdmin)
    return render_template("admin/editar_uni.html", universidad=tupla, administradores=administradores, nombreAdmin=nombreAdmin, nombreAnterior=nombreAnterior)


@app.route('/editar', methods=['GET', 'POST'])#esta es en si la que hace el proceso logico de editar
def editar():
    adminNombre = request.form.get("admin")
    nombre = request.form.get("nombreEditado")
    nombreAnterior= request.form.get("universidadAnterior")
    adminAnterior = request.form.get("adminAnterior")
    id_uni = request.form.get("UniEditado")
    print("Id_universidad:", id_uni)
    print("Admin nombre: ", adminNombre)
    print("NOMBRE UNI: ", nombre)
    id_administrador=None
    id_administradorAnterior=None
    nombreAux=None
    contador=0
    consulta = ("select id_administrador from Administrador where nombre_admin=%s;")
    cur.execute(consulta, adminAnterior)
    tuplaIdAnterior=cur.fetchone()
    if tuplaIdAnterior is not None:
        for e in tuplaIdAnterior:
            id_administradorAnterior=e
    consulta = ("select id_administrador from Administrador where nombre_admin=%s;")
    cur.execute(consulta, (adminNombre))
    listaID= cur.fetchone()
    if listaID is not None:
        for e in listaID:
            id_administrador=e
    print("Id_administrador: ", id_administrador)
    consulta = ("select nombre_universidad from Universidad where nombre_universidad=%s;")
    cur.execute(consulta, (nombre))
    lista=cur.fetchone()
    if lista is not None:
        for e in lista:
            nombreAux=e
        print(nombreAux)
    if nombre==nombreAnterior:
        print("El nombre nuevo y el anterior son el mismo")
        consulta="update Universidad set id_administrador=%s, nombre_universidad=%s where id_universidad=%s;"
        cur.execute(consulta, (id_administrador, nombre, id_uni))
        conexion.commit()
        flash("Universidad actualizada con exito")
        return redirect(url_for('mostrar_universidades'))
    elif(nombreAux==None):
        print("El nombre de la universidad es nuevo")
        consulta = "update Universidad set id_administrador=%s, nombre_universidad=%s where id_universidad=%s;"
        cur.execute(consulta, (id_administrador, nombre, id_uni))
        conexion.commit()
        flash("Universidad actualizada con exito")
        return redirect(url_for('mostrar_universidades'))
    elif(id_administrador!=id_administradorAnterior):
        consulta = "update Universidad set id_administrador=%s, nombre_universidad=%s where id_universidad=%s;"
        cur.execute(consulta, (id_administrador, nombre, id_uni))
        conexion.commit()
        flash("Universidad actualizada con exito")
        return redirect(url_for('mostrar_universidades'))
    else:
        flash("Esa universidad ya esta registrada")
        return redirect(url_for('mostrar_universidades'))


@app.route('/eliminar/<string:id>', methods=['GET', 'POST'])
def eliminar(id):
    consulta = ("delete from Universidad where id_universidad=%s;")
    cur.execute(consulta, (id))
    conexion.commit()
    flash("Universidad eliminada con exito")
    return redirect(url_for('mostrar_universidades'))


#Parte logia del CRUD de talleres
@app.route('/agregarTaller', methods=['GET', 'POST'])
def agregarTaller():
    nombreUniversidad = request.form.get("nombreUniversidad")
    nombreTaller = request.form.get("nombreNuevo")
    tipoTaller = request.form.get("tipoTaller")
    nombreAux=None
    id_admin=None
    print(nombreTaller)
    print(nombreUniversidad)
    print(tipoTaller)
    if nombreUniversidad is None:
        flash("Debes seleccionar una universidad")
        return redirect(url_for('mostrar_talleres'))
    else:
        consulta = ("select *from Universidad where nombre_universidad=%s;")
        cur.execute(consulta, nombreUniversidad)
        universidad=cur.fetchone()
        print(universidad[0])
        consulta = ("select * from Taller where id_universidad=%s AND nombre_taller=%s AND tipo_taller=%s ;")
        cur.execute(consulta, (universidad[0], nombreTaller, tipoTaller))
        comprobante=cur.fetchone()
        print(comprobante)

    if comprobante is None:
        print("Entra al else")
        consulta = ("insert into Taller (id_universidad, nombre_taller, tipo_taller) values(%s, %s, %s);")
        cur.execute(consulta, (universidad[0], nombreTaller, tipoTaller))
        conexion.commit()
        flash("Taller registrado con exito")
        return redirect(url_for('mostrar_talleres'))
    else:
        print("Entra al else")
        flash("Ese taller ya existe en la universidad")
        return redirect(url_for('mostrar_talleres'))


@app.route('/llenareditarTaller/<string:id>', methods=['GET', 'POST'])#esta parte es para llenar el formulario con los datos traidos de "mostrar universiadades"
def llenareditarTaller(id):
    print(id)
    id_UniversidadAnterior = None
    nombreUniversidadAnterior=None
    consulta="select * from Taller where id_talleres=%s"
    cur.execute(consulta, id)
    taller = cur.fetchall()
    print("Taller: ", taller)
    for e in taller:
        id_UniversidadAnterior=e[1]
    consulta="select nombre_universidad from Universidad where id_universidad=%s;"
    cur.execute(consulta, id_UniversidadAnterior)
    tupla=cur.fetchone()
    for e in tupla:
        nombreUniversidadAnterior=e
    print("Nombre Univesidad: ", nombreUniversidadAnterior)
    consulta="select * from Universidad"
    cur.execute(consulta)
    universidades=cur.fetchall()
    print("Todas las universidades: ")
    return render_template("admin/editarTaller.html", taller=taller, universidades=universidades, uniAnterior=nombreUniversidadAnterior)





@app.route('/editarTaller', methods=['GET', 'POST'])#esta es en si la que hace el proceso logico de editar
def editarTaller():
    nombreUniAnterior = request.form.get("uniAnterior")
    nombreUni= request.form.get("nombreUni")
    nombreAnterior= request.form.get("nombreAnterior")
    nombreNuevo = request.form.get("nombreEditado")
    tipoAnterior=request.form.get("tipoAnterior")
    tipoTaller=request.form.get("tipoTaller")
    if nombreNuevo is None:
        flash("Ingresa el nombre de taler antes de editar")
        return redirect(url_for('mostrar_talleres'))
    elif nombreNuevo==nombreAnterior and nombreUni==nombreUniAnterior and  tipoAnterior==tipoTaller:
        flash("Se actualizo de manera correcta")
        redirect(url_for('mostrar_talleres'))
    elif nombreUni != nombreUniAnterior:

        return redirect(url_for('mostrar_universidades'))


@app.route('/eliminarTaller/<string:id>', methods=['GET', 'POST'])
def eliminarTaller(id):
    consulta = ("delete from Taller where id_talleres=%s;")
    cur.execute(consulta, (id))
    conexion.commit()
    flash("Taller eliminada con exito")
    return redirect(url_for('mostrar_universidades'))



if __name__ == "__main__":
    app.run(debug = True, host= '0.0.0.0')