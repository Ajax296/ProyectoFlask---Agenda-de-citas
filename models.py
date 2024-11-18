from config import db
from datetime import datetime

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num_documento = db.Column(db.String(255), unique=True, nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(255), unique=True, nullable= False)
    telefono = db.Column(db.Integer, unique=True, nullable=False)
    estado = db.Column(db.Boolean, default=True)
    citas = db.relationship("Cita", backref="usuario", lazy=True)


class Cita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.Boolean, default=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)

class Notificacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensaje = db.Column(db.String(255), nullable=False)
    estado_envio = db.Column(db.Boolean, default=False)
    fecha_envio = db.Column(db.DateTime, default=datetime.now())
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    cita_id = db.Column(db.Integer, db.ForeignKey("cita.id"), nullable=False)
    usuario = db.relationship("Usuario", backref="notificaciones")
    cita = db.relationship("Cita", backref="notificaciones")