# from util.network import *
# from util.network import connect_to_api
from util import *
from util.bike import Bike

# Connect to API
# network.connect_to_api()

rower1 = Bike("red", "BMX", represents=True)
rower2 = Bike("blue", "BMX", represents=False)
rower1.brake()
rower1.model = "Romet"
print(rower1)
print(rower2)
lista = []
lista.append(rower1)
lista.append(rower2)
print(lista)
print(Bike.ilosc_egzemplarzy)
print(rower1.ilosc_egzemplarzy)
print(id(rower1))
print(id(rower2))

