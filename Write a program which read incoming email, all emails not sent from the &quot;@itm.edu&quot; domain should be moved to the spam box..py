import imaplib
import email
from email.header import decode_header

# Login to the email server
username = 'your_email@gmail.com'
password = 'your_password'
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username, password)

# Select the inbox
mail.select("inbox")

# Search for all emails in the inbox
status, messages = mail.search(None, "ALL")
email_ids = messages[0].split()

# Iterate through each email
for e_id in email_ids:
    status, msg_data = mail.fetch(e_id, "(RFC822)")
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            from_ = msg.get("From")
            # Check if the email is not from the '@itm.edu' domain
            if "@itm.edu" not in from_:
                # Move email to spam
                mail.store(e_id, '+X-GM-LABELS', '\\Spam')
                print(f"Moved email from {from_} to spam")

# Logout from the email server
mail.logout()

