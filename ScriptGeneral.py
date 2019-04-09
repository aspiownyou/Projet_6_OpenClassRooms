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
dhcpGlobal = yaml.safe_load(open("ConfigDHCP_global.yaml"))

# Creating empty dictionaries for YAML data retrieval
carte={}
dhcp={}
vlan={}

# definition of variables for the DHCP part
max_lease = dhcpGlobal["Globale"]["lease_max"]
default_lease = dhcpGlobal["Globale"]["lease"]
iDHCPName = dhcpGlobal["Globale"]["interfaces"]


# Function of creating network interfaces according to the contents of the Config.yaml file
def creationInterface(fichConf):
    
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

        # Debian-based
        elif os.path.exists("/etc/network/") and not os.path.exists("/etc/netplan/"):

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

        # Red-Hat-based
        elif os.path.exists("/etc/sysconfig/network-scripts/"):

            # Interface configuration loop
            for card in configE:
                carte = configE[card]
                R.carteE(carte)    # Calling the interface configuration function in the RedHatScript.py script

                # Saving configurations to a ResultatScript.conf file
                fichConf.write("L'interface " + carte["name"] + " vient d'etre ajoutée avec l'adresse : " + carte["adresse"] + "\n")

        # OpenSuse
        elif os.path.exists("/etc/sysconfig/network/"):

            # Interface configuration loop
            for card in configE:
                carte = configE[card]
                O.carteE(carte)     # Calling the interface configuration function in the OpenSuseScript.py script
                
                # Saving configurations to a ResultatScript.conf file
                fichConf.write("L'interface " + carte["name"] + " vient d'etre ajoutée avec l'adresse : " + carte["adresse"] + "\n")

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

def installDHCP():

    # Installing the ISC-DHCP-server package
    if os.path.exists("/etc/yum/"):
        os.system("yum install -y dhcp-server*")
    elif os.path.exists("/etc/apt/"):
        os.system("apt install -y isc-dhcp-server*")
    elif os.path.exists("/etc/zypp/"):
        os.system("zypper install -y dhcp-server*")



# ISC-DHCP Server installation and configuration function
def creationDHCP(fichConf):

    try:
        # 

        #iDHCP = open("/etc/default/isc/dhcp-server")
        #iDHCP.write("# Interface DHCP declaration")
        #iDHCP.write("INTERFACES=\"" + iDHCPName + "\" \n")

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
            print("debian debian debian")

        # DHCP address pool fill loop
        for dhcp_inf in configD:
            dhcp = configD[dhcp_inf]
            sdhcp.configDHCP(dhcp, fichierDHCP)
            print("Configuration du pool dhcp sur le réseau " + dhcp["subnet"])
            fichConf.write("Configuration du pool dhcp sur le réseau " + dhcp["subnet"] + "\n")

    except Exception as e:
        print("Problème creation dhcp")
        print(e)

    else:
        print("Configuration du DHCP OK!")


# VLAN configuration function with ConfigVLAN.yaml file
def ajoutVLAN(fichConf):

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
                fichConf.write("Création du VLAN " + str(vlan["interface"]) + "." + str(vlan["num"]) + " " + vlan["adresse"] + "\n")

        # Debian-based
        elif os.path.exists("/etc/network/") and not os.path.exists("/etc/netplan/"):

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
                fichConf.write("Création du VLAN " + str(vlan["interface"]) + "." + str(vlan["num"]) + " " + vlan["adresse"] + "\n")

        # Red-Hat-based
        elif os.path.exists("/etc/sysconfig/network-scripts/"):

            # VLAN configuration loop
            for vlan_inf in configV:
                vlan = configV[vlan_inf]
                R.vlan(vlan)        # Calling the vlans configuration function in the RedHatScript.py script
                
                # Saving configurations to a ResultatScript.conf file
                fichConf.write("Création du VLAN " + str(vlan["interface"]) + "." + str(vlan["num"]) + " " + vlan["adresse"] + "\n")

        # OpenSuse
        elif os.path.exists("/etc/sysconfig/network/"):

            # Starting wicked network manager
            startWicked()

            # VLAN configuration loop
            for vlan_inf in configV:
                vlan = configV[vlan_inf]
                O.vlan(vlan)        # Calling the vlans configuration function in the OpenSuseScript.py script
                
                # Saving configurations to a ResultatScript.conf file
                fichConf.write("Création du VLAN " + str(vlan["interface"]) + "." + str(vlan["num"]) + " " + vlan["adresse"] + "\n")

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

# Network services restart function        
def redemarrage():
    if os.path.exists("/etc/netplan/"): # Ubuntu / Netplan
        os.system("netplan apply")
    elif os.path.exists("/etc/network/") and not os.path.exists("/etc/netplan/"): # Debian
        os.system("/etc/init.d/networking restart")
    elif os.path.exists("/etc/sysconfig/network-scripts/"):
        if os.path.exists("/etc/NetworkManager/"):      # Fedora
                
            # Restarting NetworkManager
            os.system("service NetworkManager restart")

        else:    # CentOS
                
            # Restarting network service 
            os.system("/etc/init.d/network restart")
    elif os.path.exists("/etc/sysconfig/network/"): # OpenSuse
        os.system("/etc/init.d/network restart")

def restartDHCP():

        # Executing service restart commands and automatic execution at startup
        if os.path.exists("/etc/NetworkManager"):
            os.system("/etc/init.d/dhcpd restart")
            os.system("systemctl enable dhcpd")
        elif os.path.exists("/etc/network/"):
            os.system("/etc/init.d/isc-dhcp-server restart")
            os.system("systemctl enable dhcpd")
        else:
            os.system("/etc/init.d/dhcpd restart")
            os.system("systemctl enable dhcpd")

def startWicked():
    os.system("systemctl disable NetworkManager")
    os.system("systemctl enable wicked.service")
    os.system("service wicked restart")