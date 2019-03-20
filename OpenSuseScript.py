# Script pour OpenSuse

def carteE(carte):

    if carte['num'] == 1:
        x = "3"
        chemin = "/etc/sysconfig/network-scripts/ifcfg-enp0s" + x
        fichier = open(chemin, "w")
        fichier.write("TYPE=" + carte["type"] + "\nBOOTPROTO=" + carte["mode"] + "\nSTARTMODE=auto \nIPADDR=" + carte["adresse"] + "\nNETMASK=" + carte["netmask"] + "\nBROADCAST=" + carte["broadcast"])
        print("le fichier "+chemin+' à été créé')
    if carte['num'] > 1:
        x = carte['num'] + 6
        chemin = "/etc/sysconfig/network-scripts/ifcfg-enp0s" + str(x)
        fichier = open(chemin, "w")
        fichier.write("TYPE=" + carte["type"] + "\nBOOTPROTO=" + carte["mode"] + "\nSTARTMODE=auto \nIPADDR=" + carte["adresse"] + "\nNETMASK=" + carte["netmask"] + "\nBROADCAST=" + carte["broadcast"])
        print("le fichier "+chemin+' à été créé')
    else:
        print("probleme YAML")
    
    print()

def dhcp():
    print("en cour")

def vlan():
    print("en cour")

def routage():
    print("en cour")