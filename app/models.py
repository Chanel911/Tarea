
from . import db
import uuid

class Producto(db.Model):
    __tablename__ = 'productos'

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.Text)
    precio = db.Column(db.Numeric)
    stock = db.Column(db.Integer, default=0)
    estatus = db.Column(db.String(15), default='DISPONIBLE')
