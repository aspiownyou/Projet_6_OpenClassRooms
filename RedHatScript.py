# Script for configuring network interfaces and VLANS for RedHat-based versions

# Network interface file creation function
def carteE(carte):

        # Creating the file path
        chemin = "/etc/sysconfig/network-scripts/ifcfg-" + carte["name"]

        # Creating the file and editing with the data in the YAML file
        fichier = open(chemin, "w")
        fichier.write("TYPE=" + carte["type"] + "\n")
        fichier.write("BOOTPROTO=" + carte["mode"] + "\n")
        fichier.write("ONBOOT=yes \n")
        fichier.write("IPADDR=" + carte["adresse"] + "\n")
        fichier.write("NETMASK=" + carte["netmask"] + "\n")
        fichier.write("BROADCAST=" + carte["broadcast"])

        # Optional parameter
        if carte["gateway"] != '':
                fichier.write("GATEWAY=" + carte["gateway"])
        
        # Viewing the created file
        print("le fichier "+chemin+' à été créé')

        # Closing the file
        fichier.close()

# VLANS interface file creation function
def vlan(vlan):

        # Creating the file path
        chemin = "/etc/sysconfig/network-scripts/ifcfg-" + vlan["device"]

        # Creating the file and editing with the data in the YAML file
        fichier = open(chemin, "w")
        fichier.write("DEVICE=" + vlan["device"] + "\n")
        fichier.write("BOOTPROTO=" + vlan["bootproto"] + "\n")
        fichier.write("ONBOOT=yes\n")
        fichier.write("IPADDR=" + vlan["adresse"] + "\n")
        fichier.write("NETMASK=" + vlan["netmask"] + "\n")
        fichier.write("NETWORK=" + vlan["network"] + "\n")
        fichier.write("VLAN=yes")
        
        # Viewing the created file
        print("le fichier "+chemin+' à été créé')

        # Closing the file
        fichier.close()
