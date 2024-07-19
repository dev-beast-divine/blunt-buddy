from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_text():
    prompt = request.json.get('prompt', '')
    result = subprocess.run(['ollama', 'run', 'dolphin-llama3:8b', '--prompt', prompt], capture_output=True, text=True)
    return jsonify({'response': result.stdout})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
