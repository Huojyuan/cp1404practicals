"""
Email to Name Storage Program
Estimated time: 25 minutes
Actual time: 22 minutes

This program stores users' emails (keys) and names (values) in a dictionary.
It extracts a default name from the email and asks the user to confirm or edit it.
At the end, it prints all stored names and emails in a readable format.
"""

def extract_name_from_email(email):
    """Extract a name from the email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = ' '.join(parts).title()
    return name


def main():
    email_to_name = {}

    while True:
        email = input("Email: ").strip()
        if email == "":
            break

        default_name = extract_name_from_email(email)
        response = input(f"Is your name {default_name}? (Y/n) ").strip().lower()

        if response not in ('', 'y', 'yes'):
            name = input("Name: ").strip()
        else:
            name = default_name

        email_to_name[email] = name

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
