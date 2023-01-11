from GenNom import genName
from generation_rail import link , showlink
from random import randint

def gen_train_station(nbt,nbt_comp,language):
    train_stations = []
    for i in range(nbt):
        train_station = {}
        train_station["id_Station"] = i
        train_station["name"] = genName()
        train_station["city"] = genName()
        train_station["id_language"] = language[randint(0,len(language)-1)]["id_language"]
        train_station["nbt_train_track"] = randint(1,6)
        if randint(1,2) == 1:
            train_station["have_terminals"] = True
        else:
            train_station["have_terminals"] = False
        train_station["hourly"] = str(randint(0,6)) + "h00 / " + str(randint(20,24)) + "h00"
        train_station["id_company"] = randint(0,nbt_comp-1)
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

def gen_station_service(nbt,service_):
    train_stations_service = []
    for i in range(nbt):
        allservice = [service_[i]["id_service"] for i in range(len(service_))]
        for j in range(randint(0,len(allservice))):
            service = {}
            serv = allservice[randint(0,len(allservice)-1)]
            service["id_station"] = i
            service["id_service"] = serv
            allservice.remove(serv)
            train_stations_service.append(service)
    return train_stations_service

def gen_station_language(nbt,language_):
    train_stations_language = []
    for i in range(nbt):
        all_language = [language_[i]["id_language"] for i in range(len(language_))]
        for j in range(randint(1,len(all_language))):
            language = {}
            lang = all_language[randint(0,len(all_language)-1)]
            language["id_station"] = i
            language["id_language"] = lang
            all_language.remove(lang)
            train_stations_language.append(language)
    return train_stations_language

def station_lang(station, lang):
    train_stations_lang = []
    for i in range(len(station)):
        alllang = [lang[i]["id_language"] for i in range(len(lang))]
        for j in range(randint(0,len(alllang)-1)):
            lang = {}
            langue = alllang[randint(0,len(alllang)-1)]
            lang["id_station"] = i
            lang["id_language"] = langue
            alllang.remove(langue)
            train_stations_lang.append(lang)
    return train_stations_lang

def gen_journey(po):
    links = link(po)
    id = 0
    journeys = []
    for link_ in links:
        journey = {}
        journey["id_journey"] = 0
        journey["id_station_1"] = link_[0]
        journey["id_station_2"] = link_[1]
        journey["distance"] = link_[2]
        journeys.append(journey)
        id += 1
        journey = {}
        journey["id_journey"] = 0
        journey["id_station_1"] = link_[1]
        journey["id_station_2"] = link_[0]
        journey["distance"] = link_[2]
        journeys.append(journey)
        id += 1
    journeys.sort(key=lambda x: x["id_station_2"])
    journeys.sort(key=lambda x: x["id_station_1"])
    for i in range(len(journeys)):
        journeys[i]["id_journey"] = i
    return journeys

def gen_company(nbt):
    companies = []
    for i in range(nbt):
        company = {}
        company["id_company"] = i
        company["name"] = genName()
        company["email"] = "service.client@" + company["name"] + ".com"
        company["phone"] = "0" + str(randint(100000000,999999999))
        companies.append(company)
    return companies

def gen_train_journey(journeys,trains):
    train_journey = []
    for journey in journeys:
        train = []
        nbt_train = randint(1,len(trains)-1)
        while len(train)<nbt_train:
            id_train = randint(0,len(trains)-1)
            if id_train not in train:
                train.append(id_train)
        for id_train in train:
            train_journey_ = {}
            train_journey_["id_train"] = id_train
            train_journey_["id_journey"] = journey["id_journey"]
            train_journey.append(train_journey_)
    return train_journey
