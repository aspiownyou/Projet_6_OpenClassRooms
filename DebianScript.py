# Script pour debian

def carteE(carte, fichier):
    fichier.write("\n \n# interface " + str(carte["num"]) + "\n")
    fichier.write("auto " + carte["name"] + "\n")
    fichier.write("allow-hotplug " + carte["name"] + "\n")
    fichier.write("iface " + carte["name"] + " inet static\n")
    fichier.write("  address " + carte["adresse"] + "\n")
    fichier.write("  netmask " + carte["netmask"] + "\n")
    if carte["gateway"] != '':
        fichier.write("  gateway " + carte["gateway"] + "\n")
    fichier.write("  broadcast " + carte["broadcast"] + "\n")

def vlan(vlan, fichier):
    fichier.write("\n\n# vlan " + str(vlan["num"]) + "\n")
    fichier.write("auto " + vlan["device"] + "\n")
    fichier.write("iface " + vlan["device"] + " inet static\n")
    fichier.write("  address " + vlan["adresse"] + "\n")
    fichier.write("  netmask " + vlan["netmask"] + "\n")
    fichier.write("  vlan-raw-device " + vlan["interface"])

def routage():
    print("en cour")