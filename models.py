from config import db

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

    def __repr__(self):
        return f"ID: {self.id}, Titulo: {self.titulo}, Descripcion: {self.descripcion}, Fecha: {self.fecha}"