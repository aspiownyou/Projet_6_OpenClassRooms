#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import yaml
import datetime

# Import scripts from different supported Linux versions
import RedHatScript as R
import DebianScript as D
import NetplanScript as N
import OpenSuseScript as O
import ScriptDHCP as sdhcp

# Opening YAML configuration files
configE = yaml.safe_load(open("Config.yaml"))
configD = yaml.safe_load(open("ConfigDHCP_pools.yaml"))
configV = yaml.safe_load(open("ConfigVLAN.yaml"))
lease = yaml.safe_load(open("ConfigDHCP_lease.yaml"))

repUser = os.system("echo $HOME") + "ResultatScript.conf"
date = datetime.datetime.now()
fichConf = open(repUser, "a")
fichConf.write(str(date) + "\n")

# Creating empty dictionaries for YAML data retrieval
carte={}
dhcp={}
vlan={}

# definition of variables for the DHCP part
max_lease = lease["Globale"]["lease_max"]
default_lease = lease["Globale"]["lease"]


# Function of creating network interfaces according to the contents of the Config.yaml file
def creationInterface():
    
    try:
        # Debian and Ubuntu (version 16.04 and higher) differentiating
        if os.path.exists("/etc/netplan/"):
            fichier = open("/etc/netplan/50-cloud-init.yaml", "w")
            fichier.write("network:\n")
            fichier.write("  version: 2\n")
            fichier.write("  ethernets:\n")
        elif os.path.exists("/etc/network/") and not os.path.exists("/etc/netplan/"):
            fichier = open("/etc/network/interfaces", "w")
            fichier.write("# The loopback network interface \nauto lo \niface lo inet loopback \n \n")

        # Interface file creation loop
        for card in configE:
            carte = configE[card]

            # Launching the interface creation script for Netplan
            if os.path.exists("/etc/netplan/"):
                N.carteE(carte, fichier)
                print("L'interface " + carte["name"] + " vient d'etre ajoutée avec l'adresse : " + carte["adresse"])
                fichConf.write("L'interface " + carte["name"] + " vient d'etre ajoutée avec l'adresse : " + carte["adresse"] + "\n")

            # Launching the interface creation script for RedHat
            elif os.path.exists("/etc/sysconfig/network-scripts/") and not os.path.exists("/etc/netplan/"):
                R.carteE(carte)
                fichConf.write("L'interface " + carte["name"] + " vient d'etre ajoutée avec l'adresse : " + carte["adresse"] + "\n")
    
            # Launching the interface creation script for Debian
            elif os.path.exists("/etc/network/") and not os.path.exists("/etc/netplan/"):
                D.carteE(carte, fichier)
                print("L'interface " + carte["name"] + " vient d'etre ajoutée avec l'adresse : " + carte["adresse"])
                fichConf.write("L'interface " + carte["name"] + " vient d'etre ajoutée avec l'adresse : " + carte["adresse"] + "\n")

            # Launching the interface creation script for OpenSuse
            elif os.path.exists("/etc/sysconfig/network/") and not os.path.exists("/etc/netplan/"):
                O.carteE(carte)
                fichConf.write("L'interface " + carte["name"] + " vient d'etre ajoutée avec l'adresse : " + carte["adresse"] + "\n")

            # If OS not supported
            else:
                print("Systeme non prise en charge")

        # Running network restart commands
        if os.path.exists("/etc/NetworkManager"):
            os.system("service NetworkManager restart")
        elif os.path.exists("/etc/network/"):
            os.system("service networking restart")
        else:
            os.system("service network restart")

    except:
        print("Problème script ajout carte plus à jour")


# ISC-DHCP Server installation and configuration function
def creationDHCP():

    try:

        # Installing the ISC-DHCP-server package
        if os.path.exists("/etc/yum/"):
            os.system("yum install -y dhcp-server*")
        elif os.path.exists("/etc/apt/"):
            os.system("apt install -y isc-dhcp-server*")
        elif os.path.exists("/etc/zypp/"):
            os.system("zypper install -y dhcp-server*")

        # initializing the configuration file with the duration of the leases in the ConfigDHCP_lease.yaml file
        if os.path.exists("/etc/zypp/"):                                        # If OpenSuse
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

        # DHCP address pool fill loop
        for dhcp_inf in configD:
            dhcp = configD[dhcp_inf]
            sdhcp.configDHCP(dhcp, fichierDHCP)
            print("Configuration du pool dhcp sur le réseau " + dhcp["subnet"])
            fichConf.write("Configuration du pool dhcp sur le réseau " + dhcp["subnet"] + "\n")

        # Executing service restart commands and automatic execution at startup
        if os.path.exists("/etc/NetworkManager"):
            os.system("service dhcpd restart")
            os.system("systemctl enable dhcpd")
        elif os.path.exists("/etc/network/"):
            os.system("service isc-dhcp-server restart")
            os.system("systemctl enable dhcpd")
        else:
            os.system("service dhcpd restart")
            os.system("systemctl enable dhcpd")

    except:
        print("Problème creation dhcp")


# VLAN configuration function with ConfigVLAN.yaml file
def ajoutVLAN():

    try:
        # Debian and Ubuntu (version 16.04 and higher) differentiating
        if os.path.exists("/etc/netplan/"):
            fichier = open("/etc/netplan/50-cloud-init.yaml", "a")
            fichier.write("\n  vlans:\n")
        elif os.path.exists("/etc/network/") and not os.path.exists("/etc/netplan/"):
            fichier = open("/etc/network/interfaces", "a")
            fichier.write("\n \n")
            fichier.write("\n# declaration des vlans \n")

        # Loop filling the interfaces configuration files
        for vlan_inf in configV:
            vlan = configV[vlan_inf]

            # Launching the interface creation script for Netplan
            if os.path.exists("/etc/netplan/"):
                N.vlan(vlan, fichier)
                print("Création du VLAN " + vlan["device"] + " " + vlan["adresse"])
                fichConf.write("Création du VLAN " + vlan["device"] + " " + vlan["adresse"] + "\n")

            # Launching the interface creation script for RedHat
            elif os.path.exists("/etc/sysconfig/network-scripts/") and not os.path.exists("/etc/netplan/"):
                R.vlan(vlan)
                fichConf.write("Création du VLAN " + vlan["device"] + " " + vlan["adresse"] + "\n")
    
            # Launching the interface creation script for Debian
            elif os.path.exists("/etc/network/") and not os.path.exists("/etc/netplan/"):
                D.vlan(vlan, fichier)
                print("Création du VLAN " + vlan["device"] + " " + vlan["adresse"])
                fichConf.write("Création du VLAN " + vlan["device"] + " " + vlan["adresse"] + "\n")

            # Launching the interface creation script for OpenSuse
            elif os.path.exists("/etc/sysconfig/network/") and not os.path.exists("/etc/netplan/"):
                O.vlan(vlan)
                fichConf.write("Création du VLAN " + vlan["device"] + " " + vlan["adresse"] + "\n")

            # If OS not supported
            else:
                print("Systeme non prise en charge")
        
        # Running network restart commands
        if os.path.exists("/etc/NetworkManager"):
            os.system("service NetworkManager restart")
        elif os.path.exists("/etc/network/"):
            os.system("service networking restart")
        else:
            os.system("service network restart")

    except:
        print("Probleme script vlan")
        

# Main function managing the script's unrolled
def main():

    # Testing the presence of an argument
    if len(sys.argv) < 2:
        print("Il faut un argument pour appeller le script :\n")
        print("\n        E ou e   creation d'interface(s) réseau")
        print("\n        D ou d   configuraiton d'un serveur dhcp")
        print("\n        V ou v   configuration des vlan")
    
    # Retrieving the argument
    argument = sys.argv[1]

    # Processing the argument and launching the attached function
    if argument == 'E' or argument == 'e':
        creationInterface()
        print("Vous pourrez trouver les modifications effectué dans le fichier : " + repUser)

    elif argument == 'D' or argument == 'd':
        creationDHCP()
        print("Vous pourrez trouver les modifications effectué dans le fichier : " + repUser)
    elif argument == 'V' or argument == 'v':
        ajoutVLAN()
        print("Vous pourrez trouver les modifications effectué dans le fichier : " + repUser)
    else:
        print("Il faut un argument pour appeller le script :\n")
        print("\n        E ou e  creation d'interface(s) réseau")
        print("\n        D ou d  configuraiton d'un serveur dhcp")
        print("\n        V ou v  configuration des vlan")

# Calling the main function
main()