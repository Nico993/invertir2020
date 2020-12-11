import random
def inicializar(request):
    request.session["dificultad"] = 0
    request.session["efectivo"] = 500000
    request.session["marketing"] = 10000
    request.session["IyD"] = 10000
    request.session["ampliacionplanta"] = 10000
    request.session["banco1"] = 100000
    request.session["banco2"] = 300000
    request.session["devolverbanco1"] = 0
    request.session["devolverbanco2"] = 0
    request.session["mes"] = 1
    request.session["personas"] = 2000
    request.session["produccion"] = 75
    request.session["precio"] = 39.99
    request.session["cantprodvendidos"] = 2000
    request.session["cantprodproducidos"] = 2000
    request.session["stock"] = 0
    request.session["mantenimiento"] = 1000
    request.session["sueldos"] = 3000
    request.session["impuestos"] = 3000
    request.session["costoprod"] = 1000
    request.session["alquieler"] = 2000
    request.session["suministros"] = 2000
    request.session["interesestotales"] = 0
def calculosprincipales(request,prestamobanco1, prestamobanco2, Precio, Produccion, marketing, calidad, maquinaria, devolver1, devolver2):
    bandefec = bandbanc = True
    request.session["banco1"] = float(request.session["banco1"]) + float(devolver1) - float(prestamobanco1)
    request.session["banco2"] = float(request.session["banco2"]) + float(devolver2) - float(prestamobanco2)
    request.session["marketing"] = float(marketing)
    request.session["IyD"] = float(request.session["IyD"]) + float(calidad)
    request.session["ampliacionplanta"] = float(request.session["ampliacionplanta"]) + float(maquinaria)
    request.session["produccion"] = float(Produccion)
    request.session["precio"] = float(Precio)
    request.session["efectivo"] = float(request.session["efectivo"]) - float(request.session["marketing"]) - float(calidad) - float(maquinaria) + float(prestamobanco1) + float(prestamobanco2) - float(devolver1) - float(devolver2)
    if request.session["efectivo"] < 0:
        bandefec = False
    if request.session["banco1"] < 0 or request.session["banco2"] < 0:
        bandbanc = False
    if bandbanc == False or bandefec == False:
        return False
    else:
        return True

def quenosepasebanco(request):
    if (request.session["banco1"] > 100000):
        request.session["banco1"] = 100000
    if(request.session["banco2"] > 300000):
        request.session["banco2"] = 300000

def devolverbanco(request):
    request.session["devolverbanco1"] = 100000 - request.session["banco1"]
    request.session["devolverbanco2"] = 300000 - request.session["banco2"]

def intereses(request):
    request.session["interesestotales"] = (request.session["devolverbanco1"] * 0.207) + (request.session["devolverbanco2"] * 0.405)

def producir(request):
    if(request.session["dificultad"] == 1):
        if(request.session["produccion"] == 25): request.session["cantprodproducidos"] = int(random.randint(100,1000) + (int(request.session["ampliacionplanta"]) / 50) - (int(request.session["IyD"]) / 500000))
        elif(request.session["produccion"] == 50): request.session["cantprodproducidos"] = int(random.randint(2000,3100) + (int(request.session["ampliacionplanta"]) / 50) - (int(request.session["IyD"]) / 500000))
        elif(request.session["produccion"] == 75): request.session["cantprodproducidos"] = int(random.randint(3200,4300) + (int(request.session["ampliacionplanta"]) / 50) - (int(request.session["IyD"]) / 500000))
        elif (request.session["produccion"] == 100): request.session["cantprodproducidos"] = int(random.randint(4400,5500) + (int(request.session["ampliacionplanta"]) / 50) - (int(request.session["IyD"]) / 500000))
        else: request.session["cantprodprucidos"] = int(random.randint(1,3))
    elif(request.session["dificultad"] == 2):
        if(request.session["produccion"] == 25): request.session["cantprodproducidos"] = int(random.randint(50,1000) + (int(request.session["ampliacionplanta"]) / 50) - (int(request.session["IyD"]) / 50000))
        elif(request.session["produccion"] == 50): request.session["cantprodproducidos"] = int(random.randint(1001,2000) + (int(request.session["ampliacionplanta"]) / 50) - (int(request.session["IyD"]) / 50000))
        elif(request.session["produccion"] == 75): request.session["cantprodproducidos"] = int(random.randint(2001,3000) + (int(request.session["ampliacionplanta"]) / 50) - (int(request.session["IyD"]) / 50000))
        elif (request.session["produccion"] == 100): request.session["cantprodproducidos"] = int(random.randint(3001,4000) + (int(request.session["ampliacionplanta"]) / 50) - (int(request.session["IyD"]) / 50000))
        else: request.session["cantprodprucidos"] = int(random.randint(1,3))
    elif(request.session["dificultad"] == 3):
        if(request.session["produccion"] == 25): request.session["cantprodproducidos"] = int(random.randint(50,700) + (int(request.session["ampliacionplanta"]) / 50) - (int(request.session["IyD"]) / 5000))
        elif(request.session["produccion"] == 50): request.session["cantprodproducidos"] = int(random.randint(701,1700) + (int(request.session["ampliacionplanta"]) / 50) - (int(request.session["IyD"]) / 5000))
        elif(request.session["produccion"] == 75): request.session["cantprodproducidos"] = int(random.randint(1701,2500) + (int(request.session["ampliacionplanta"]) / 50) - (int(request.session["IyD"]) / 5000))
        elif (request.session["produccion"] == 100): request.session["cantprodproducidos"] = int(random.randint(2501,3500) + (int(request.session["ampliacionplanta"]) / 50) - (int(request.session["IyD"]) / 5000))
        else: request.session["cantprodprucidos"] = random.randint(1,3)



def personasinteresadas(request):
    if(request.session["dificultad"] == 1):
        if(request.session["precio"] == 19.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.randint(1,50) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.randint(50,100) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.randint(101,500) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.randint(501,1000) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.randint(1001,5000) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.randint(5001,10000) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.randint(10001,20000) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.randint(20001,30000) + (request.session["IyD"] / random.randint(100,500)))
            else:  request.session["personas"] = int(random.randint(30001,40000) + (request.session["IyD"] / random.randint(100,500)))
        elif(request.session["precio"] == 29.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.randint(1,40) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.randint(50,90) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.randint(101,400) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.randint(501,900) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.randint(1001,4000) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.randint(5001,9000) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.randint(10001,10900) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.randint(20001,20900) + (request.session["IyD"] / random.randint(100,500)))
            else:  request.session["personas"] = int(random.randint(30001,40000) + (request.session["IyD"] / random.randint(100,500)))
        elif(request.session["precio"] == 39.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.randint(1,30) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.randint(50,80) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.randint(101,300) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.randint(501,800) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.randint(1001,3000) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.randint(5001,8000) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.randint(10001,10800) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.randint(20001,20800) + (request.session["IyD"] / random.randint(100,500)))
            else:  request.session["personas"] = int(random.randint(30001,40000) + (request.session["IyD"] / random.randint(100,500)))
        elif(request.session["precio"] == 49.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.randint(1,20) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.randint(50,70) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.randint(101,400) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.randint(501,700) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.randint(1001,2000) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.randint(5001,7000) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.randint(10001,10700) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.randint(20001,20700) + (request.session["IyD"] / random.randint(100,500)))
            else:  request.session["personas"] = int(random.randint(30001,40000) + (request.session["IyD"] / random.randint(100,500)))
    elif(request.session["dificultad"] == 2):
        if(request.session["precio"] == 19.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.randint(1,50) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.randint(50,100) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.randint(101,400) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.randint(501,9000) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.randint(1001,4900) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.randint(5001,9000) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.randint(10001,10900) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.randint(20001,20900) + (request.session["IyD"] / random.randint(400,500)))
            else:  request.session["personas"] = int(random.randint(30001,40000) + (request.session["IyD"] / random.randint(400,500)))
        elif(request.session["precio"] == 29.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.randint(1,40) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.randint(50,90) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.randint(101,300) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.randint(501,800) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.randint(1001,4800) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.randint(5001,8000) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.randint(10001,10800) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.randint(20001,20800) + (request.session["IyD"] / random.randint(400,500)))
            else:  request.session["personas"] = int(random.randint(30001,40000) + (request.session["IyD"] / random.randint(400,500)))
        elif(request.session["precio"] == 39.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.randint(1,30) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.randint(50,80) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.randint(101,200) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.randint(501,900) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.randint(1001,4700) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.randint(5001,7000) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.randint(10001,10700) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.randint(20001,20700) + (request.session["IyD"] / random.randint(400,500)))
            else:  request.session["personas"] = int(random.randint(30001,40000) + (request.session["IyD"] / random.randint(400,500)))
        elif(request.session["precio"] == 49.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.randint(1,20) + (request.session["IyD"] / random.randint(100,500)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.randint(50,70) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.randint(101,200) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.randint(501,800) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.randint(1001,4700) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.randint(5001,6000) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.randint(10001,10600) + (request.session["IyD"] / random.randint(400,500)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.randint(20001,20600) + (request.session["IyD"] / random.randint(400,500)))
            else:  request.session["personas"] = int(random.randint(30001,40000) + (request.session["IyD"] / random.randint(400,500)))
    
    elif(request.session["dificultad"] == 3):
        if(request.session["precio"] == 19.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.randint(1,30) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.randint(50,100) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.randint(101,200) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.randint(201,700) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.randint(701,1900) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.randint(1901,5000) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.randint(5001,10000) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.randint(10001,10900) + (request.session["IyD"] / random.randint(500,700)))
            else:  request.session["personas"] = int(random.randint(10001,30000) + (request.session["IyD"] / random.randint(500,700)))
        elif(request.session["precio"] == 29.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.randint(1,20) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.randint(50,90) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.randint(101,190) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.randint(201,600) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.randint(701,1800) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.randint(1901,4000) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.randint(5001,9000) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.randint(10001,10500) + (request.session["IyD"] / random.randint(500,700)))
            else:  request.session["personas"] = int(random.randint(10001,30000) + (request.session["IyD"] / random.randint(500,700)))
        elif(request.session["precio"] == 39.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.randint(1,10) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.randint(50,80) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.randint(101,180) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.randint(201,500) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.randint(701,1700) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.randint(1901,3000) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.randint(5001,8000) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.randint(10001,10400) + (request.session["IyD"] / random.randint(500,700)))
            else:  request.session["personas"] = int(random.randint(10001,30000) + (request.session["IyD"] / random.randint(500,700)))
        elif(request.session["precio"] == 49.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.randint(1,10) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.randint(50,70) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.randint(101,170) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.randint(201,400) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.randint(701,1600) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.randint(1901,2000) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.randint(5001,7000) + (request.session["IyD"] / random.randint(500,700)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.randint(10001,10300) + (request.session["IyD"] / random.randint(500,700)))
            else:  request.session["personas"] = int(random.randint(10001,30000) + (request.session["IyD"] / random.randint(500,700)))

def vender(request):
    if(request.session["cantprodproducidos"] - request.session["personas"] + request.session["stock"] >= 0):
        request.session["stock"] = request.session["stock"]  + request.session["cantprodproducidos"] - request.session["personas"]
        request.session["efectivo"] = request.session["efectivo"] + (request.session["personas"] * float(request.session["precio"]))
        request.session["cantprodvendidos"] = request.session["personas"]
    else:
        request.session["efectivo"] = float(request.session["efectivo"]) + float(((request.session["stock"]) + float(request.session["cantprodproducidos"])) * float(request.session["precio"]))
        request.session["cantprodvendidos"] = request.session["cantprodproducidos"] + request.session["stock"]
        request.session["stock"] = 0


def gastos(request):
    if(request.session["dificultad"] == 1):
        if(request.session["produccion"] == 25):
            request.session["mantenimiento"] = random.randint(500,1000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.randint(500,1000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.randint(500,1000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquieler"] = random.randint(500,1000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.randint(500,1000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.randint(500,1000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)
        elif(request.session["produccion"] == 50):
            request.session["mantenimiento"] = random.randint(1001,5000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.randint(1001,5000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.randint(1001,5000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquieler"] = random.randint(1001,5000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.randint(1001,5000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.randint(1001,5000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)

        elif(request.session["produccion"] == 75):
            request.session["mantenimiento"] = random.randint(5001,10000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.randint(5001,10000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.randint(5001,10000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquieler"] = random.randint(5001,10000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.randint(5001,10000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.randint(5001,10000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)

        elif(request.session["produccion"] == 100):
            request.session["mantenimiento"] = random.randint(10001,10500) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.randint(10001,10500) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.randint(10001,10500) + (request.session["ampliacionplanta"] / 100)
            request.session["alquieler"] = random.randint(10001,10500) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.randint(10001,10500) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.randint(10001,10500) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)
    if(request.session["dificultad"] == 2):
        if(request.session["produccion"] == 25):
            request.session["mantenimiento"] = random.randint(5001,10000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.randint(5001,10000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.randint(5001,10000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquieler"] = random.randint(5001,10000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.randint(5001,10000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.randint(5001,10000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)
        elif(request.session["produccion"] == 50):
            request.session["mantenimiento"] = random.randint(10001,15000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.randint(10001,15000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.randint(10001,15000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquieler"] = random.randint(10001,15000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.randint(10001,15000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.randint(10001,15000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)

        elif(request.session["produccion"] == 75):
            request.session["mantenimiento"] = random.randint(15001,20000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.randint(15001,20000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.randint(15001,20000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquieler"] = random.randint(15001,20000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.randint(15001,20000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.randint(15001,20000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)

        elif(request.session["produccion"] == 100):
            request.session["mantenimiento"] = random.randint(20001,25000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.randint(20001,25000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.randint(20001,25000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquieler"] = random.randint(20001,25000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.randint(20001,25000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.randint(20001,25000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)
    if(request.session["dificultad"] == 3):
        if(request.session["produccion"] == 25):
            request.session["mantenimiento"] = random.randint(15001,20000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.randint(15001,20000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.randint(15001,20000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquieler"] = random.randint(15001,20000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.randint(15001,20000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.randint(15001,20000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)
        elif(request.session["produccion"] == 50):
            request.session["mantenimiento"] = random.randint(20001,25000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.randint(20001,25000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.randint(20001,25000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquieler"] = random.randint(20001,25000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.randint(20001,25000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.randint(20001,25000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)

        elif(request.session["produccion"] == 75):
            request.session["mantenimiento"] = random.randint(25001,30000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.randint(25001,30000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.randint(25001,30000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquieler"] = random.randint(25001,30000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.randint(25001,30000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.randint(25001,30000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)

        elif(request.session["produccion"] == 100):
            request.session["mantenimiento"] = random.randint(30001,40000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.randint(30001,40000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.randint(30001,40000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquieler"] = random.randint(30001,40000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.randint(30001,40000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.randint(30001,40000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)

def jugabilidad(request):
    quenosepasebanco(request)
    devolverbanco(request)
    intereses(request)
    producir(request)
    personasinteresadas(request)
    vender(request)
    gastos(request)
    request.session["efectivo"] = request.session["efectivo"] - request.session["interesestotales"] - request.session["mantenimiento"] - request.session["sueldos"] - request.session["impuestos"] - request.session["costoprod"] - request.session["alquieler"] - request.session["suministros"]
    if request.session["efectivo"] < 0:
        return False
    else: 
        return True
    

def calculartodo(request, prestamobanco1, prestamobanco2, Precio, Produccion, marketing, calidad, maquinaria, devolver1, devolver2):
    band = calculosprincipales(request, prestamobanco1, prestamobanco2, Precio, Produccion, marketing, calidad, maquinaria, devolver1, devolver2)
    band1 = jugabilidad(request)
    if(band == False or band1 == False):
        return False
    else:
        return True
    

