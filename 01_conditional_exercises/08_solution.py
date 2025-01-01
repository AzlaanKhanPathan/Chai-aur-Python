password = "12345678910"
password_length = len(password)

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else: 
    strength = "Strong"

print("Password strength is: ", strength)