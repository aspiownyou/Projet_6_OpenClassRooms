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
    for card in config:
        carte = config[card]

        if os.path.exists("/etc/netplan/"):
            print("developpement de la partie netplan en cour")

        elif os.path.exists("/etc/sysconfig/network-scripts/"):
            R.carteE(carte)
    
        elif os.path.exists("/etc/network/"):
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