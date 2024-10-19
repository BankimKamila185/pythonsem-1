def split_email(email):
    # Step 1: Using the split method to separate the email
    username, domain = email.split("@")
    
    # Step 2: Return or print the results
    return username, domain

# Example usage
email = "Bankimkamila923@gmail.com"
username, domain = split_email(email)
print("Username:", username)  # Output: Username: exampleuser
print("Domain:", domain)      # Output: Domain: gmail.com