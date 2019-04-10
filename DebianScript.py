# Script for configuring network interfaces and VLANS for Debian-based versions

# Network interface file creation function
def carteE(carte, fichier):

    # Editing with the data in the YAML file
    fichier.write("\n \n# interface " + str(carte["name"]) + "  " + str(carte["adresse"]) + "\n")
    fichier.write("auto " + carte["name"] + "\n")

    # main card allocation
    if carte["primaire"] == 'y':
        fichier.write("allow-hotplug " + carte["name"] + "\n")

    fichier.write("iface " + carte["name"] + " inet " + carte["mode"] +" \n")
    if carte["mode"] == "static":
        fichier.write("  address " + carte["adresse"] + "\n")
        fichier.write("  netmask " + carte["netmask"] + "\n")
        fichier.write("  broadcast " + carte["broadcast"] + "\n")

        # Optional parameter
        if carte["gateway"] != '':
            fichier.write("  gateway " + carte["gateway"] + "\n")    

# VLANS interface file creation function
def vlan(vlan, fichier):

    # Editing with the data in the YAML file
    fichier.write("\n\n# vlan vlan" + str(vlan["num"]) + "  " + str(vlan["adresse"]) + "\n")
    fichier.write("auto " + str(vlan["interface"]) + "." + str(vlan["num"]) + "\n")
    fichier.write("iface " + vlan["interface"] + "." + vlan["num"] + " inet static\n")
    fichier.write("  address " + vlan["adresse"] + "\n")
    fichier.write("  netmask " + vlan["netmask"] + "\n")
    fichier.write("  vlan-raw-device " + vlan["interface"])

    # Optional parameter
    if vlan["gateway"] != '':
        fichier.write("  gateway " + vlan["gateway"] + "\n")
