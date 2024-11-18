from config import app, db, mail
from models import Cita, Usuario, Notificacion
from datetime import datetime
from flask_mail import Message

#-----Crear base de datos-----
@app.cli.command("create_db")
def create_db():
    db.create_all()
    print("Base de datos creada exitosamente")

#-----CRUD usuarios-----
@app.cli.command("crear_usuario")
def crear_usuario():
    num_documento = int(input("Ingrese su numero de documento: "))
    nombre = input("Ingrese su nombre completo: ")
    correo = input("Ingrese su correo de contacto: ")
    telefono = int(input("Ingrese su telefono de contacto: "))
    usuario = Usuario(num_documento = num_documento, nombre = nombre, correo = correo, telefono = telefono)
    db.session.add(usuario)
    db.session.commit()
    print("Usuario registrado exitosamente")

@app.cli.command("consultar_usuarios")
def consultar_usuarios():
    usuarios = Usuario.query.filter(Usuario.estado == True).all()
    if usuarios:
        for usuario in usuarios:
            print(f"Nombre: {usuario.nombre}, Correo: {usuario.correo}, Telefono: {usuario.telefono}")
    else:
        print("No se encontraron registros")

@app.cli.command("actualizar_usuario")
def actualizar_usuario():
    id_usuario = int(input("Ingrese el id del usuario a actualizar: "))
    usuario = Usuario.query.filter(Usuario.id == id_usuario, Usuario.estado == True).first()
    if usuario:
        nombre = input("Ingrese su nombre completo: ")
        correo = input("Ingrese su correo de contacto: ")
        telefono = int(input("Ingrese su telefono de contacto: "))
        usuario.nombre = nombre
        usuario.correo = correo
        usuario.telefono = telefono
        db.session.commit()
        print("Usuario actualizado exitosamente")
    else:
        print("No se encontraron registros")

@app.cli.command("eliminar_usuario")
def eliminar_usuario():
    id_usuario = int(input("Ingrese el id del usuario a eliminar: "))
    usuario = Usuario.query.filter(Usuario.id == id_usuario, Usuario.estado == True).first()
    if usuario:
        usuario.estado = False
        db.session.commit()
        print("Usuario eliminado exitosamente")
    else:
        print("No se encontraron registros")

@app.cli.command("reactivar_usuario")
def reactivar_usuario():
    id_usuario = int(input("Ingrese el id del usuario a reactivar: "))
    usuario = Usuario.query.filter(Usuario.id == id_usuario, Usuario.estado == False).first()
    if usuario:
        usuario.estado = True
        db.session.commit()
        print("Usuario restaurado exitosamente")
    else:
        print("No se encontraron registros")

#-----CRUD citas-----

@app.cli.command("crear_cita")
def crear_cita():
    id_usuario = int(input("Ingrese el id del usuario que tiene esta cita: "))
    usuario = Usuario.query.filter(Usuario.id == id_usuario, Usuario.estado == True).first()
    if usuario:
        titulo = input("Ingrese el titulo de su cita: ")
        fecha_str = input("Ingrese la fecha de su cita(Año-Mes-Dia Hora:Minuto:Segundo): ")
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d %H:%M:%S')
        descripcion = input("Ingrese la descripcion de su cita: ")
        cita =  Cita(titulo=titulo, fecha=fecha, descripcion=descripcion, usuario_id=id_usuario)
        db.session.add(cita)
        db.session.commit()

        mensaje = f"Recordatorio: \nTitulo: {cita.titulo} \nFecha: {cita.fecha}"
        notificacion = Notificacion(usuario_id = id_usuario, cita_id = cita.id, mensaje = mensaje)
        db.session.add(notificacion)
        db.session.commit()
        print("Cita creada exitosamente con su respectivo recordatorio")
    else:
        print("El usuario ingresado no esta registrado en el sistema")

@app.cli.command("consultar_citas")
def consultar_citas():
    citas = Cita.query.filter(Cita.estado == True).all()
    if citas:
        for cita in citas:
            print(f"Usuario: {cita.usuario_id}, Titulo: {cita.titulo}, Descripcion: {cita.descripcion}, Fecha: {cita.fecha}")
    else:
        print("No se encontraron registros")

@app.cli.command("consultar_cita_fecha")
def consultar_cita_fecha():
    fecha_str = input("Ingrese la fecha de su cita (Año-Mes-Dia Hora:Minuto:Segundo): ")
    fecha = datetime.strptime(fecha_str, '%Y-%m-%d %H:%M:%S')
    citas = Cita.query.filter(Cita.fecha == fecha, Cita.estado == True).all()
    if citas:
        for cita in citas:
            print(f"Titulo: {cita.titulo}, Descripcion: {cita.descripcion}, Fecha: {cita.fecha}")
    else:
        print("No se encontraron registros para este dia")

@app.cli.command("consultar_cita_id")
def consultar_cita_id():
    id_consulta = int(input("Ingrese el id de la cita: "))
    cita = Cita.query.filter(Cita.id == id_consulta, Cita.estado == True).first()
    if cita:
        print(f"Titulo: {cita.titulo}, Descripcion: {cita.descripcion}, Fecha: {cita.fecha}")
    else:
        print("No se encontraron registros para este dia")

@app.cli.command("actualizar_cita")
def actualizar_cita():
    id_consulta = int(input("Ingrese el id de la cita a actualizar: "))
    cita = Cita.query.filter(Cita.id == id_consulta, Cita.estado == True).first()
    if cita:
        titulo = input("Ingrese el nuevo titulo de su cita: ")
        fecha_str = input("Ingrese la nueva fecha de su cita(Año-Mes-Dia Hora:Minuto:Segundo): ")
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d %H:%M:%S')
        descripcion = input("Ingrese la nueva descripcion de su cita: ")
        cita.titulo = titulo
        cita.fecha = fecha
        cita.descripcion = descripcion
        db.session.commit()
        print("Cita actualizada exitosamente")
    else:
        print("No se encontraron registros")

@app.cli.command("eliminar_cita")
def eliminar_cita():
    id_consulta = int(input("Ingrese el id de la cita a eliminar: "))
    cita = Cita.query.filter(Cita.id == id_consulta, Cita.estado == True).first()
    if cita:
        cita.estado = False
        db.session.commit()
        print("Cita eliminada exitosamente")
    else:
        print("No se encontraron registros")

@app.cli.command("restaurar_cita")
def restaurar_cita():
    id_consulta = int(input("Ingrese el id de la cita a restaurar: "))
    cita = Cita.query.filter(Cita.id == id_consulta, Cita.estado == False).first()
    if cita:
        cita.estado = True
        db.session.commit()
        print("Cita restaurada exitosamente")
    else:
        print("No se encontaron registros")

#-----Logica de notificaciones-----

@app.cli.command("enviar_notificacion")
def enviar_notificacion():
    fecha_actual = datetime.now()
    notificaciones = Notificacion.query.filter(Notificacion.fecha_envio <= fecha_actual, Notificacion.estado_envio == False)
    for notificacion in notificaciones:
        usuario = Usuario.query.get(notificacion.usuario_id)
        cita = Cita.query.get(notificacion.cita_id)

        msg = Message("Recordatorio de cita", sender="jr.camacho296@gmail.com", recipients=[usuario.correo])
        msg.body = notificacion.mensaje
        mail.send(msg)

        notificacion.estado_envio = True
        db.session.commit()
        print(f"Notificacion enviada al usuario {usuario.nombre} con correo {usuario.correo} para la cita {cita.titulo}")
    print("Notificaciones enviadas satisfactoriamente")