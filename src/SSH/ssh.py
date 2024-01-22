import paramiko
import re
import time
import os
import subprocess

#script_IP_path = "../../Fonctions/IP.sh"


def ssh_connection_attempt():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    return ssh_client


def connexion(hostname, username, password, ssh_client):
    try:
        bash_script = open("../../Fonctions/IP.sh").read()
        ssh_client.connect(hostname=hostname, username=username, password=password, timeout=10)
       
        stdin, stdout, stderr = ssh_client.exec_command(bash_script)
        # read the standard output and print it
        print(stdout.read().decode())
        # print errors if there are any
        err = stderr.read().decode()
        if err:
            print(err)
        # close the connection
        ssh_client.close()
        
    except paramiko.AuthenticationException:
        print("Auth Failed")
    except paramiko.SSHException as e:
        print(f"Erreur SSH: {str(e)}")
