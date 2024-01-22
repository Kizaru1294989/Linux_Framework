#!/bin/bash
network_interface=$(ip route | grep default | awk '{print $5}')
ip_info=$(ip -4 -o addr show dev "$network_interface" | awk '$3 == "inet" {print $4}')
gateway=$(ip route | grep default | awk '{print $3}')
ip_with_mask="$ip_info"

echo -e "auto lo\niface lo inet loopback\n" > /etc/network/interfaces
echo -e "auto $network_interface\niface $network_interface inet static\n\taddress $ip_with_mask\n\tgateway $gateway" >> /etc/network/interfaces
echo "
███████ ██    ██  ██████  ██████ ███████ ███████ ███████ 
██      ██    ██ ██      ██      ██      ██      ██      
███████ ██    ██ ██      ██      █████   ███████ ███████ 
     ██ ██    ██ ██      ██      ██           ██      ██ 
███████  ██████   ██████  ██████ ███████ ███████ ███████                                                   
"
echo "Votre machine possède désormais une adresse IP statique avec ces caractéristiques : "
echo "Carte réseau : $network_interface"
echo "Adresse IP avec masque : $ip_with_mask"
echo "Passerelle (Gateway) : $gateway"
/etc/init.d/networking restart
echo "Reboot of the machine"
reboot