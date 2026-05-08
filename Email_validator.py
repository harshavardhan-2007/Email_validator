import re

def is_valid_email(email):
    # basic pattern for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# User input
email = input("Enter your email: ")

# Check and print result
if is_valid_email(email):
    print("Valid email address ✅")
else:
    print("Invalid email address ❌")