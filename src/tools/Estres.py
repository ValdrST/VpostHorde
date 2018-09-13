from Peticion import Peticion
import threading
import time
import json

class Estres(Peticion):
    def __init__(self,hilos,tiempo,url,payload,tipo,headers,auth,archivo,archivoRespuestas):
        self.hilos = hilos
        self.tiempo = tiempo
        self.file = archivo
        self.archivoRespuestas = archivoRespuestas
        Peticion.__init__(self,url,payload,tipo,headers, auth)
        self.respuestas = []

    def iniciarHilos(self):
        output = open(self.archivoRespuestas+".txt","w")
        if(self.tipo == "POST"):
            if(self.file == False):
                while(self.tiempo == None or time.time() <= time.time()+self.tiempo):
                    for i in range(int(self.hilos)):
                        thread = threading.Thread(target = self.post, args = (self.respuestas,),name=str(i+1)+" peticion")
                        thread.start()
                    thread.join()
                    if (self.tiempo==None):
                        break
                output.writelines(self.respuestas)
            else:
                while(self.tiempo == None or time.time() <= time.time()+self.tiempo):
                    for i in range(int(self.hilos)):
                        thread = threading.Thread(target = self.postFile, args = (self.respuestas,),name=str(i+1)+" peticion")
                        thread.start()
                    thread.join()
                    if (self.tiempo==None):
                        break
                output.writelines(self.respuestas)
        elif(self.tipo == "GET"):
            while(self.tiempo == None or time.time() <= time.time()+self.tiempo):
                for i in range(int(self.hilos)):
                    thread = threading.Thread(target = self.get, args = (self.respuestas,),name=str(i+1)+" peticion")
                    thread.start()
                thread.join()
                if (self.tiempo==None):
                    break
            output.writelines(str(json.dumps(self.respuestas)))
        elif(self.tipo == "DELETE"):
            while(self.tiempo == None or time.time() <= time.time()+self.tiempo):
                for i in range(int(self.hilos)):
                    thread = threading.Thread(target = self.delete, args = (self.respuestas,),name=str(i+1)+" peticion")
                    thread.start()
                thread.join()
                if (self.tiempo==None):
                    break
            output.writelines(self.respuestas)
        elif(self.tipo == "HEAD"):
            while(self.tiempo == None or time.time() <= time.time()+self.tiempo):
                for i in range(int(self.hilos)):
                    thread = threading.Thread(target = self.head, args = (self.respuestas,),name=str(i+1)+" peticion")
                    thread.start()
                thread.join()
                if (self.tiempo==None):
                    break
            output.writelines(self.respuestas)
        elif(self.tipo == "OPTIONS"):
            while(self.tiempo == None or time.time() <= time.time()+self.tiempo):
                for i in range(int(self.hilos)):
                    thread = threading.Thread(target = self.options, args = (self.respuestas,),name=str(i+1)+" peticion")
                    thread.start()
                thread.join()
                if (self.tiempo==None):
                    break
            output.writelines(self.respuestas)
        else:
            pass