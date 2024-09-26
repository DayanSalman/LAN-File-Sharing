from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from flask_httpauth import HTTPBasicAuth
import os

app = Flask(__name__)
auth = HTTPBasicAuth()

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
CODE_SNIPPETS = []  # List to store code snippets

# Create the uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Sample user data (In production, use a secure method to store user credentials)
users = {
    "admin": "password"  # Change this to your desired username and password
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

@app.route('/')
@auth.login_required
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files, code_snippets=CODE_SNIPPETS)

@app.route('/upload', methods=['POST'])
@auth.login_required
def upload_file():
    file = request.files['file']
    if file:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return redirect(url_for('index'))

@app.route('/download/<filename>')
@auth.login_required
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@app.route('/save_code', methods=['POST'])
@auth.login_required
def save_code():
    code_snippet = request.form.get('code')  # Get the code snippet from the form
    if code_snippet:
        CODE_SNIPPETS.append(code_snippet)  # Save code snippet to the list
    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
@auth.login_required
def clear_files():
    files = os.listdir(UPLOAD_FOLDER)
    for file in files:
        os.remove(os.path.join(UPLOAD_FOLDER, file))
    return redirect(url_for('index'))

@app.route('/clear_codes', methods=['POST'])
@auth.login_required
def clear_codes():
    CODE_SNIPPETS.clear()  # Clear the list of code snippets
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
