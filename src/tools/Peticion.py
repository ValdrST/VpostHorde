import requests
import threading
from multiprocessing import Queue
import time
import sys
import json
from analisis import analisis
import time

class Peticion(object):
    def __init__(self,url,payload,tipo,headers, auth):
        self.payload = payload
        if(payload != None):
            self.payloadCurlADict()
        self.tipo = tipo.upper()
        self.headers = headers
        if headers != None:
            self.headerCurlADict()
        self.tiposValidos = ("POST","GET","PUT","DELETE","HEAD","OPTIONS")
        self.url = url
        self.auth = auth
        

    def payloadCurlADict(self):
        payload = {}
        datos = self.payload.split("&")
        for dato in datos:
            dato = dato.split("=")
            payload[dato[0]] = dato[1]
        self.payload = payload

    def headerCurlADict(self):
        payload = {}
        datos = self.payload.split(",")
        for dato in datos:
            dato = dato.split(":")
            payload[dato[0]] = dato[1]
        self.payload = payload

    def istipoValido(self, tipo):
        if tipo in self.tiposValidos:
            return True
        return False
    
    def get(self, resultados):
        try:
            tiempoInicio = time.time()
            r = requests.get(self.url,params = self.payload, headers = self.headers, auth = self.auth)
            respuesta = {}
            respuesta["code"] = r.status_code
        except Exception as e:
            respuesta["code"] = str(e)
        finally:
            respuesta["fecha"] = time.strftime("%c")
            respuesta["timeDate"] = time.time()
            respuesta["tiempoPeticion"] = time.time() - tiempoInicio
            resultados.append(respuesta)
            return respuesta
    
    def post(self,resultados):
        try:
            r = requests.post(self.url,data = self.payload, headers = self.headers, auth = self.auth)
            respuesta = {}
            respuesta["code"] = r.status_code
        except Exception as e:
            print(str(e))
            resultados.append(e)
        finally:
            respuesta["fecha"] = time.strftime("%c")
            respuesta["time"] = time.time()
            resultados.append(respuesta)
            return respuesta
    
    def postFile(self,resultados):
        try:
            files = {'file':open(self.payload,'rb')}
            r = requests.post(self.url,files = files, headers = self.headers, auth = self.auth)
            respuesta = {}
            respuesta["code"] = r.status_code
        except Exception as e:
            print(str(e))
            resultados.append(e)
        finally:
            respuesta["fecha"] = time.strftime("%c")
            respuesta["time"] = time.time()
            resultados.append(respuesta)
            return respuesta

    def put(self,resultados):
        try:
            r = requests.put(self.url,data = self.payload, headers = self.headers, auth = self.auth)
            respuesta = {}
            respuesta["code"] = r.status_code
        except Exception as e:
            print(str(e))
            resultados.append(e)
        finally:
            respuesta["fecha"] = time.strftime("%c")
            respuesta["time"] = time.time()
            resultados.append(respuesta)
            return respuesta

    def delete(self,resultados):
        try:
            r = requests.delete(self.url, auth = self.auth)
            respuesta = {}
            respuesta["code"] = r.status_code
        except Exception as e:
            print(str(e))
            resultados.append(e)
        finally:
            respuesta["fecha"] = time.strftime("%c")
            respuesta["time"] = time.time()
            resultados.append(respuesta)
            return respuesta
    
    def head(self,resultados):
        try:
            r = requests.head(self.url,headers = self.headers, auth = self.auth)
            respuesta = {}
            respuesta["code"] = r.status_code
        except Exception as e:
            print(str(e))
            resultados.append(e)
        finally:
            respuesta["fecha"] = time.strftime("%c")
            respuesta["time"] = time.time()
            resultados.append(respuesta)
            return respuesta
    
    def options(self,resultados):
        try:
            r = requests.options(self.url, params = self.payload, headers = self.headers, auth = self.auth)
            respuesta = {}
            respuesta["code"] = r.status_code
        except Exception as e:
            print(str(e))
            resultados.append(e)
        finally:
            respuesta["fecha"] = time.strftime("%c")
            respuesta["time"] = time.time()
            resultados.append(respuesta)
            return respuesta

    def isJson(self):
        try:
            json.loads(self.payload)
        except ValueError as e:
            print(str(e))
            return False
        return True