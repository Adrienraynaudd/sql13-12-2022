import random
import math

def gen(X,Y,nbt):
    tab = []
    po=[]
    for i in range(Y):
        tab.append([])
        for j in range(X):
            tab[i].append(".")
    count=0
    while nbt>count:
        x,y=random.randint(0,X-1),random.randint(0,Y-1)
        if tab[y][x]==".":
            tab[y][x]=count
            po.append((count,x,y))
            count+=1
    return tab,po

def display(tab):
    for i in range(len(tab)):
        str_=""
        for j in range(len(tab[i])):
            if tab[i][j]=="X":
                if j>0 and j < len(tab[i])-1 and i>0 and i<len(tab)-1 and tab[i+1][j]!="." and tab[i-1][j]!="." and tab[i][j+1]!="." and tab[i][j-1]!="." :
                    str_+="╬═"
                elif j>0 and j < len(tab[i])-1 and i>0 and tab[i-1][j]!="." and tab[i][j+1]!="." and tab[i][j-1]!="." :
                    str_+="╩═"
                elif j>0 and j < len(tab[i])-1 and i<len(tab)-1 and tab[i+1][j]!="." and tab[i][j+1]!="." and tab[i][j-1]!="." :
                    str_+="╦═"
                elif j < len(tab[i])-1 and i>0 and i<len(tab)-1 and tab[i+1][j]!="." and tab[i-1][j]!="." and tab[i][j+1]!=".":
                    str_+="╠═"
                elif j>0 and i>0 and i<len(tab)-1 and tab[i+1][j]!="." and tab[i-1][j]!="." and tab[i][j-1]!="." :
                    str_+="╣ "
                elif j>0 and j < len(tab[i])-1 and tab[i][j+1]!="." and tab[i][j-1]!="." :
                    str_+="══"
                elif i>0 and i<len(tab)-1 and tab[i+1][j]!="." and tab[i-1][j]!="." :
                    str_+="║ "
                elif j>0 and i>0 and tab[i-1][j]!="." and tab[i][j-1]!="." :
                    str_+="╝ "
                elif j < len(tab[i])-1 and i<len(tab)-1 and tab[i+1][j]!="." and tab[i][j+1]!=".":
                    str_+="╔═"
                elif j>0 and i<len(tab)-1 and tab[i+1][j]!="." and tab[i][j-1]!="." :
                    str_+="╗ "
                elif i>0 and tab[i-1][j]!="." and j<len(tab[i])-1 and tab[i][j+1]:
                    str_+="╚═"
                else:
                    str_+="X "
            elif tab[i][j] == ".":
                str_+=str(tab[i][j])+" "
            elif len(str(tab[i][j]))==1:
                str_+="0"+str(tab[i][j])
            else:
                str_+=str(tab[i][j])+""
        print(str_)

def link(tab,po):
    links = []
    for unit in po:
        poss = []
        for unit2 in po:
            if unit[0]!=unit2[0]:
                poss.append((unit[0],unit2[0],dist((unit[1],unit[2]),(unit2[1],unit2[2]))))
        poss.sort(key=takedist)
        count = 0
        i = 0
        while count!=2 and i<len(poss):
            isin = False
            for var in links:
                if (var[0]==poss[i][0] and var[1]==poss[i][1]) or (var[1]==poss[i][0] and var[0]==poss[i][1]) :
                    isin=True
                    break
            if not isin:
                links.append(poss[i])
                count+=1
            i+=1
    return links

def showlink(tab,po,links):
    for link_ in links:
        coord1=[]
        coord2=[]
        for i in po:
            if link_[0] == i[0]:
                coord1=[i[1],i[2]]
            if link_[1] == i[0]:
                coord2=[i[1],i[2]]
        dirr = [1,1]
        if coord1[0]>coord2[0]:
            dirr[0]=-1
        if coord1[1]>coord2[1]:
            dirr[1]=-1
        while coord1[0]!=coord2[0]:
            coord1[0]=coord1[0]+dirr[0]
            if tab[coord1[1]][coord1[0]]==".":
                tab[coord1[1]][coord1[0]]="X"
        while coord1[1]!=coord2[1]:
            coord1[1]=coord1[1]+dirr[1]
            if tab[coord1[1]][coord1[0]]==".":
                tab[coord1[1]][coord1[0]]="X"
    display(tab)




def dist(coord1,coord2):
    dist1 = coord1[0]-coord2[0]
    dist2 = coord1[1]-coord2[1]
    if dist1 < 0:
        dist1 = -dist1
    if dist2 < 0:
        dist2 = -dist2
    return dist1+dist2

def takedist(elem):
    return elem[2]

tab,po = gen(100,35,50)
showlink(tab,po,link(tab,po))




