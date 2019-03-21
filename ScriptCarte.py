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
        y = 1
        fichier = open("/etc/netplan/50-cloud-init.yaml", "w")
        fichier.write("network:\n")
        fichier.write("    version2:\n")
        fichier.write("    ethernets:\n")
    if os.path.exists("/etc/network/"):
        y = 0
        fichier = open("/etc/network/interfaces", "w")
        fichier.write("# The loopback network interface \nauto lo \niface lo inet loopback \n \n")

    for card in config:
        carte = config[card]

        if os.path.exists("/etc/netplan/") and y == 1:
            N.carteE(carte, fichier)

        elif os.path.exists("/etc/sysconfig/network-scripts/"):
            R.carteE(carte)
    
        elif os.path.exists("/etc/network/") and y == 0:
            D.carteE(carte, fichier)
            print("developpement de la partie debian en cours")

        elif os.path.exists("/etc/sysconfig/network/"):
            print("developpement de la partie opensuse en cours")

        else:
            print("Systeme non prise en charge")

def main():
    # fonction main gérant le déroulé du script
    argument = sys.argv[1]

    if argument == 'E':
        creationInterface()

# appel du main pour au lancement du script
main()