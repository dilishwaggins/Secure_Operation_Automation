import smtplib
import ssl
from email.message import EmailMessage

def send_email(sender_email, sender_password, recipient_email, subject, body):
    print("[+] Preparing email...")
    
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email
    
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("[+] Email sent successfully!")
    except Exception as e:
        print(f"[!] Failed to send email: {e}")

def run():
    sender_email = input("Enter your email: ").strip()
    sender_password = input("Enter your email password (App Password recommended): ").strip()
    recipient_email = input("Enter recipient email: ").strip()
    subject = input("Enter email subject: ").strip()
    body = input("Enter email body: ").strip()
    
    send_email(sender_email, sender_password, recipient_email, subject, body)

if __name__ == "__main__":
    run()
