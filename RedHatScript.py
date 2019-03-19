# Script pour les bases Red Hat (red hat, fedora, centos)

def carteE(carte):

        if carte['num'] == 1:
                x = "3"
                chemin = "/etc/sysconfig/network-scripts/ifcfg-enp0s" + x
                fichier = open(chemin, "w")
                fichier.write("TYPE=" + carte["type"] + "\nBOOTPROTO=" + carte["mode"] + "\nONBOOT=yes \nIPADDR=" + carte["adresse"] + "\nNETMASK" + carte["netmask"])
                print("le fichier "+chemin+' à été créé')
        if carte['num'] > 1:
                x = carte['num'] + 6
                chemin = "/etc/sysconfig/network-scripts/ifcfg-enp0s" + x
                fichier = open(chemin, "w")
                fichier.write("TYPE=" + carte["type"] + "\nBOOTPROTO=" + carte["mode"] + "\nONBOOT=yes \nIPADDR=" + carte["adresse"] + "\nNETMASK" + carte["netmask"])
                print("le fichier "+chemin+' à été créé')
        else:
                print("Impossible de créer un fichier de configuration, le fichier YAML doit etre mal renseigné.")


def dhcp():
    print("en cour")

def vlan():
    print("en cour")

def routage():
    print("en cour")