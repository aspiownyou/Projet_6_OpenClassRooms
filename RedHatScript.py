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
        print("le fichier "+chemin+' à été créé')


def dhcp():
    print("en cour")

def vlan():
    print("en cour")

def routage():
    print("en cour")