from flask import jsonify
import sqlite3
from service.ServicioUsuario import *
from app import *
#API
class ControladorUsuario:

    serviciousuario = ServicioUsuario()
    #Para registrarse
    @app.route("/api/registro", methods = ['POST'])
    def registrar(request):
        try:
            global serviciousuario
            respuesta = serviciousuario.registrar(request) 
            return jsonify({"respuesta":f"Se registro al usuario {respuesta}"})


        except Exception as e:
            return e.__traceback__
        
    
    #Para logearse
    @app.route("api/iniciosesion", methods = ['POST'])
    def logear(request):
        try:
            global serviciousuario
            respuesta = serviciousuario.iniciarsesion(request.correo,request.clave)
            return jsonify({"respuesta":f"Se logeo al usuario {respuesta}"})

        except Exception as e:
            return e.__traceback__
        
    #Para enviar la incidencia
    
    @app.route("api/enviar", methods = ['POST'])
    def enviar():
        return jsonify({"respuesta":f"Se envio la incidencia"})