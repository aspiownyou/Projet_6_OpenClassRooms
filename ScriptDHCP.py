def configDHCP(dhcp, fichier):
    
    fichier.write("subnet " + dhcp["subnet"] + " netmask " + dhcp["netmask"] + "{\n")
    fichier.write("  range " + dhcp["range_start"] + " " + dhcp["range_end"] + ";\n")
    fichier.write("  option broadcast-address " + dhcp["broadcast"] + ";\n")
    fichier.write("  option router " + dhcp["router"] + ";\n")
    
    if dhcp["dns"] != '':
        fichier.write("  option domain-name-server " + dhcp["dns"] + ";\n")
    elif dhcp["domain"] != '':
        fichier.write("  option domain-name " + dhcp["domain"] + ";\n")
    elif dhcp["ntp"] != '':
        fichier.write("  option ntp-servers " + dhcp["ntp"] + ";\n")

    fichier.write("}")