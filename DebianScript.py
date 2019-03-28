# Script for configuring network interfaces and VLANS for Debian-based versions

# Network interface file creation function
def carteE(carte, fichier):

    # Editing with the data in the YAML file
    fichier.write("\n \n# interface " + str(carte["name"]) + str(carte["adresse"]) + "\n")
    fichier.write("auto " + carte["name"] + "\n")
    fichier.write("allow-hotplug " + carte["name"] + "\n")
    fichier.write("iface " + carte["name"] + " inet static\n")
    fichier.write("  address " + carte["adresse"] + "\n")
    fichier.write("  netmask " + carte["netmask"] + "\n")

    # Optional parameter
    if carte["gateway"] != '':
        fichier.write("  gateway " + carte["gateway"] + "\n")
    fichier.write("  broadcast " + carte["broadcast"] + "\n")

# VLANS interface file creation function
def vlan(vlan, fichier):

    # Editing with the data in the YAML file
    fichier.write("\n\n# vlan " + str(carte["name"]) + str(carte["adresse"]) + "\n")
    fichier.write("auto " + vlan["device"] + "\n")
    fichier.write("iface " + vlan["device"] + " inet static\n")
    fichier.write("  address " + vlan["adresse"] + "\n")
    fichier.write("  netmask " + vlan["netmask"] + "\n")
    fichier.write("  vlan-raw-device " + vlan["interface"])

    # Optional parameter
    if carte["gateway"] != '':
        fichier.write("  gateway " + carte["gateway"] + "\n")
