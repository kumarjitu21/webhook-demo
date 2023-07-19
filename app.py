from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data.get('event') == 'push':
        subprocess.run(['sh', 'hello-world.sh'])  # Replace with your actual script path
        return jsonify({"message": "Script executed successfully!"}), 200
    else:
        return jsonify({"message": "No action required."}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
