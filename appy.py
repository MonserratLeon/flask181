#importacion del framework
from flask import Flask
from flask_mysqldb import MySQL


#inicializacion del APP
app= Flask(__name__)


#Configuracion de la conexion
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbexpo'
mysql= MySQL(app)


#declaracion de ruta http://localhost:5000
    @app.route('/expo')
def expo():
    return render_template('Exploracion y diagnostico 2.html')

#ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000,debug=True)

    #declaracion de ruta http://localhost:5000
    @app.route('/Administracionmedicos 2.html')
def expo():
    return render_template('Administracion medicos 2.html')

#ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000,debug=True)