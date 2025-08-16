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

