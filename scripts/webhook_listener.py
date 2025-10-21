from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    if data and 'alerts' in data:
        os.system("ansible-playbook ansible/playbook.yml -i ansible/inventory")
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
