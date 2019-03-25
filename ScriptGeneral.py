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
configD = yaml.safe_load(open("ConfigDHCP_pools.yaml"))
configV = yaml.safe_load(open("ConfigVLAN.yaml"))
lease = yaml.safe_load(open("ConfigDHCP_lease.yaml"))
carte={}
dhcp={}
vlan={}
max_lease = lease["Globale"]["lease_max"]
default_lease = lease["Globale"]["lease"]

def creationInterface():
    
    try:
        #differientiation des versions debian et ubuntu
        if os.path.exists("/etc/netplan/"):
            fichier = open("/etc/netplan/50-cloud-init.yaml", "w")
            fichier.write("network:\n")
            fichier.write("  version: 2\n")
            fichier.write("  ethernets:\n")
        elif os.path.exists("/etc/network/") and not os.path.exists("/etc/netplan/"):
            fichier = open("/etc/network/interfaces", "w")
            fichier.write("# The loopback network interface \nauto lo \niface lo inet loopback \n \n")

        #boucle permettant de liste et traiter les cartes une a une
        for card in configE:
            carte = configE[card]

            #lancement du script de création du fichier pour Netplan
            if os.path.exists("/etc/netplan/"):
                N.carteE(carte, fichier)

            #lancement du script de création du fichier pour base RedHat
            elif os.path.exists("/etc/sysconfig/network-scripts/") and not os.path.exists("/etc/netplan/"):
                R.carteE(carte)
    
            #lancement du script de création du fichier pour Debian
            elif os.path.exists("/etc/network/") and not os.path.exists("/etc/netplan/"):
                D.carteE(carte, fichier)

            #lancement du script de création du fichier pour OpenSuse
            elif os.path.exists("/etc/sysconfig/network/") and not os.path.exists("/etc/netplan/"):
                O.carteE(carte)

            else:
                print("Systeme non prise en charge")

        if os.path.exists("/etc/NetworkManager"):
            os.system("service NetworkManager restart")
        elif os.path.exists("/etc/network/"):
            os.system("service networking restart")
        else:
            os.system("service network restart")

    except:
        print("Problème script ajout carte plus à jour")

def creationDHCP():

    try:

        #installation du paquet isc-dhcp-server
        if os.path.exists("/etc/yum/"):
            os.system("yum install -y dhcp-server*")
        elif os.path.exists("/etc/apt/"):
            os.system("apt install -y isc-dhcp-server*")
        elif os.path.exists("/etc/zypp/"):
            os.system("zypper install -y dhcp-server*")

        # initialisation du fichier de conf avec la durée des baux par défaut
        if os.path.exists("/etc/zypp/"):
            fichierDHCP = open("/etc/dhcpd.conf", "w")
            fichierDHCP.write("# durée des baux dhcp\n")
            fichierDHCP.write("default-lease-time " + default_lease + "\n")
            fichierDHCP.write("max-lease-time " + max_lease + "\n \n \n")
            fichierDHCP.write("# config des étendues DHCP\n")
        else:
            fichierDHCP = open("/etc/dhcp/dhcpd.conf", "w")
            fichierDHCP.write("# durée des baux dhcp\n")
            fichierDHCP.write("default-lease-time " + default_lease + "\n")
            fichierDHCP.write("max-lease-time " + max_lease + "\n \n \n")
            fichierDHCP.write("# config des étendues DHCP\n")

        for dhcp_inf in configD:
            dhcp = configD[dhcp_inf]
            sdhcp.configDHCP(dhcp, fichierDHCP)

        if os.path.exists("/etc/NetworkManager"):
            os.system("service dhcpd restart")
        elif os.path.exists("/etc/network/"):
            os.system("service isc-dhcp-server restart")
        else:
            os.system("service dhcpd restart")

    except:
        print("Problème creation dhcp")


# fonction d'ajout des VLANs
def ajoutVLAN():

    try:
        #differientiation des versions debian et ubuntu
        if os.path.exists("/etc/netplan/"):
            fichier = open("/etc/netplan/50-cloud-init.yaml", "a")
            fichier.write("\n  vlans:\n")
        elif os.path.exists("/etc/network/") and not os.path.exists("/etc/netplan/"):
            fichier = open("/etc/network/interfaces", "a")
            fichier.write("\n \n")
            fichier.write("\n# declaration des vlans \n")

        #boucle permettant de liste et traiter les vlans une a une
        for vlan_inf in configV:
            vlan = configV[vlan_inf]

            #lancement du script de création du fichier pour Netplan
            if os.path.exists("/etc/netplan/"):
                N.vlan(vlan, fichier)

            #lancement du script de création du fichier pour base RedHat
            elif os.path.exists("/etc/sysconfig/network-scripts/") and not os.path.exists("/etc/netplan/"):
                R.vlan(vlan)
    
            #lancement du script de création du fichier pour Debian
            elif os.path.exists("/etc/network/") and not os.path.exists("/etc/netplan/"):
                D.vlan(vlan, fichier)

            #lancement du script de création du fichier pour OpenSuse
            elif os.path.exists("/etc/sysconfig/network/") and not os.path.exists("/etc/netplan/"):
                O.vlan(vlan)

            else:
                print("Systeme non prise en charge")
        
        if os.path.exists("/etc/NetworkManager"):
            os.system("service NetworkManager restart")
        elif os.path.exists("/etc/network/"):
            os.system("service networking restart")
        else:
            os.system("service network restart")

    except:
        print("Probleme script vlan")
        

# fonction main gérant le déroulé du script
def main():

    if len(sys.argv) < 2:
        print("Il faut un argument pour appeller le script :\n")
        print("\n        E ou e   creation d'interface(s) réseau")
        print("\n        D ou d   configuraiton d'un serveur dhcp")
        print("\n        V ou v   configuration des vlan")
    
    argument = sys.argv[1]

    if argument == 'E' or argument == 'e':
        creationInterface()
    elif argument == 'D' or argument == 'd':
        creationDHCP()
    elif argument == 'V' or argument == 'v':
        ajoutVLAN()
    else:
        print("Il faut un argument pour appeller le script :\n")
        print("\n        E ou e  creation d'interface(s) réseau")
        print("\n        D ou d  configuraiton d'un serveur dhcp")
        print("\n        V ou v  configuration des vlan")

# appel du main pour au lancement du script
main()