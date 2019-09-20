from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "Hello world!\n"

@app.route("/rotem")
def hello_rotem():
    return "Hello Rotem!\n"

if __name__ == "__main__":
    app.run()