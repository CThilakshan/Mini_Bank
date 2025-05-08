import hashlib

password = input("Password: ")
password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
print(f"Password Hash: {password_hash}")
