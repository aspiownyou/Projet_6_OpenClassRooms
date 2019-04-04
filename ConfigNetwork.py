import os
import sys
import time
import datetime

# Creating the configuration file
repUser = "/tmp/ResultatScript.conf"

# Retrieving date and time
date = datetime.datetime.now()

# Opening and registering the date and time in the new file
fichConf = open(repUser, "a")
fichConf.write(str(date) + "\n")

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
        creationInterface(fichConf)
        print("Vous pourrez trouver les modifications effectué dans le fichier : " + repUser)

    elif argument == 'D' or argument == 'd':
        creationDHCP(fichConf)
        print("Vous pourrez trouver les modifications effectué dans le fichier : " + repUser)
    elif argument == 'V' or argument == 'v':
        ajoutVLAN(fichConf)
        print("Vous pourrez trouver les modifications effectué dans le fichier : " + repUser)
    else:
        print("Il faut un argument pour appeller le script :\n")
        print("\n        E ou e  creation d'interface(s) réseau")
        print("\n        D ou d  configuraiton d'un serveur dhcp")
        print("\n        V ou v  configuration des vlan")

    fichConf.write("\n \n \n")


# Calling the main function
main()