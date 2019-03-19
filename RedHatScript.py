# Script pour les bases Red Hat (red hat, fedora, centos)

def carteE(carte):

        x = "3"
        chemin = "/etc/sysconfig/network-scripts/ifcfg-enp0s" + x

        if carte['num'] == 1:
                fichier = open(chemin, "w")
                fichier.write("TYPE=" + carte["type"])
                fichier.close()
                fichier = open(chemin, "a")
                fichier.write("BOOTPROTO=" + carte["mode"])
                fichier.write("ONBOOT=yes")
                fichier.write("IPADDR=" + carte["adresse"])
                fichier.write("NETMASK" + carte["netmask"])
                print("le fichier "+chemin+' à été créé')
                fichier.close()
        if carte['num'] > 1:
                chemin += 5
                fichier = open(chemin, "w")
                fichier.write("TYPE=" + carte["type"])
                fichier.close()
                fichier = open(chemin, "a")
                fichier.write("BOOTPROTO=" + carte["mode"])
                fichier.write("ONBOOT=yes")
                fichier.write("IPADDR=" + carte["adresse"])
                fichier.write("NETMASK" + carte["netmask"])
                print("le fichier "+chemin+' à été créé')
        else:
                print("Impossible de créer un fichier de configuration, le fichier YAML doit etre mal renseigné.")


def dhcp():
    print("en cour")

def vlan():
    print("en cour")

def routage():
    print("en cour")