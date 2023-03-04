from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def send_to_discord():
    if request.method == 'POST':
        name = "Gotcha!"
        link = request.form['link']


        data = {'Name': name, 'content': link}
        headers = {'Content-type': 'application/json'}
        response = requests.post('https://discord.com/api/webhooks/1081433957243035728/Oeu6e96b1Ivb4JC-bQLDPjV7Oytnn3GbhGexKxTEEeR4QIPaI4rd00FIbKz6gqnkIxFX', json=data, headers=headers)
        if response.ok:
            return 'Message sent to Discord.'
        else:
            return 'Error sending message to Discord.'
    else:
        return 'Hello, world!'

if __name__ == '__main__':
    app.run()
