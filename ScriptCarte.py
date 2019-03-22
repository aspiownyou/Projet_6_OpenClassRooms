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
import ScriptDHCP as sdhcp

#suppression des fichiers de conf de base
#os.system("rm -r /etc/sysconfig/network/network-scripts/ifcfg-*")

configE = yaml.safe_load(open("Config.yaml"))
configD = yaml.safe_load(open("ConfigDHCP.yaml"))
carte={}
dhcp={}

def creationInterface():
    
    try:
        #differientiation des versions debian et ubuntu
        if os.path.exists("/etc/netplan/"):
            fichier = open("/etc/netplan/50-cloud-init.yaml", "w")
            fichier.write("network:\n")
            fichier.write("  version: 2\n")
            fichier.write("  ethernets:\n")
        elif os.path.exists("/etc/network/") and os.path.exists("/etc/netplan/") == False:
            fichier = open("/etc/network/interfaces", "w")
            fichier.write("# The loopback network interface \nauto lo \niface lo inet loopback \n \n")

        #boucle permettant de liste et traiter les cartes une a une
        for card in configE:
            carte = configE[card]

            #lancement du script de création du fichier pour Netplan
            if os.path.exists("/etc/netplan/"):
                N.carteE(carte, fichier)

            #lancement du script de création du fichier pour base RedHat
            elif os.path.exists("/etc/sysconfig/network-scripts/") and os.path.exists("/etc/netplan/") == False:
                R.carteE(carte)
    
            #lancement du script de création du fichier pour Debian
            elif os.path.exists("/etc/network/") and os.path.exists("/etc/netplan/") == False:
                D.carteE(carte, fichier)

            #lancement du script de création du fichier pour OpenSuse
            elif os.path.exists("/etc/sysconfig/network/") and os.path.exists("/etc/netplan/") == False:
                O.carteE(carte)

            else:
                print("Systeme non prise en charge")
    except:
        print("Problème script plus à jour")

def creationDHCP():

    try:

        #installation du paquet isc-dhcp-server
        if os.path.exists("/etc/yum/"):
            os.system("yum install -y dhcp-server*")
        elif os.path.exists("/etc/apt/"):
            os.system("apt install -y isc-dhcp-server*")
        elif os.path.exists("/etc/zypp/"):
            os.system("zypper install -y dhcp-server*")

        fichierDHCP = open("/etc/dhcp/dhcpd.conf", "w")
        fichierDHCP.write("# durée des baux dhcp\n")
        fichierDHCP.write("default-lease-time  600\n")
        fichierDHCP.write("max-lease-time  7200\n \n \n")
        fichierDHCP.write("# config des étendues DHCP\n")

        for dhcp_inf in configD:
            dhcp = configD[dhcp_inf]
            sdhcp.configDHCP(dhcp, fichierDHCP)
        
        fichierDHCP.close()


    except:
        print("Problème de script")

# fonction main gérant le déroulé du script
def main():
    
    argument = sys.argv[1]

    if argument == 'E':
        creationInterface()
    if argument == 'D':
        creationDHCP()
    elif len(argument) < 2:
        print("Il faut un argument pour appeller le script :\n")
        print("\n        E   creation d'interface(s) réseau")
        print("\n        D   configuraiton d'un serveur dhcp")
        print("\n        V   configuration des vlan")
        print("\n        R   activation du routage")

# appel du main pour au lancement du script
main()