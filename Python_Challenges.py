# Python Challenges
# 1. Check if a user's name is not empty and the age is greater than or equal to 18

# 2. Check if the password is at least 8 characters long and does not contain spaces

# 3. Check if a user’s email is not empty, contains '@', and ends with '.com'

# 4. Check if a username is a string, is not None, and is longer than 5 characters

# 5. Check if the user is either an admin or a moderator,
#     and either they’re not banned or they’ve verified their email

# Problem 1
user_name = "Aatif"
age = 19
print(len(user_name)>0 and age >= 18 )

# Problem 2

Password ="@Mr_Aatif"

print( len(Password) >= 8 and " " not in Password )

# Problem 3

Email = input("Enter Your Email i'd")
print(len(Email) > 0 and "@" in Email and Email.endswith(".com"))


# Problem 4

Username = input("Enter Your Username: ")
print(isinstance(Username, str) and len(Username) > 5)


# Problem 5

role = "admin"       # can be "admin", "moderator", "user"
banned = False
verified_email = True

print((role == "admin" or role == "moderator") and (not banned or verified_email))
