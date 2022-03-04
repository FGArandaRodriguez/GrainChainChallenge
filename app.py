from flask import Flask, request,flash, redirect, render_template
from iluminate import iluminate
import datetime
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

key = os.urandom(12)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config['UPLOAD_FOLDER']='data'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/habitacion', methods=['GET'])
def rooms():
    file_name = request.args.get('file_name', None)
    proporcion = int(request.args.get('proporcion',0))

    #validamos la ruta, ya que si accedemos con esta ruta, pero con un nombre de archivo no valido,
    #nos deberá retornar al index
    if not file_name:
        #usaremos Flash para enviar un alert directamente en el front
        flash('¡Vaya!, debes cargar un archivo de habitación para poder ver la solución')
        return redirect('/')
    
    #En este caso almacenaremos el archivo en la carpeta data, por lo que especificaremos la ruta
    path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)

    #Por si se accede a la url con otro nombre de archivo, validamos que el archivo se encuentre copiado en la carpeta de data
    #De otra forma redireccionamos al index
    if not os.path.exists(path):
        flash('El archivo de la habitación a la que intentas darle solución no existe en memoria, ¡Por favor cargalo!')
        return redirect('/')

    #Comenzaremos a leer el archivo y a armar la matriz
    matriz = []
    file_lines = open(path,'r')
    for tuple in file_lines:
        row = []
        for caracter in tuple:
            #Validamos que solo vengan carácteres 1 y 0
            if caracter in ['0','1']:
                row.append(int(caracter))
        matriz.append(row)

    global max_proporcion 
    max_proporcion= 0
    proporcion_color = {}
    try:
        i = iluminate(matriz)
        i.define_ruta()
        matriz, max_proporcion, proporcion_color = i.encender_luz(proporcion = proporcion)
    except Exception as e:
        flash(str(e))
        return redirect('/')

    #Enviamos los datos al front
    render_t = render_template('habitacion.html',
        matriz = matriz,
        proporcion= proporcion,
        max_proporcion=max_proporcion,
        proporcion_color = proporcion_color,
        file_name=file_name)
    return render_t

#creamos un método para subir los archivos 
@app.route('/subir_archivo', methods=['POST'])
def upload_txt():
    files = request.files['file']
    if files.filename == '':
        flash('Debes seleccionar un archivo con una matriz para darle solución')
        return redirect('/')
    file_names = secure_filename(files.filename)
    files.save(os.path.join(app.config['UPLOAD_FOLDER'], file_names))

    return redirect(f'/habitacion?file_name={file_names}&proporcion=-1')

if  __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')