import random
import hashlib

def generate_password(length=8):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?`~"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def encrypt_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def save_passwords_to_file(filename, passwords):
    with open(filename, "w") as file:
        for password in passwords:
            file.write(password + "\n")

def generate_encrypted_passwords(num_passwords, length=8):
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length)
        encrypted_password = encrypt_password(password)
        passwords.append(encrypted_password)
    return passwords

def generate_text(length=10):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?`~"
    text = ''.join(random.choice(characters) for _ in range(length))
    return text

def save_text_to_file(filename, text):
    with open(filename, "w") as file:
        file.write(text)

user_choice = input("O que você deseja gerar? Digite 'senha' para gerar senhas criptografadas ou 'texto' para gerar um texto aleatório: ")

if user_choice == "senha":
    num_passwords = int(input("Quantas senhas criptografadas você deseja gerar? "))
    filename = r"C:\Users\use\Desktop\senhas_criptografadas.txt"

    passwords = generate_encrypted_passwords(num_passwords)

    print("As senhas estão sendo geradas. Aguarde...")
    print("Senhas geradas:")
    for password in passwords:
        print(password)

    save_passwords_to_file(filename, passwords)

    print(f"As senhas criptografadas foram geradas e salvas no arquivo '{filename}'.")
elif user_choice == "texto":
    text_length = int(input("Qual o tamanho do texto aleatório que você deseja gerar? "))
    filename = r"C:\Users\use\Desktop\texto_aleatorio.txt"

    generated_text = generate_text(text_length)

    print("O texto aleatório está sendo gerado. Aguarde...")
    print("Texto gerado:")
    print(generated_text)

    save_text_to_file(filename, generated_text)

    print(f"O texto aleatório foi gerado e salvo no arquivo '{filename}'.")
