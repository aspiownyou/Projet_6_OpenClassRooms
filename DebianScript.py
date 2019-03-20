# Script pour debian

def carteE(carte, fichier):
    fichier.write("\n \n# " + str(carte["num"]) + "interface \nauto " + carte["name"] + "\nallow-hotplug " + carte["name"] + "\niface " + carte["name"] + " inet static\n" + "    address " + carte["adresse"] + "\n    netmask " + carte["netmask"] + "\n    gateway " + carte["gateway"] + "\n    broadcast " + carte["broadcast"] + "\n")
    print(fichier)

def dhcp():
    print("en cour")

def vlan():
    print("en cour")

def routage():
    print("en cour")