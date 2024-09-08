# Enhanced Email Slicer Program

def email_slicer(email):
    # Check if the email contains exactly one '@'
    if email.count('@') != 1:
        return "Invalid email address. It should contain exactly one '@'."
    
    # Split the email address into username and domain
    try:
        username, domain = email.split('@')
    except ValueError:
        return "Error splitting the username and domain."

    # Check if username or domain is empty
    if not username or not domain:
        return "Invalid email address. Username or domain cannot be empty."

    # Check if domain contains a dot ('.')
    if '.' not in domain:
        return "Invalid domain. Domain should contain a '.'"

    # Split the domain into domain name and extension
    try:
        domain_name, extension = domain.rsplit('.', 1)
    except ValueError:
        return "Error splitting the domain name and extension."

    # Check if domain name or extension is empty
    if not domain_name or not extension:
        return "Invalid domain. Domain name or extension cannot be empty."

    return f"Username: {username}\nDomain Name: {domain_name}\nExtension: {extension}"

# Input email from user
email = input("Enter your email address: ").strip()

# Call the email slicer function and display the results
result = email_slicer(email)
print(result)

