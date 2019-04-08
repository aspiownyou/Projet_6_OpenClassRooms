# Script for configuring network interfaces and VLANS for Debian-based versions

# Network interface file creation function
def carteE(carte, fichier):

    # Editing with the data in the YAML file
    fichier.write("    " + carte["name"] + ":\n")
    fichier.write("      addresses: [ " + carte["adresse"] + "/" + carte["cidr"] + " ]\n")
    
    # Optional parameter
    if carte["gateway"] != '' :
        fichier.write("      gateway4: " + carte["gateway"] + "\n")

# VLANS interface file creation function
def vlan(vlan, fichier):

    # Editing with the data in the YAML file
    fichier.write("  vlans:\n")
    fichier.write("    vlan" + str(vlan["device"]) + ":\n")
    fichier.write("      id: " + str(vlan["device"]) + "\n")
    fichier.write("      link: " + vlan["interface"] + "\n")
    fichier.write("      adresses: " + vlan["adresse"] + "\n")
    
    # Optional parameter
    if vlan["gateway"] != '':
        fichier.write("      gateway4: " + vlan["gateway"] + "\n")
