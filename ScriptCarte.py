#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import yaml

#importation des autres scripts
import RedHatScript as R
import DebianScript as D
import NetplanScript as N
import OpenSuseScript as O

#suppression des fichiers de conf de base
#os.system("rm -r /etc/sysconfig/network/network-scripts/ifcfg-*")

config = yaml.load(open("Config.yaml"))
carte={}

#boucle permettant de liste et traiter les cartes une a une
def creationInterface():
    
    if os.path.exists("/etc/netplan/"):
        fichier = open("/etc/netplan/50-cloud-init.yaml", "w")
        fichier.write("network:\n")
        fichier.write("  version2:\n")
        fichier.write("  ethernets:\n")
    elif os.path.exists("/etc/network/") and os.path.exists("/etc/netplan/") == False:
        fichier = open("/etc/network/interfaces", "w")
        fichier.write("# The loopback network interface \nauto lo \niface lo inet loopback \n \n")

    for card in config:
        carte = config[card]

        if os.path.exists("/etc/netplan/"):
            N.carteE(carte, fichier)

        elif os.path.exists("/etc/sysconfig/network-scripts/") and os.path.exists("/etc/netplan/") == False:
            R.carteE(carte)
    
        elif os.path.exists("/etc/network/") and os.path.exists("/etc/netplan/") == False:
            D.carteE(carte, fichier)

        elif os.path.exists("/etc/sysconfig/network/") and os.path.exists("/etc/netplan/") == False:
            O.carteE(carte)

        else:
            print("Systeme non prise en charge")

def main():
    # fonction main gérant le déroulé du script
    argument = sys.argv[1]

    if argument == 'E':
        creationInterface()
    elif len(argument) < 2:
        print("Il faut un argument pour appeller le script :\n")
        print("\n        E   creation d'interface(s) réseau")
        print("\n        D   configuraiton d'un serveur dhcp")
        print("\n        V   configuration des vlan")
        print("\n        R   activation du routage")

# appel du main pour au lancement du script
main()