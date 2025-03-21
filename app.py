from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

# Store running Streamlit process
current_process = None
current_module = None


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/start_streamlit/<module>')
def start_streamlit(module):
    global current_process, current_module

    module_paths = {
        "codereview": "codereview.py",
        "resumereview": "resumereview/main.py"
    }

    if module not in module_paths:
        return jsonify({'error': 'Invalid module'}), 400

    # Stop any currently running module before starting a new one
    if current_process and current_process.poll() is None:
        current_process.terminate()
        current_process = None
        current_module = None  # Reset module name

    # Start Streamlit only for the selected module
    current_process = subprocess.Popen(['streamlit', 'run', module_paths[module]], shell=False)
    current_module = module

    return jsonify({'status': f'{module} Streamlit app started'})


@app.route('/stop_streamlit')
def stop_streamlit():
    global current_process, current_module

    if current_process and current_process.poll() is None:
        current_process.terminate()
        current_process = None
        current_module = None
        return jsonify({'status': 'Streamlit app stopped'})

    return jsonify({'error': 'No module is running'}), 400


if __name__ == '__main__':
    app.run(debug=True)
