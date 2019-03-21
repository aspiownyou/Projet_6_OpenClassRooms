# Script pour les distributions utilisants netplan

def carteE(carte, fichier):
    fichier.write("        " + carte["name"] + ":\n")
    fichier.write("            addresses: [ " + carte["adresse"] + "/" + carte["cidr"] + " ]\n")
    fichier.write("            broadcast: " + carte["broadcast"] + "\n")
    if carte["gateway"] != '' :
        fichier.write("            gateway4: " + carte["gateway"] + "\n")

def dhcp():
    print("en cour")

def vlan():
    print("en cour")

def routage():
    print("en cour")