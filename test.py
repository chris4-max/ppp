
nom  = input("Quel est votre nom ? ")
age = input("Quel est votre age ? ")
try:
    age_prochain = int(age) + 1
except:
    print("ERREUR: Vous devez rentrer un nombre pour l'age")    
else:    
    print("vous vous appelez " + nom + " et vous avez " + str(age) + " ans")
    print("L'an prochain, vous aurez " + str(age_prochain) + " ans")

#print("Merci, passez une bonne journée")

#print(type(age))
