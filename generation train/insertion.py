#function who insert a element in a sql db

import sqlite3
from generation_train_station import *
from fixgen import *

def insert_element(table,key,element):
    element = str(element)
    con = sqlite3.connect('train.db')
    c = con.cursor()
    c.execute("INSERT INTO `"+table+"` ("+key+") VALUES ("+element+")")
    con.commit()
    con.close()

def gen_db(nbt_train,nbt_comp,X,Y):

    # generate all the data
    train,language,service = fix_gen()
    company = gen_company(nbt_comp)
    train_station = gen_train_station(nbt_train,len(company),language)
    _ , po = gen_tab(X,Y,train_station)
    journey = gen_journey(po)
    train_journey = gen_train_journey(journey,train)
    station_language = station_lang(train_station,language)
    station_service = gen_station_service(len(train_station),service)
    station_language = gen_station_language(len(train_station),language)

    # insert all the data in the db
    for company_ in company:
        key_,val = get_key_val(company_)
        insert_element("company", key_,val)
    for train_ in train:
        key_,val = get_key_val(train_)
        insert_element("train", key_,val)
    for train_station_ in train_station:
        key_,val = get_key_val(train_station_)
        insert_element("train_station", key_,val)
    for journey_ in journey:
        key_,val = get_key_val(journey_)
        insert_element("journey", key_,val)
    for train_journey_ in train_journey:
        key_,val = get_key_val(train_journey_)
        insert_element("train_journey", key_,val)
    for station_language_ in station_language:
        key_,val = get_key_val(station_language_)
        insert_element("train_station_language", key_,val)
    for station_service_ in station_service:
        key_,val = get_key_val(station_service_)
        insert_element("train_station_service", key_,val)
    for language_ in language:
        key_,val = get_key_val(language_)
        insert_element("language", key_,val)
    for service_ in service:
        key_,val = get_key_val(service_)
        insert_element("service", key_,val)
    for station_language_ in station_language:
        key_,val = get_key_val(station_language_)
        insert_element("train_station_language", key_,val)

def get_key_val(dic):
    key_ = []
    val = []
    for key in dic.keys():
        key_.append(key)
        val.append(str(dic[key]))
    key_ = ",".join(key_)
    val = "'"+"','".join(val)+"'"
    return key_ , val

gen_db(50,10,100,100)