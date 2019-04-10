# Script for configuring network interfaces and VLANS for Debian-based versions

# Network interface file creation function
def carteE(carte, fichier):

        # Editing with the data in the YAML file
        fichier.write("    " + carte["name"] + ":\n")
        if carte["mode"] == "static":
                fichier.write("      addresses: [ " + carte["adresse"] + "/" + carte["cidr"] + " ]\n")
                # Optional parameter
                if carte["gateway"] != '' :
                        fichier.write("      gateway4: " + carte["gateway"] + "\n")
        else:
                fichier.write("      dhcp4: true \n")
        

# VLANS interface file creation function
def vlan(vlan, fichier):

    # Editing with the data in the YAML file
    fichier.write("    vlan" + str(vlan["num"]) + ":\n")
    fichier.write("      id: " + str(vlan["num"]) + "\n")
    fichier.write("      link: " + vlan["interface"] + "\n")
    fichier.write("      addresses: [ " + vlan["adresse"] + "/" + vlan["cidr"] + " ]\n")
    
    # Optional parameter
    if vlan["gateway"] != '':
        fichier.write("      gateway4: " + vlan["gateway"] + "\n")
