#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
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

# Creating the configuration file
repUser = "/tmp/ResultatScript.conf"

# Retrieving date and time
date = datetime.datetime.now()

# Ouverture et inscription de la date et de l'heure dans le nouveau fichier
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
        
################### Linux distribution detection ###################
        
        # Netplan (Ubuntu 16.04 and later)
        if os.path.exists("/etc/netplan/"): 
    
            # Opening the Netplan configuration file
            fichier = open("/etc/netplan/50-cloud-init.yaml", "w")
            fichier.write("network:\n")
            fichier.write("  version: 2\n")
            fichier.write("  ethernets:\n")

            # Interface configuration loop
            for card in configE:
                carte = configE[card]
                N.carteE(carte, fichier)    # Calling the interface configuration function in the NetplanScript.py script

                # Display of the configured interface
                print("L'interface " + carte["name"] + " vient d'etre ajoutée avec l'adresse : " + carte["adresse"])

                # Saving configurations to a ResultatScript.conf file
                fichConf.write("L'interface " + carte["name"] + " vient d'etre ajoutée avec l'adresse : " + carte["adresse"] + "\n")
    
            # Application of changes
            os.system("netplan apply")
            print("Redémarrage du service réseau...")
            time.sleep(10)

        # Debian-based
        elif os.path.exists("/etc/network/") and not os.path.exists("/etc/netplan/"):
    
            # Stopping network service
            os.system("service networking stop")
            print("Arret du service réseau...")
            time.sleep(5)

            # Opening interfaces configuration file
            fichier = open("/etc/network/interfaces", "w")
            fichier.write("# The loopback network interface \nauto lo \niface lo inet loopback \n \n")

            # Interface configuration loop
            for card in configE:
                carte = configE[card]
                D.carteE(carte, fichier)  # Calling the interface configuration function in the DebianScript.py script

                # Display of the configured interface
                print("L'interface " + carte["name"] + " vient d'etre ajoutée avec l'adresse : " + carte["adresse"])
                
                # Saving configurations to a ResultatScript.conf file
                fichConf.write("L'interface " + carte["name"] + " vient d'etre ajoutée avec l'adresse : " + carte["adresse"] + "\n")

            # Starting network service
            os.system("service networking start")
            print("Redémarrage du service réseau...")
            time.sleep(10)

        # Red-Hat-based
        elif os.path.exists("/etc/sysconfig/network-scripts/"):
            if os.path.exists("/etc/NetworkManager/"):   # Fedora
                
                # Stopping NetworkManager
                os.system("service NetworkManager stop")
                print("Arret du service réseau...")
                time.sleep(5)
            else:
                
                # Stopping network service
                os.system("service network stop")
                print("Arret du service réseau...")
                time.sleep(5)

            # Interface configuration loop
            for card in configE:
                carte = configE[card]
                R.carteE(carte)    # Calling the interface configuration function in the RedHatScript.py script

                # Saving configurations to a ResultatScript.conf file
                fichConf.write("L'interface " + carte["name"] + " vient d'etre ajoutée avec l'adresse : " + carte["adresse"] + "\n")

            if os.path.exists("/etc/NetworkManager/"):

                # Starting NetworkManager
                os.system("service NetworkManager start")
                print("Redémarrage du service réseau...")
                time.sleep(10)
            else:

                # Starting network service
                os.system("service network start")
                print("Redémarrage du service réseau...")
                time.sleep(10)

        # OpenSuse
        elif os.path.exists("/etc/sysconfig/network/"):
    
            # Stopping network service
            os.system("service network stop")
            print("Arret du service réseau...")
            time.sleep(5)

            # Interface configuration loop
            for card in configE:
                carte = configE[card]
                O.carteE(carte)     # Calling the interface configuration function in the OpenSuseScript.py script
                
                # Saving configurations to a ResultatScript.conf file
                fichConf.write("L'interface " + carte["name"] + " vient d'etre ajoutée avec l'adresse : " + carte["adresse"] + "\n")

            # Starting network service
            os.system("service network start")
            print("Redémarrage du service réseau...")
            time.sleep(10)

        # Linux distribution not supported
        else:
            print("Systeme non pris en charge")

    # Retrieving exceptions
    except Exception as e:
        print("Problème script ajout carte plus à jour")
        print(e)
    
    # If the script is executed correctly
    else:
        print("Création des interfaces OK!")


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
            fichierDHCP.write("default-lease-time " + default_lease + ";" + "\n")
            fichierDHCP.write("max-lease-time " + max_lease + ";" + "\n \n \n")
            fichierDHCP.write("# config des étendues DHCP\n")
        else:
            fichierDHCP = open("/etc/dhcp/dhcpd.conf", "w")
            fichierDHCP.write("# durée des baux dhcp\n")
            fichierDHCP.write("default-lease-time " + default_lease + ";" + "\n")
            fichierDHCP.write("max-lease-time " + max_lease + ";" + "\n \n \n")
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

    except Exception as e:
        print("Problème creation dhcp")
        print(e)

    else:
        print("Configuration du DHCP OK!")


# VLAN configuration function with ConfigVLAN.yaml file
def ajoutVLAN():

    try:

################### Linux distribution detection ###################
        
        # Netplan (Ubuntu 16.04 and later)
        if os.path.exists("/etc/netplan/"):
    
            # Opening the Netplan configuration file
            fichier = open("/etc/netplan/50-cloud-init.yaml", "a")
            fichier.write("\n  vlans:\n")

            # VLAN configuration loop
            for vlan_inf in configV:
                vlan = configV[vlan_inf]
                N.vlan(vlan, fichier)       # Calling the vlans configuration function in the NetplanScript.py script
                
                # Display of the configured vlan
                print("Création du VLAN " + vlan["device"] + " " + vlan["adresse"])
                
                # Saving configurations to a ResultatScript.conf file
                fichConf.write("Création du VLAN " + vlan["device"] + " " + vlan["adresse"] + "\n")
    
            # Application of changes
            os.system("netplan apply")
            print("Redémarrage du service réseau...")
            time.sleep(10)

        # Debian-based
        elif os.path.exists("/etc/network/") and not os.path.exists("/etc/netplan/"):
    
            # Stopping network service
            os.system("service networking stop")
            print("Arret du service réseau...")
            time.sleep(5)

            # Opening interfaces configuration file
            fichier = open("/etc/network/interfaces", "a")
            fichier.write("\n \n")
            fichier.write("\n# declaration des vlans \n")

            # VLAN configuration loop
            for vlan_inf in configV:
                vlan = configV[vlan_inf]
                D.vlan(vlan, fichier)       # Calling the vlans configuration function in the DebianScript.py script
                
                # Display of the configured VLAN
                print("Création du VLAN " + vlan["device"] + " " + vlan["adresse"])
                
                # Saving configurations to a ResultatScript.conf file
                fichConf.write("Création du VLAN " + vlan["device"] + " " + vlan["adresse"] + "\n")

            # Starting network service
            os.system("service networking start")
            print("Redémarrage du service réseau...")
            time.sleep(10)

        # Red-Hat-based
        elif os.path.exists("/etc/sysconfig/network-scripts/"):
            if os.path.exists("/etc/NetworkManager/"):      # Fedora
                
                # Stopping NetworkManager
                os.system("service NetworkManager stop")
                print("Arret du service réseau...")
                time.sleep(5)
            else:
                
                # Stopping network service
                os.system("service network stop")
                print("Arret du service réseau...")
                time.sleep(5)

            # VLAN configuration loop
            for vlan_inf in configV:
                vlan = configV[vlan_inf]
                R.vlan(vlan)        # Calling the vlans configuration function in the RedHatScript.py script
                
                # Saving configurations to a ResultatScript.conf file
                fichConf.write("Création du VLAN " + vlan["device"] + " " + vlan["adresse"] + "\n")

            if os.path.exists("/etc/NetworkManager/"):
                
                # Starting NetworkManager
                os.system("service NetworkManager start")
                print("Redémarrage du service réseau...")
                time.sleep(10)
            else:
                
                # Starting network service
                os.system("service network start")
                print("Redémarrage du service réseau...")
                time.sleep(10)

        # OpenSuse
        elif os.path.exists("/etc/sysconfig/network/"):
    
            # Stopping network service
            os.system("service network stop")
            print("Arret du service réseau...")
            time.sleep(5)

            # VLAN configuration loop
            for vlan_inf in configV:
                vlan = configV[vlan_inf]
                O.vlan(vlan)        # Calling the vlans configuration function in the OpenSuseScript.py script
                
                # Saving configurations to a ResultatScript.conf file
                fichConf.write("Création du VLAN " + vlan["device"] + " " + vlan["adresse"] + "\n")

            # Starting network service
            os.system("service network start")
            print("Redémarrage du service réseau...")
            time.sleep(10)

        # Linux distribution not supported
        else:
            print("Systeme non pris en charge")

    # Catching exceptions
    except Exception as e:
        print("Probleme script vlan")
        print(e)

    # If the script is executed correctly
    else:
        print("Création des VLANs OK!")
        

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

    fichConf.write("\n \n \n")


# Calling the main function
main()