import random
def inicializar(request):
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
    request.session["banco1"] = request.session["banco1"] + devolver1 - prestamobanco1
    request.session["banco2"] = request.session["banco2"] + devolver2 - prestamobanco2
    request.session["marketing"] = marketing
    request.session["IyD"] = request.session["IyD"] + calidad
    request.session["ampliacionplanta"] = request.session["ampliacionplanta"] + maquinaria
    request.session["produccion"] = Produccion
    request.session["precio"] = Precio
    request.session["efectivo"] = request.session["efectivo"] - request.session["marketing"] - calidad - maquinaria + prestamobanco1 + prestamobanco2 - devolver1 - devolver2
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
        if(request.session["produccion"] == 25): request.session["cantprodproducidos"] = int(random.random(100,1000) + (request.session["ampliacionplanta"] / 50) - (request.session["IyD"] / 500000))
        elif(request.session["produccion"] == 50): request.session["cantprodproducidos"] = int(random.random(2000,3100) + (request.session["ampliacionplanta"] / 50) - (request.session["IyD"] / 500000))
        elif(request.session["produccion"] == 75): request.session["cantprodproducidos"] = int(random.random(3200,4300) + (request.session["ampliacionplanta"] / 50) - (request.session["IyD"] / 500000))
        elif (request.session["produccion"] == 100): request.session["cantprodproducidos"] = int(random.random(4400,5500) + (request.session["ampliacionplanta"] / 50) - (request.session["IyD"] / 500000))
        else: request.session["cantprodprucidos"] = random.randint(1,3)
    if(request.session["dificultad"] == 2):
        if(request.session["produccion"] == 25): request.session["cantprodproducidos"] = int(random.random(50,1000) + (request.session["ampliacionplanta"] / 50) - (request.session["IyD"] / 50000))
        elif(request.session["produccion"] == 50): request.session["cantprodproducidos"] = int(random.random(1001,2000) + (request.session["ampliacionplanta"] / 50) - (request.session["IyD"] / 50000))
        elif(request.session["produccion"] == 75): request.session["cantprodproducidos"] = int(random.random(2001,3000) + (request.session["ampliacionplanta"] / 50) - (request.session["IyD"] / 50000))
        elif (request.session["produccion"] == 100): request.session["cantprodproducidos"] = int(random.random(3001,4000) + (request.session["ampliacionplanta"] / 50) - (request.session["IyD"] / 50000))
        else: request.session["cantprodprucidos"] = random.randint(1,3)
    if(request.session["dificultad"] == 3):
        if(request.session["produccion"] == 25): request.session["cantprodproducidos"] = int(random.random(50,700) + (request.session["ampliacionplanta"] / 50) - (request.session["IyD"] / 5000))
        elif(request.session["produccion"] == 50): request.session["cantprodproducidos"] = int(random.random(701,1700) + (request.session["ampliacionplanta"] / 50) - (request.session["IyD"] / 5000))
        elif(request.session["produccion"] == 75): request.session["cantprodproducidos"] = int(random.random(1701,2500) + (request.session["ampliacionplanta"] / 50) - (request.session["IyD"] / 5000))
        elif (request.session["produccion"] == 100): request.session["cantprodproducidos"] = int(random.random(2501,3500) + (request.session["ampliacionplanta"] / 50) - (request.session["IyD"] / 5000))
        else: request.session["cantprodprucidos"] = random.randint(1,3)

def personasinteresadas(request):
    if(request.session["dificultad"] == 1):
        if(request.session["precio"] == 19.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.random(1,50) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.random(50,100) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.random(101,500) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.random(501,1000) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.random(1001,5000) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.random(5001,10000) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.random(10001,20000) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.random(20001,30000) + (request.session["IyD"] / random.random(100,500)))
            else:  request.session["personas"] = int(random.random(30001,40000) + (request.session["IyD"] / random.random(100,500)))
        if(request.session["precio"] == 29.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.random(1,40) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.random(50,90) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.random(101,400) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.random(501,900) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.random(1001,4000) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.random(5001,9000) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.random(10001,10900) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.random(20001,20900) + (request.session["IyD"] / random.random(100,500)))
            else:  request.session["personas"] = int(random.random(30001,40000) + (request.session["IyD"] / random.random(100,500)))
        if(request.session["precio"] == 39.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.random(1,30) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.random(50,80) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.random(101,300) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.random(501,800) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.random(1001,3000) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.random(5001,8000) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.random(10001,10800) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.random(20001,20800) + (request.session["IyD"] / random.random(100,500)))
            else:  request.session["personas"] = int(random.random(30001,40000) + (request.session["IyD"] / random.random(100,500)))
        if(request.session["precio"] == 49.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.random(1,20) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.random(50,70) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.random(101,400) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.random(501,700) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.random(1001,2000) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.random(5001,7000) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.random(10001,10700) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.random(20001,20700) + (request.session["IyD"] / random.random(100,500)))
            else:  request.session["personas"] = int(random.random(30001,40000) + (request.session["IyD"] / random.random(100,500)))
    elif(request.session["dificultad"] == 2):
        if(request.session["precio"] == 19.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.random(1,50) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.random(50,100) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.random(101,400) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.random(501,9000) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.random(1001,4900) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.random(5001,9000) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.random(10001,10900) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.random(20001,20900) + (request.session["IyD"] / random.random(400,500)))
            else:  request.session["personas"] = int(random.random(30001,40000) + (request.session["IyD"] / random.random(400,500)))
        if(request.session["precio"] == 29.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.random(1,40) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.random(50,90) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.random(101,300) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.random(501,800) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.random(1001,4800) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.random(5001,8000) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.random(10001,10800) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.random(20001,20800) + (request.session["IyD"] / random.random(400,500)))
            else:  request.session["personas"] = int(random.random(30001,40000) + (request.session["IyD"] / random.random(400,500)))
        if(request.session["precio"] == 39.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.random(1,30) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.random(50,80) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.random(101,200) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.random(501,900) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.random(1001,4700) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.random(5001,7000) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.random(10001,10700) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.random(20001,20700) + (request.session["IyD"] / random.random(400,500)))
            else:  request.session["personas"] = int(random.random(30001,40000) + (request.session["IyD"] / random.random(400,500)))
        if(request.session["precio"] == 49.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.random(1,20) + (request.session["IyD"] / random.random(100,500)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.random(50,70) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.random(101,200) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.random(501,800) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.random(1001,4700) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.random(5001,6000) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.random(10001,10600) + (request.session["IyD"] / random.random(400,500)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.random(20001,20600) + (request.session["IyD"] / random.random(400,500)))
            else:  request.session["personas"] = int(random.random(30001,40000) + (request.session["IyD"] / random.random(400,500)))
    
    elif(request.session["dificultad"] == 3):
        if(request.session["precio"] == 19.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.random(1,30) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.random(50,100) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.random(101,200) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.random(201,700) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.random(701,1900) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.random(1901,5000) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.random(5001,10000) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.random(10001,10900) + (request.session["IyD"] / random.random(500,700)))
            else:  request.session["personas"] = int(random.random(10001,30000) + (request.session["IyD"] / random.random(500,700)))
        if(request.session["precio"] == 29.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.random(1,20) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.random(50,90) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.random(101,190) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.random(201,600) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.random(701,1800) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.random(1901,4000) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.random(5001,9000) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.random(10001,10500) + (request.session["IyD"] / random.random(500,700)))
            else:  request.session["personas"] = int(random.random(10001,30000) + (request.session["IyD"] / random.random(500,700)))
        if(request.session["precio"] == 39.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.random(1,10) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.random(50,80) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.random(101,180) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.random(201,500) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.random(701,1700) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.random(1901,3000) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.random(5001,8000) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.random(10001,10400) + (request.session["IyD"] / random.random(500,700)))
            else:  request.session["personas"] = int(random.random(10001,30000) + (request.session["IyD"] / random.random(500,700)))
        if(request.session["precio"] == 49.99):
            if(request.session["marketing"] == 0): request.session["personas"] = int(random.random(1,10) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 1 and request.session["marketing"] <= 100): request.session["personas"] = int(random.random(50,70) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 101 and request.session["marketing"] <= 500): request.session["personas"] = int(random.random(101,170) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 501 and request.session["marketing"] <= 1000): request.session["personas"] = int(random.random(201,400) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 1001 and request.session["marketing"] <= 5000): request.session["personas"] = int(random.random(701,1600) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 5001 and request.session["marketing"] <= 10000): request.session["personas"] = int(random.random(1901,2000) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 10001 and request.session["marketing"] <= 20000): request.session["personas"] = int(random.random(5001,7000) + (request.session["IyD"] / random.random(500,700)))
            elif(request.session["marketing"] >= 20001 and request.session["marketing"] <= 30000):  request.session["personas"] = int(random.random(10001,10300) + (request.session["IyD"] / random.random(500,700)))
            else:  request.session["personas"] = int(random.random(10001,30000) + (request.session["IyD"] / random.random(500,700)))

def vender(request):
    if(request.session["cantprodproducidos"] - request.session["personas"] + request.session["stock"] >= 0):
        request.session["stock"] = request.session["stock"]  + request.session["cantprodproducidos"] - request.session["personas"]
        request.session["efectivo"] = request.session["efectivo"] + (request.session["personas"] * float(request.session["precio"]))
        request.session["cantprodvendidos"] = request.session["personas"]
    else:
        request.session["efectivo"] = request.session["efectivo"] + ((request.session["stock"] + request.session["cantproproducidos"]) * request.session["precio"])
        request.session["cantprodvendidos"] = request.session["cantprodproducidos"] + request.session["stock"]
        request.session["stock"] = 0


def gastos(request):
    if(request.session["dificultad"] == 1):
        if(request.session["produccion"] == 25):
            request.session["mantenimiento"] = random.random(500,1000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.random(500,1000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.random(500,1000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquiler"] = random.random(500,1000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.random(500,1000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.random(500,1000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)
        elif(request.session["produccion"] == 50):
            request.session["mantenimiento"] = random.random(1001,5000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.random(1001,5000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.random(1001,5000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquiler"] = random.random(1001,5000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.random(1001,5000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.random(1001,5000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)

        elif(request.session["produccion"] == 75):
            request.session["mantenimiento"] = random.random(5001,10000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.random(5001,10000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.random(5001,10000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquiler"] = random.random(5001,10000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.random(5001,10000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.random(5001,10000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)

        elif(request.session["produccion"] == 100):
            request.session["mantenimiento"] = random.random(10001,10500) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.random(10001,10500) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.random(10001,10500) + (request.session["ampliacionplanta"] / 100)
            request.session["alquiler"] = random.random(10001,10500) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.random(10001,10500) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.random(10001,10500) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)
    if(request.session["dificultad"] == 2):
        if(request.session["produccion"] == 25):
            request.session["mantenimiento"] = random.random(5001,10000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.random(5001,10000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.random(5001,10000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquiler"] = random.random(5001,10000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.random(5001,10000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.random(5001,10000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)
        elif(request.session["produccion"] == 50):
            request.session["mantenimiento"] = random.random(10001,15000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.random(10001,15000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.random(10001,15000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquiler"] = random.random(10001,15000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.random(10001,15000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.random(10001,15000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)

        elif(request.session["produccion"] == 75):
            request.session["mantenimiento"] = random.random(15001,20000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.random(15001,20000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.random(15001,20000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquiler"] = random.random(15001,20000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.random(15001,20000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.random(15001,20000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)

        elif(request.session["produccion"] == 100):
            request.session["mantenimiento"] = random.random(20001,25000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.random(20001,25000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.random(20001,25000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquiler"] = random.random(20001,25000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.random(20001,25000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.random(20001,25000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)
    if(request.session["dificultad"] == 3):
        if(request.session["produccion"] == 25):
            request.session["mantenimiento"] = random.random(15001,20000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.random(15001,20000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.random(15001,20000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquiler"] = random.random(15001,20000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.random(15001,20000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.random(15001,20000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)
        elif(request.session["produccion"] == 50):
            request.session["mantenimiento"] = random.random(20001,25000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.random(20001,25000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.random(20001,25000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquiler"] = random.random(20001,25000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.random(20001,25000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.random(20001,25000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)

        elif(request.session["produccion"] == 75):
            request.session["mantenimiento"] = random.random(25001,30000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.random(25001,30000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.random(25001,30000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquiler"] = random.random(25001,30000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.random(25001,30000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.random(25001,30000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)

        elif(request.session["produccion"] == 100):
            request.session["mantenimiento"] = random.random(30001,40000) + (request.session["ampliacionplanta"] / 1000)
            request.session["sueldos"] = random.random(30001,40000) + (request.session["ampliacionplanta"] / 100)
            request.session["impuestos"] = random.random(30001,40000) + (request.session["ampliacionplanta"] / 100)
            request.session["alquiler"] = random.random(30001,40000) + (request.session["ampliacionplanta"] / 1000) + request.session["stock"]
            request.session["suministros"] = random.random(30001,40000) + (request.session["ampliacionplanta"] / 100)
            request.session["costoprod"] = random.random(30001,40000) + (request.session["ampliacionplanta"] / 100) + (request.session["IyD"] / 100)


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
    request.session["mes"] = request.session["mes"] + 1
    band = calculosprincipales(request, prestamobanco1, prestamobanco2, Precio, Produccion, marketing, calidad, maquinaria, devolver1, devolver2)
    band1 = jugabilidad(request)
    if(band == False or band1 == False):
        return False
    else:
        return True
    

