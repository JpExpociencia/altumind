
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def cargar_datos():
    datos = []
    with open('datos.txt', 'r', encoding='utf-8') as f:
        for linea in f:
            fila = linea.strip().split(',')
            datos.append(fila)
    return datos

@app.route('/', methods=['GET', 'POST'])
def buscar_codigo():
    datos = cargar_datos()
    resultado = None
    codigo_buscado = ""

    if request.method == 'POST':
        codigo_buscado = request.form['codigo'].strip().upper()
        # Buscar coincidencia
        for fila in datos[1:]:
            if fila[0].upper() == codigo_buscado:
                return redirect(url_for('mostrar_detalles', codigo=codigo_buscado))

    return render_template('index.html', codigo=codigo_buscado)

@app.route('/detalles/<codigo>')
def mostrar_detalles(codigo):
    datos = cargar_datos()
    encabezados = datos[0]
    resultado = None
    for fila in datos[1:]:
        if fila[0].upper() == codigo.upper():
            resultado = fila
            break

    return render_template('detalles.html', encabezados=encabezados, resultado=resultado, codigo=codigo)

if __name__ == '__main__':
    app.run(debug=True)