from flask import Flask, render_template
import random
import string

app = Flask(__name__)

def generate_secret_key(length=50):
    characters = string.ascii_letters + string.digits + string.punctuation
    secret_key = ''.join(random.choice(characters) for _ in range(length))
    return secret_key

@app.route('/')
def index():
    secret_key = generate_secret_key()
    return render_template('index.html', secret_key=secret_key)

if __name__ == '__main__':
    app.run(debug=True)

