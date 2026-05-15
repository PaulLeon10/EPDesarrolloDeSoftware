from flask import request, jsonify
from dto.RespuestaUsuario import *
class ServicioUsuario:

    usuarios = dict()
    credenciales = dict()
    iterid = 1
     
    #metodo para registrar, request es de tipo requestUsuario para seguir lo del dto
    def registrar(self,request):
        #Excepcion basica
        if(request.nombre is None):
            raise Exception("No ingreso un nombre")
        respuesta = RespuestaUsuario()
        global iterid
        id = iterid + 1
        respuesta.id = request.id
        respuesta.nombre = request.nombre
        respuesta.tipo = request.tipo
        respuesta.correo = request.correo
        global usuarios
        usuarios[id] = respuesta
        global credenciales
        credenciales[request.correo] = request.clave
        return respuesta
    
    def iniciarsesion(self,correo,clave):
        if(correo not in credenciales.keys):
            raise Exception("No se encontro al usuario")
        if(credenciales.email != clave):
            raise Exception("La clave es incorrenta")
        #Si llega aca esta bien
        return "Verificacion valida" + correo


        
        

        

        






