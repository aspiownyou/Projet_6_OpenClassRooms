# Script for configuring network interfaces and VLANS for OpenSuse versions

# Network interface file creation function
def carteE(carte):

    # Creating the file path
    chemin = "/etc/sysconfig/network/ifcfg-" + carte["name"]

    # Creating the file and editing with the data in the YAML file
    fichier = open(chemin, "w")
    fichier.write("TYPE='" + carte["type"] + "'\n")
    fichier.write("BOOTPROTO='" + carte["mode"] + "'\n")
    fichier.write("STARTMODE='auto' \n")
    fichier.write("IPADDR='" + carte["adresse"] + "'\n")
    fichier.write("NETMASK='" + carte["netmask"] + "'\n")
    fichier.write("NAME='" + carte["name"] + "'\n")
    fichier.write("NETWORK='" + carte["reseau"] + "'\n")
    fichier.write("BROADCAST='" + carte["broadcast"] + "'")

    # Optional parameter
    if carte["gateway"] != '':
        fichier.write("GATEWAY=" + carte["gateway"])
    
    # Viewing the created file
    print("le fichier "+chemin+' à été créé')
    fichier.close()

# VLANS interface file creation function
def vlan(vlan):

    # Creating the file path
    chemin = "/etc/sysconfig/network/ifcfg-" + vlan["interface"] + "." + vlan["num"]

    # Creating the file and editing with the data in the YAML file
    fichier = open(chemin, "w")
    fichier.write("ETHERDEVICE=" + str(vlan["interface"]) + "\n")
    fichier.write("BOOTPROTO=" + vlan["bootproto"] + "\n")
    fichier.write("ONBOOT=yes\n")
    fichier.write("IPADDR=" + vlan["adresse"] + "\n")
    fichier.write("NETMASK=" + vlan["netmask"] + "\n")
    fichier.write("NETWORK=" + vlan["network"] + "\n")
    fichier.write("VLAN_ID=" + str(vlan["num"]) + "\n")
    fichier.write("VLAN=yes")

    # Viewing the created file
    print("le fichier "+chemin+' à été créé')
    fichier.close()
