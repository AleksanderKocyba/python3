from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    number = random.randint(1, 100)
    return f"""
    <html>
    <head>
        <title>Losowa liczba</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; padding: 50px; }}
            h1 {{ font-size: 2em; font-weight: bold; color: pink; }}
            button {{ padding: 10px 20px; font-size: 1.2em; background-color: pink; border: none; cursor: pointer; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1>Wylosowana liczba: {number}</h1>
        <form action="/" method="get">
            <button type="submit">Wygeneruj ponownie</button>
        </form>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
