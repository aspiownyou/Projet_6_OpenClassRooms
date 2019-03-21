# Script pour debian

def carteE(carte, fichier):
    fichier.write("\n \n# " + str(carte["num"]) + "interface \n")
    fichier.write("auto " + carte["name"] + "\n")
    fichier.write("allow-hotplug " + carte["name"] + "\n")
    fichier.write("iface " + carte["name"] + " inet static\n")
    fichier.write("    address " + carte["adresse"] + "\n")
    fichier.write("netmask " + carte["netmask"] + "\n")
    fichier.write("gateway " + carte["gateway"] + "\n")
    fichier.write("broadcast " + carte["broadcast"] + "\n")
    print(fichier)

def dhcp():
    print("en cour")

def vlan():
    print("en cour")

def routage():
    print("en cour")