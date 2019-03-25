# ScriptCarteE
PREREQUIS:
    - python 3.x
    - bibliothèque pyyaml
    - distribution Linux basé sur Red Hat, Debian, Ubuntu ou OpenSuse

MODE D'EMPLOIS:

    lancer ScriptGeneral.py avec les droits root. Le lancement se fait avec une commande de type:

        - python ScriptGeneral.py arg

    Les scripts suivent les informations des fichiers yaml. Vous devez remplir les fichiers (ils possèdent deja tous une config pour vous guider) avec les informations de votre infrastructure. Vous avez la possibilité de faire plus de blocs d'instruction que ceux présents dans les fichiers, les scripts sont capables de gérer la présence d'un nombre aléatoire de blocs d'instructions.

    Pour la création de VLAN et du DHCP, les cartes réseaux doivent être deja configurer pour qu'ils soient effectif.

LISTE DES ARGUMENTS:

    - E : lance les scripts de création d'interface réseau. Créer les fichiers d'interfaces selon le fichier Config.yaml
    - D : lance les scripts de déploiement du DHCP. Installe un serveur DHCP et le configure suivant le fichier ConfigDHCP.yaml
    - V : lance les scripts de création de VLAN. Configure des VLANs selon le fichier ConfigVLAN.yaml
    - R : active le routage sur le serveur.