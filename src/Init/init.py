import os
from src.SSH.ssh import ssh_connection_attempt
from src.SSH.ssh import connexion
from src.Env.env import update_env_file
from src.Loading.loading import TermLoading
import re
import paramiko
import sys
from dotenv import load_dotenv
import time

def choice():
    if len(sys.argv) != 2:
        print("Usage: python main.py <remote|local>")
        sys.exit(1)

    user_choice = sys.argv[1]

    if user_choice.lower() == 'remote':
        print("Running the script remotely...")
        return True
    elif user_choice.lower() == 'local':
        print("Running the script locally...")
        return False
    else:
        print("Invalid choice. Please type 'remote' or 'local'.")
        sys.exit(1)

def initialisation(is_remote):
    load_dotenv()
    credentials = {
        'hostname': os.getenv('HOST'),
        'username': os.getenv('USER'),
        'password': os.getenv('PASSWORD')
    }
    if is_remote:
        # update_env_file()
        animation = TermLoading()
        animation.show('Connexion Attempt...', finish_message=f'Connected to {credentials["hostname"]} as {credentials["username"]} ✅', failed_message=f'Failed to Connect to {credentials["hostname"]} as {credentials["username"]}❌😨😨')
        time.sleep(1)
        try:
            initialisation_remote(credentials)
            animation.finished = True
        except Exception as e:
            animation.failed = True
            print(f"Error during remote initialization: {e}")
    else:
        initialisation_local()
        print("No additional setup required for local execution.")


def initialisation_remote(credentials):
    ssh_client = ssh_connection_attempt()
    connexion(credentials['hostname'], credentials['username'], credentials['password'], ssh_client)


def initialisation_local():
    print('local')
