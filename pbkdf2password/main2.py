from django.contrib.auth.hashers import PBKDF2PasswordHasher

hasher = PBKDF2PasswordHasher()

print(hasher.encode(password='password', salt='ZRz2H4NkDZVr5kz8abSQV9', iterations=390000))
print(hasher.verify(password='password', encoded=hasher.encode(password='password', salt='ZRz2H4NkDZVr5kz8abSQV9', iterations=390000)))
