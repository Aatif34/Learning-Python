# Python Challenges
# Problem 1

# Validate the Quality and Correctness of Email Values
#  Can you write a Python program that checks if an email:
# Is not empty?
# Contains both . and @?
# Contains exactly one @ symbol?
# Ends with .com, .org, or .net?
# Is not longer than 254 characters?
# Starts and ends with a letter or digit?

email = input("Enter Your Email ID: ").strip()

if (
    email != ""
    and "." in email
    and "@" in email
    and email.count("@") == 1
    and email.endswith((".com", ".org", ".net"))
    and len(email) <= 254
    and email[0].isalnum()
    and email[-1].isalnum()
):
    print("Your Email ID is correct ")
else:
    print("Your Email ID is not correct , please re-enter")


# Other Method

email = input("Enter Your Email ID: ").strip()

if email == "":
    print(" Email cannot be empty")
elif " " in email:
    print(" Email cannot contain spaces")
elif "." not in email or "@" not in email:
    print(" Email must contain '.' and '@'")
elif email.count("@") != 1:
    print(" Email must contain exactly one '@'")
elif not email.endswith((".com", ".org", ".net")):
    print(" Email must end with .com, .org, or .net")
elif len(email) > 254:
    print(" Email must be 254 characters or fewer")
elif not (email[0].isalnum() and email[-1].isalnum()):
    print(" Email must start and end with a letter or digit")
else:
    print(" Your Email ID is correct")


# Problem 2

# Validate the Quality and Correctness of Passwords
# Must not be empty
# Must be at least 8 characters
# Must include at least 1 uppercase
# Must include at least 1 lowercase
# Must not be same as the email
# Must not contain any spaces
# Must start and end with a letter or digit


email = input("Enter your Email ID: ").strip()
password = input("Enter Password: ").strip()

if password == "":
    print(" Password cannot be empty")
elif len(password) < 8:
    print(" Password must be at least 8 characters")
elif not any(ch.isupper() for ch in password):
    print(" Password must include at least 1 uppercase letter")
elif not any(ch.islower() for ch in password):
    print(" Password must include at least 1 lowercase letter")
elif password == email:
    print(" Password cannot be the same as Email")
elif " " in password:
    print(" Password must not contain spaces")
elif not (password[0].isalnum() and password[-1].isalnum()):
    print(" Password must start and end with a letter or digit")
else:
    print(" Your Password is correct")
