#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import yaml

#suppression des fichiers de conf de base
#os.system("rm -r /etc/sysconfig/network/network-scripts/ifcfg-*")

config = yaml.load(open("Config.yaml"))
carte={}

print(config)

#boucle permettant de liste et traiter les cartes une a une
for card in config:
    carte = config[card]
    print(carte)