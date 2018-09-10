import sys
import ast
def analisis():
    f = open(sys.argv[1],"r")
    fres = open(sys.argv[1]+"Res.txt","w")
    f.readline()
    estado = []
    tiempo = []
    for line in f:
        line = line [:len(line)-1]
        line = line.split(",")
        estado.append(line[0])
        tiempo.append(line[1])
    promedio = 0
    for segundos in tiempo:
        promedio = promedio + float(segundos)
        suma = promedio 
    promedio = promedio / len(tiempo)
    print(promedio)
    exito, fallo = 0,0
    for state in estado:
        if (state == "exito"):
            exito = exito + 1
        if (state == "fallo"):
            fallo = fallo + 1
    print("Tiempo promedio: " + str(promedio) + " exitos: " + str(exito) + " fallo: " + str(fallo))
    fres.write("Tiempo promedio: " + str(promedio) + " exitos: " + str(exito) + " fallo: " + str(fallo))
    f.close()
    fres.close()