import random
import string

def generate_secret_key(length=50):
    characters = string.ascii_letters + string.digits + string.punctuation
    secret_key = ''.join(random.choice(characters) for _ in range(length))
    return secret_key

# Generate a secret key with the default length of 50 characters
secret_key = generate_secret_key()
print("Generated Secret Key:", secret_key)

