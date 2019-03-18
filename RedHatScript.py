# Script pour les bases Red Hat (red hat, fedora, centos)

x = "3"
chemin = "/etc/sysconfig/network-scripts/ifcfg-enp0s" + x

def carteE(carte):
    if carte['num'] == 1:
        fichier = open(chemin, "w")
        fichier.write("TYPE=" + carte["type"] + "/nBOOTPROTO=" + carte["mode"] + "/nONBOOT=yes /nIPADDR=" + carte["adresse"] + "/NETMASK" + carte["netmask"])


def dhcp():
    print("en cour")

def vlan():
    print("en cour")

def routage():
    print("en cour")