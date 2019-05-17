from flask import Flask, render_template, redirect, request
import os

app = Flask(__name__)

@app.route('/')
def index():
	os.chdir("/home/pi/oprint/local/bin/OctoControl")
	return render_template('index.html')
	
@app.route('/topLeft', methods = ['GET'])
def topLeft():
	tip_up()
	os.system("bash 8g1 x5 y280 z0")
	tip_home()
	return ''
	
@app.route('/topRight', methods = ['GET'])
def topRight():
	#os.system("bash 8g G91")
	tip_up() #SUBE LA PUNTA PARA NO RAYAR LA CAMA
	os.system("bash 8g1 x285 y280 z0")	#ESPERA HASTA QUE TERMINE DE SUBIR LA PUNTA PARA MOVERSE
	tip_home()	#REGRESA LA PUNTA A HOME
	return ''
	
@app.route('/bottomLeft', methods = ['GET'])
def bottomLeft():
	tip_up()
	os.system("bash 8g1 x5 y0 z0")
	tip_home()
	return ''
	
@app.route('/bottomRight', methods = ['GET'])
def bottomRight():
	tip_up()
	os.system("bash 8g1 x285 y0 z0")
	tip_home()
	return ''
	
@app.route('/calibrate', methods = ['GET'])
def calibrate():
	tip_up()
	os.system('bash 8g G91') #Después de ejecutar este comando, el posisionamiento será relativo a la posición actual
	#if
	os.system('bash 8g1 100')
	
	os.system('bash 8g G90') #Después de este comando, el posisionamiento vuelve a ser absoluto, es decir, relativo al origen de la impresora (HOME)
	
def tip_up():
	os.system("bash 8g1 Z5") #SUBE LA PUNTA PARA NO RAYAR LA CAMA
	
def tip_home():
	os.system("bash 8g G28 Z")	#REGRESA LA PUNTA A HOME
	
if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0', port=50000)