import os
from dotenv import load_dotenv

def update_env_file():
    load_dotenv()
    host = input("Entrez la nouvelle valeur pour 'host': ")
    user = input("Entrez la nouvelle valeur pour 'user': ")
    password = input("Entrez la nouvelle valeur pour 'password': ")
    os.environ['HOST'] = host if host else os.getenv('HOST', '')
    os.environ['USER'] = user if user else os.getenv('USER', '')
    os.environ['PASSWORD'] = password if password else os.getenv('PASSWORD', '')
    env_file_path = "../.env"
    with open(env_file_path, "w") as f:
        f.write(f"HOST={os.environ['HOST']}\nUSER={os.environ['USER']}\nPASSWORD={os.environ['PASSWORD']}\n")

    print(f"Fichier {env_file_path} mis à jour avec succès.")

if __name__ == "__main__":
    update_env_file()
