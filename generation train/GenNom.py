import random

son_syl = ["e","a","i","o","u","y","ou","ai","en","an"]
son_cons = ["z","r","t","p","qu","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n","ph","ch"]

def genName():
    nbt_syl = random.randint(3,7)
    if nbt_syl == 1:
        return son_syl[random.randint(0,len(son_syl)-1)]
    else:
        name = ""
        is_syl = False
        if random.randint(1,2) == 1:
            is_syl = True
        for i in range(nbt_syl):
            if is_syl:
                name += son_syl[random.randint(0,len(son_syl)-1)]
            else:
                name += son_cons[random.randint(0,len(son_cons)-1)]
            is_syl = not is_syl
        return name

