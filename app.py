from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

# This is required for Vercel
if __name__ == '__main__':
    app.run()