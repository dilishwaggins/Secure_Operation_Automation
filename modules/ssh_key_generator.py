import paramiko
import os

def generate_ssh_key(key_name="id_rsa", key_size=2048, save_path="."):
    """
    Generates an SSH key pair and saves them in the specified directory.
    :param key_name: Name for the key files (default: id_rsa)
    :param key_size: Key size in bits (default: 2048)
    :param save_path: Directory where keys will be saved (default: current directory)
    """
    # Ensure save path exists
    os.makedirs(save_path, exist_ok=True)
    
    # Generate RSA Key
    key = paramiko.RSAKey.generate(key_size)
    private_key_path = os.path.join(save_path, key_name)
    public_key_path = f"{private_key_path}.pub"
    
    # Save private key
    with open(private_key_path, "w") as private_key_file:
        key.write_private_key(private_key_file)
    os.chmod(private_key_path, 0o600)  # Secure private key permissions
    
    # Save public key
    with open(public_key_path, "w") as public_key_file:
        public_key_file.write(f"{key.get_name()} {key.get_base64()}")
    
    print(f"SSH Key Pair Generated:")
    print(f"- Private Key: {private_key_path}")
    print(f"- Public Key: {public_key_path}")

def run():
    key_name = input("Enter key name (default: id_rsa): ") or "id_rsa"
    save_path = input("Enter save directory (default: current directory): ") or "."
    
    generate_ssh_key(key_name, save_path=save_path)

if __name__ == "__main__":
    run()
