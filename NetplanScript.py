# Script pour les distributions utilisants netplan

def carteE(carte, fichier):
    fichier.write("    " + carte["name"] + ":\n")
    fichier.write("      addresses: [ " + carte["adresse"] + "/" + carte["cidr"] + " ]\n")
    if carte["gateway"] != '' :
        fichier.write("      gateway4: " + carte["gateway"] + "\n")


def vlan(vlan, fichier):
    fichier.write("  vlans:\n")
    fichier.write("    vlan" + str(vlan["num"]) + ":\n")
    fichier.write("      id: " + str(vlan["num"]) + "\n")
    fichier.write("      link: " + vlan["interface"] + "\n")
    fichier.write("      adresses: " + vlan["adresse"] + "\n")
    if vlan["gateway"] != '':
        fichier.write("      gateway4: " + vlan["gateway"] + "\n")
