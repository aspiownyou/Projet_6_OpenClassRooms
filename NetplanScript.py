# Script pour les distributions utilisants netplan

def carteE(carte, fichier):
    fichier.write("    " + carte["name"] + ":\n")
    fichier.write("      addresses: [ " + carte["adresse"] + "/" + carte["cidr"] + " ]\n")
    if carte["gateway"] != '' :
        fichier.write("      gateway4: " + carte["gateway"] + "\n")


def vlan(vlan, fichier):
    print("en cour")

def routage():
    print("en cour")