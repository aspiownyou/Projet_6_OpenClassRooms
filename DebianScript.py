# Script pour debian

def carteE(carte, fichier):
    fichier.write("# " + str(carte["num"]) + "interface \niface " + carte["name"] + " inet static\n" + "    address " + carte["adresse"] + "\n    netmask " + carte["netmask"] + "\n    gateway " + carte["gateway"])
    print(fichier)

def dhcp():
    print("en cour")

def vlan():
    print("en cour")

def routage():
    print("en cour")