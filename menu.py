import sqlite3
import os

def main():
    while True:
        clear()
        print("Menu")
        print("1. Select all train station")
        print("2. Select data of a train station")
        print("3. Select data base on a service")
        print("4. Select data base on a language")
        print("5. Select data base on a passengers per year")
        print("6. Select data base on a distance")
        print("7. Select data base on a company")
        print("8. Exit")
        choice = input("Enter your choice: ")
        clear()
        if choice == "1":
            print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format("id_station","name","address","hourly","id_company","passengers_per_year","id_service","id_language","id_journey"))
            printres(select_element("SELECT * FROM train_station"))
        elif choice == "2":
            id = input("Enter the id of the train station: ")
            res = select_element("SELECT * FROM train_station WHERE id_station = "+id)
            if len(res) == 0:
                print("No train station with this id")
            else:
                print("\n")
                print_station(res[0])
                
        elif choice == "3":
            services = select_element("SELECT name FROM service")
            for i in range(len(services)):
                print(str(i+1)+" : "+services[i][0])
            id = input("Enter your choice : ")
            res = ""
            try:
                printres(select_element("SELECT * FROM train_station WHERE id_Station IN (SELECT id_station FROM train_station_service WHERE id_service = "+str(int(id)-1)+")"))
            except:
                print("! bad enter !")
        elif choice == "4":
            languages = select_element("SELECT name FROM language")
            for i in range(len(languages)):
                print(str(i+1)+" : "+languages[i][0])
            id = input("Enter your choice : ")
            res = ""
            try:
                printres(select_element("SELECT * FROM train_station WHERE id_Station IN (SELECT id_station FROM train_station_language WHERE id_language = "+str(int(id)-1)+")"))
            except:
                print("! bad enter !")
        elif choice == "5":
            types = input("1 : superior\n2 : lower\n3 : equal\nEnter your choice : ")
            nbt = input("Enter the number of passenger : ")
            if types == "1":
                printres(select_element("SELECT * FROM train_station WHERE passengers_per_year >= "+nbt))
            elif types == "2":
                printres(select_element("SELECT * FROM train_station WHERE passengers_per_year <= "+nbt))
            elif types == "3":
                printres(select_element("SELECT * FROM train_station WHERE passengers_per_year = "+nbt))
        elif choice == "6":
            types = input("1 : superior\n2 : lower\n3 : equal\nEnter your choice : ")
            nbt = input("Enter the number of distance : ")
            if types == "1":
                print_journey(select_element("SELECT * FROM journey WHERE distance >= "+nbt))
            elif types == "2":
                print_journey(select_element("SELECT * FROM journey WHERE distance <= "+nbt))
            elif types == "3":
                print_journey(select_element("SELECT * FROM journey WHERE distance = "+nbt))
            
        elif choice == "7":
            companys = select_element("SELECT name FROM companys")
            for i in range(len(companys)):
                print(str(i+1)+" : "+companys[i][0])
            id = input("Enter your choice : ")
            res = ""
            try:
                printres(select_element("SELECT * FROM train_station WHERE id_Station IN (SELECT id_station FROM train_station_language WHERE id_company = "+str(int(id)-1)))
            except:
                print("! bad enter !")
        else:
            print("Goodbye")
            break
        input("\n\nPress enter to continue")

def select_element(commande):
    con = sqlite3.connect('train.db')
    c = con.cursor()
    c.execute(commande)
    result = c.fetchall()
    con.commit()
    con.close()
    return result

def printres(result):
    count = 1
    for i in result:
        for j in i:
            print('{:<20}'.format(j),end=" ")
        print()
        if count%20 == 0:
            input(str(count-19)+" to "+str(count)+" / "+str(len(result))+" result\nPress enter to continue")
        count += 1

def print_station(res):
    services = []
    temp = select_element("SELECT name FROM service WHERE id_service IN (SELECT id_service FROM train_station_service WHERE id_station = "+str(res[0])+")")
    for service in temp:
        services.append(service[0])
    language = []
    temp = select_element("SELECT name FROM language WHERE id_language IN (SELECT id_language FROM train_station_language WHERE id_station = "+str(res[0])+")")
    for service in temp:
        language.append(service[0])
    temp = select_element("SELECT * FROM company WHERE id_company = "+str(res[7]))
    company = temp[0]
    print(('{:>20} : '+str(res[0])).format("id"))
    print(('{:>20} : '+str(res[1])).format("name"))
    print(('{:>20} : '+str(res[2])).format("city"))
    print(('{:>20} : '+language[0]).format("language"))
    for i in range(1,len(language)) :
        print(" "*23 + language[i])
    print(('{:>20} : '+str(res[4])).format("nbt train track"))
    if res[5] :
        print('{:>20} : Yes'.format("have terminal"))
    else : 
        print('{:>20} : No'.format("have terminal"))
    print(('{:>20} : '+str(res[6])).format("hourly"))
    print(('{:>20} : '+str(res[8])).format("passengers per year"))
    if len(services) == 0 :
        print('{:>20} : Nothing'.format("services"))
    else :
        print(('{:>20} : '+services[0]).format("services"))
        for i in range(1,len(services)):
            print(" "*23 + services[i])
    print('{:>20} : '.format("company"))
    print(('\t{:>20} : '+str(company[1])).format("name"))
    print(('\t{:>20} : '+str(company[2])).format("e-mail"))
    print(('\t{:>20} : '+str(company[3])).format("phone number"))

def clear():
    try:
        os.system('cls')
    except:
        try:
            os.system('clear')
        except:
            print("\n\n\n\n\n")

def print_journey(journeys):
    for journey in journeys:
        name1 = select_element("SELECT name FROM train_station WHERE id_Station = "+str(journey[1]))
        name2 = select_element("SELECT name FROM train_station WHERE id_Station = "+str(journey[2]))
        print(('n°{:<5} {:<20} to n°{:<5} {:<20} with a distance of ' + str(journey[3])).format(journey[1],name1[0][0],journey[2],name2[0][0]))





 



main()