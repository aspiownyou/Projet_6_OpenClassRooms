# Script for configuring network interfaces and VLANS for RedHat-based versions

# Network interface file creation function
def carteE(carte):

        # Creating the file path
        chemin = "/etc/sysconfig/network-scripts/ifcfg-" + carte["name"]

        # Creating the file and editing with the data in the YAML file
        fichier = open(chemin, "w")
        fichier.write("TYPE=" + carte["type"] + "\n")
        fichier.write("ONBOOT=yes \n")
        fichier.write("BOOTPROTO=" + carte["mode"] + "\n")
        if carte["mode"] == "static":
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
        chemin = "/etc/sysconfig/network-scripts/ifcfg-" + vlan["interface"] + "." + vlan["num"]

        # Creating the file and editing with the data in the YAML file
        fichier = open(chemin, "w")
        fichier.write("DEVICE=" + str(vlan["interface"]) + "." + str(vlan["num"]) + "\n")
        fichier.write("BOOTPROTO=" + vlan["bootproto"] + "\n")
        fichier.write("ONBOOT=yes\n")
        
        if vlan["bootproto"] == "static":
                fichier.write("IPADDR=" + vlan["adresse"] + "\n")
                fichier.write("NETMASK=" + vlan["netmask"] + "\n")
                fichier.write("NETWORK=" + vlan["network"] + "\n")
                        
        fichier.write("VLAN=yes")
        
        # Viewing the created file
        print("le fichier "+chemin+' à été créé')

        # Closing the file
        fichier.close()
