from GenNom import genName
from generation_rail import link , showlink
from random import randint

def gen_train_station(nbt):
    train_stations = []
    for i in range(nbt):
        train_station = {}
        train_station["id_Station"] = i
        train_station["name"] = genName()
        train_station["city"] = genName()
        train_station["nbt_train_tracks"] = randint(1,6)
        if randint(1,2) == 1:
            train_station["have_terminals"] = True
        else:
            train_station["have_terminals"] = False
        train_station["hourly"] = str(randint(0,6)) + "h00 /" + str(randint(20,24)) + "h00"
        train_station["id_company"] = 0
        train_station["passengers_per_year"] = randint(100000,1000000)
        train_stations.append(train_station)
    return train_stations

def gen_tab(X,Y,train_stations):
    tab = []
    po=[]
    for i in range(Y):
        tab.append([])
        for j in range(X):
            tab[i].append(".")
    count=0
    while len(train_stations)>count:
        x,y=randint(0,X-1),randint(0,Y-1)
        if tab[y][x]==".":
            tab[y][x]=count
            po.append((count,x,y))
            count+=1
    return tab,po

train_stations = gen_train_station(10)
for i in range(len(train_stations)):
    print(train_stations[i])
tab,po = gen_tab(50,50,train_stations)
links = link(po)
for i in range(len(links)):
    print(links[i])
