# Script pour les bases Red Hat (red hat, fedora, centos)

def carteE(carte):

        x = carte["name"]
        chemin = "/etc/sysconfig/network-scripts/ifcfg-" + x
        fichier = open(chemin, "w")
        fichier.write("TYPE=" + carte["type"] + "\nBOOTPROTO=" + carte["mode"] + "\nONBOOT=yes \nIPADDR=" + carte["adresse"] + "\nNETMASK=" + carte["netmask"] + "\nBROADCAST=" + carte["broadcast"])
        print("le fichier "+chemin+' à été créé')


def dhcp():
    print("en cour")

def vlan():
    print("en cour")

def routage():
    print("en cour")