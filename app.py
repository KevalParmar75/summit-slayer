from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)
streamlit_process = None

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/start_streamlit')
def start_streamlit():
    global streamlit_process
    if streamlit_process is None:
        streamlit_process = subprocess.Popen(['streamlit', 'run', 'resumereview/main.py'], shell=True)
    return jsonify({'status': 'Streamlit app started'})

if __name__ == '__main__':
    app.run(debug=True)
