# Script pour les distributions utilisants netplan

def carteE(carte, fichier):
    fichier.write("network:")
    fichier.write("    version2:")
    fichier.write("    ethernets:")
    fichier.write("        " + carte["name"] + ":")
    fichier.write("            addresses: " + carte["adresse"] + "/" + carte["cidr"])
    fichier.write("            gateway4: " + carte["gateway"])
    print()

def dhcp():
    print("en cour")

def vlan():
    print("en cour")

def routage():
    print("en cour")