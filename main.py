import argparse
from modules import password_strength_checker, ssh_key_generator, report_emailer

def main():
    parser = argparse.ArgumentParser(description="Secure Operations Automation Tool")
    parser.add_argument("-p", "--password", help="Check password strength", action="store_true")
    parser.add_argument("-s", "--ssh-key", help="Generate SSH keys", action="store_true")
    parser.add_argument("-e", "--email", help="Send security report via email", action="store_true")
    
    args = parser.parse_args()
    
    if args.password:
        password_strength_checker.run()
    elif args.ssh_key:
        ssh_key_generator.run()
    elif args.email:
        report_emailer.run()
    else:
        print("\nUsage: python main.py -p | -s | -e")
        print("  -p  Check password strength")
        print("  -s  Generate SSH keys")
        print("  -e  Send security report via email")

if __name__ == "__main__":
    main()
