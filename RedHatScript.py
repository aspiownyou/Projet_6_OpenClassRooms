# Script pour les bases Red Hat (red hat, fedora, centos)

def carteE(carte):

        x = carte["name"]
        chemin = "/etc/sysconfig/network-scripts/ifcfg-" + x
        fichier = open(chemin, "w")
        fichier.write("TYPE=" + carte["type"] + "\n")
        fichier.write("BOOTPROTO=" + carte["mode"] + "\n")
        fichier.write("ONBOOT=yes \n")
        fichier.write("IPADDR=" + carte["adresse"] + "\n")
        fichier.write("NETMASK=" + carte["netmask"] + "\n")
        fichier.write("BROADCAST=" + carte["broadcast"])
        if carte["gateway"] != '':
                fichier.write("GATEWAY=" + carte["gateway"])
        print("le fichier "+chemin+' à été créé')
        fichier.close()

def vlan(vlan):
        chemin = "/etc/sysconfig/network-scripts/ifcfg-" + vlan["device"]
        fichier = open(chemin, "w")
        fichier.write("DEVICE=" + vlan["device"] + "\n")
        fichier.write("BOOTPROTO=" + vlan["bootproto"] + "\n")
        fichier.write("ONBOOT=yes\n")
        fichier.write("IPADDR=" + vlan["adresse"] + "\n")
        fichier.write("NETMASK=" + vlan["netmask"] + "\n")
        fichier.write("NETWORK=" + vlan["network"] + "\n")
        fichier.write("VLAN=yes")

        print("en cour")
        fichier.close()
