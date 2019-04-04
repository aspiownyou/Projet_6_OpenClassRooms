# ScriptCarteE
PREREQUIS:
    - python 3.x
    - bibliothèque pyyaml installée (python -m pip isntall pyyaml)
    - distribution Linux basé sur Red Hat, Debian, Ubuntu ou OpenSuse

MODE D'EMPLOIS:

    lancer ConfigNetwork.py avec les droits root. Le lancement se fait avec une commande de type:

        - python ScriptGeneral.py argument

    Les scripts suivent les informations des fichiers yaml. Vous devez donc remplir les fichiers 
    (ils sont deja tous rempli pour vous guider en donnant un exemple) avec les informations de votre infrastructure.
    Vous avez la possibilité de faire plus de blocs d'instruction que ceux présents dans les fichiers, 
    les scripts sont capables de gérer la présence d'un nombre non déterminé de blocs d'instructions.

    Pour la création des intefaces, seul Ethernet est géré, de plus il faut bien pensé à ne mettre qu'une seule
    Gateway. Le lancement de cette partie se fait avec l'arguement E ou e et les informations nécéssaire à la configuration
    sont rangé dans le fichier Config.yaml .

    Pour l'installation et la configuration d'un serveur ISC-DHCP-Server, vous aurez besoin d'une accès internet. Les
    informations nécéssaire au déploiement du dhcp seront stockées dans les fichiers ConfigDHCP_lease.yaml et 
    ConfigDHCP_pools.yaml . Les argments D ou d serviront à lancer cette partie.

    Pour la configuration de VLAN, les interfaces doivent deja être configurées et le script lancé avec les arguments 
    V ou v. Les informations servant à leurs paramétrage seront stocké dans le fichier ConfigVLAN.yaml .

    Pour la création de VLAN et du DHCP, les cartes réseaux doivent être deja configurer pour qu'ils soient effectif.

    Note : Il sera peut etre nécéssaire de relancer les services réseaux, voir redémarer le serveur (Fedora).

LISTE DES ARGUMENTS:

    - E : lance les scripts de création d'interface réseau. Créer les fichiers d'interfaces selon le fichier Config.yaml
    - D : lance les scripts de déploiement du DHCP. Installe un serveur DHCP et le configure suivant le fichier ConfigDHCP.yaml
    - V : lance les scripts de création de VLAN. Configure des VLANs selon le fichier ConfigVLAN.yaml