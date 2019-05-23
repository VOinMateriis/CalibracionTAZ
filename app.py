##########
#####	Aplicación para mover la punta de la impresora TAZ a las esquinas para calibrarla
##########
from flask import Flask, render_template, redirect, request
import os

app = Flask(__name__)


#Carga la plantilla "index.html"
@app.route('/')
def index():
	os.chdir("/home/pi/oprint/local/bin/OctoControl")	#se mueve al directorio donde están los comandos de OctoControl
	os.system("bash 8g G0 F3000")	#set speed/feedrate of move in mm/minute (between the starting point and ending point)
	tip_up()	#sube la punta (por si al inicio la punta esta en otra esquina y el su posicion de origen) para no rayar la cama al moverse
	os.system("bash 8home")	#va a "home" para calibrar la posición de la punta y moverse correctamente
	bottomLeft()	#se mueve a abajo a la izquierda para comenzar
	return render_template('index.html')	#carga la plantilla

mv2calibrate = 0	#variable que identifica en que lado de la impresora está la punta (izquierdo o derecho) para saber hacia qué lado mover la punta en la función 'calibrate'
state = 0		#variable que identifica si la punta está en una esquina o en la posición para calibrar para saber si alejar o regresar la punta en la función 'calibrate'


#Se mueve arriba a la izquierda
@app.route('/topLeft', methods = ['GET'])
def topLeft():
	global mv2calibrate	#To tell Python, that we want to use the global variable, we have to use the keyword “global”
	global state
	tip_up()	#sube la punta para no rayar la cama al moverse
	os.system("bash 8g1 x5 y280 z0")	#realiza el movimiento
	tip_home()	#regresa la punta a su posición de origen (home)
	mv2calibrate = 1	#declara que la punta está en el lado izquierdo
	state = 0		#declara que la punta está en una esquina y no en la posición para calibrar
	return ''


#Se mueve arriba a la derecha
@app.route('/topRight', methods = ['GET'])
def topRight():
	global mv2calibrate
	global state
	tip_up()
	os.system("bash 8g1 x285 y280 z0")
	tip_home()
	mv2calibrate = 2	#declara que la punta está en el lado derecho
	state = 0
	return ''


#Se mueve abajo a la izquierda
@app.route('/bottomLeft', methods = ['GET'])
def bottomLeft():
	global mv2calibrate
	global state
	tip_up()
	os.system("bash 8g1 x5 y0 z0")
	tip_home()
	mv2calibrate = 1
	state = 0
	return ''


#Se mueve abajo a la derecha
@app.route('/bottomRight', methods = ['GET'])
def bottomRight():
	global mv2calibrate
	global state
	tip_up()
	os.system("bash 8g1 x285 y0 z0")
	tip_home()
	mv2calibrate = 2
	state = 0
	return ''
	

#Aleja la punta de la esquina para dejar espacio para calibrarla
#Al volver a presionar "Calibrar" regresa la punta a la esquina
@app.route('/calibrate', methods = ['GET'])
def calibrate():
	global state	#indica a python que se va a usar las variables globales en lugar de locales
	global mv2calibrate

	tip_up()	#sube la punta para no rayar la cama al moverse
	os.system('bash 8g G91') #Después de ejecutar este comando, el posisionamiento será relativo a la posición actual
	
	#Aleja la punta de la esquina para dejar espacio para calibrar la cama
	if state == 0:	#0 = esquina
		#Aleja la punta hacia la derecha de la esquina para dejar espacio para calibrar
		if mv2calibrate == 1:	#1 = izquierda de la cama
			os.system("bash 8g1 x100")
		#Aleja la punta hacia la izquierda de la esquina para dejar espacio para calibrar
		elif mv2calibrate == 2:	#2 = derecha de la cama
			os.system("bash 8g1 x-100")
		state = 1	#Declara que la punta está alejada de la esquina para regresarla al volver a presionar "Calibrar"
	
	#Regresa la punta a la esquina
	elif state == 1:	#1 = posición para calibrar
		#Regresa la punta a la esquina desde la derecha
		if mv2calibrate == 1:
			os.system("bash 8g1 x-100")
		#Regresa la punta a la esquina desde la izquierda
		elif mv2calibrate == 2:
			os.system("bash 8g1 x100")
		state = 0	#Declara que la punta está en la esquina para alejarla y dejar espacio para calibrar al presionar "Calibrar"
		
	#print(state)
	#print(mv2calibrate)
		
	os.system('bash 8g G90') #Después de este comando, el posisionamiento vuelve a ser absoluto, es decir, relativo al origen de la impresora (HOME)
	tip_home()	#regresa la punta a su posición de origen (home)
	return ''


#Sube la punta para no rayar la cama al moverse
def tip_up():
	os.system("bash 8g1 Z5")


#Regresa la punta a su posición de origen (home)
def tip_home():
	os.system("bash 8g G28 Z")
	

if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0', port=50000)