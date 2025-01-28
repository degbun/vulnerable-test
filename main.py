import os
import hashlib
import sqlite3
import subprocess

# 1. Utilisation de mot de passe en clair (vulnérabilité de sécurité)
def get_password():
    password = "password123"  # Utilisation d'un mot de passe en clair
    return password

# 2. Injections SQL (vulnérabilité SQLi)
def fetch_data_from_db(user_input):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input}'"  # Injection SQL
    cursor.execute(query)
    return cursor.fetchall()

# 3. Utilisation de subprocess sans gestion d'entrée (vulnérabilité de commande externe)
def run_command():
    command = "ls"
    subprocess.run(command, shell=True)  # Vulnérabilité si un utilisateur malveillant fournit des entrées

# 4. Exposition d'informations sensibles (vulnérabilité de fuite d'informations)
def save_sensitive_info():
    secret_key = "my_secret_key"  # Exposition de données sensibles dans le code
    with open("secret.txt", "w") as f:
        f.write(secret_key)

# 5. Utilisation de hashage faible (vulnérabilité de sécurité)
def hash_password(password):
    # Utilisation de MD5 qui est un algorithme de hashage faible
    return hashlib.md5(password.encode()).hexdigest()  # MD5 est obsolète et vulnérable

# Exemple d'utilisation de ces vulnérabilités
def main():
    password = get_password()  # Vulnérabilité de mot de passe en clair
    print(f"Password: {password}")
    
    user_input = "' OR 1=1 --"  # Tentative d'injection SQL
    data = fetch_data_from_db(user_input)
    print(f"Data: {data}")
    
    run_command()  # Vulnérabilité de commande externe
    
    save_sensitive_info()  # Vulnérabilité d'exposition d'informations sensibles
    
    hashed_password = hash_password(password)  # Vulnérabilité de hashage faible
    print(f"Hashed password: {hashed_password}")

if __name__ == "__main__":
    main()
