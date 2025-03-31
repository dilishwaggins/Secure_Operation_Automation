# Secure Operations Automation

## Overview
Secure Operations Automation is a Python-based security tool that helps automate common security tasks, making security operations more efficient and reliable. It includes:

- **Password Strength Checker** – Analyzes password strength and suggests improvements.
- **SSH Key Generator** – Generates secure SSH key pairs for authentication.
- **Report Emailer** – Sends security reports via email.

This tool is designed for SOC analysts, IT administrators, and security professionals who want to streamline security-related tasks.

## Features
### 1. Password Strength Checker
- Evaluates password strength based on length, complexity, and character variety.
- Provides recommendations to improve password security.
- Can hash passwords using bcrypt for secure storage.

### 2. SSH Key Generator
- Generates secure RSA or Ed25519 SSH key pairs.
- Saves private and public keys for secure authentication.
- Helps improve SSH-based security for remote access.

### 3. Report Emailer
- Sends security reports via email.
- Uses SMTP authentication to ensure secure email transmission.
- Allows users to specify sender, recipient, and SMTP server details.

## Installation
### Prerequisites
Ensure you have Python installed (Python 3.8 or later is recommended). You will also need to install the required dependencies.

### Install Dependencies
Run the following command to install necessary Python libraries:
```sh
pip install -r requirements.txt
```

## Usage
Run the main script with the appropriate command-line arguments to execute different modules:

### Check Password Strength
```sh
python main.py -p
```

### Generate SSH Keys
```sh
python main.py -s
```

### Send a Security Report via Email
```sh
python main.py -e
```

## File Structure
```
Secure-Operations-Automation/
│── modules/
│   ├── password_strength_checker.py
│   ├── ssh_key_generator.py
│   ├── report_emailer.py
│── main.py
│── README.md
│── requirements.txt
```

## Configuration
### Setting Up Email for Report Emailer
To use the email module, update the `report_emailer.py` file with SMTP server details, or modify `main.py` to input them dynamically.

## Real-World Applications
- **System Administrators:** Automate security tasks like password checks and SSH key generation.
- **SOC Analysts:** Streamline security workflows by integrating security automation.
- **DevOps Teams:** Improve security best practices in development environments.

## Contributing
If you’d like to contribute, feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For inquiries or support, reach out to me joy.zawadi32@gmail.com.

