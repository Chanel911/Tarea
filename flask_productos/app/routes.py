
from flask import Blueprint, render_template, request, redirect, url_for
from .models import Producto
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    productos = Producto.query.all()
    return render_template('index.html', productos=productos)

@main.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nuevo = Producto(
            nombre=request.form['nombre'],
            descripcion=request.form['descripcion'],
            precio=request.form['precio'],
            stock=request.form['stock']
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('form.html')

@main.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    producto = Producto.query.get_or_404(id)
    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.descripcion = request.form['descripcion']
        producto.precio = request.form['precio']
        producto.stock = request.form['stock']
        producto.estatus = request.form['estatus']
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('form.html', producto=producto)

@main.route('/eliminar/<id>')
def eliminar(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('main.index'))
