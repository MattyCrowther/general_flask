import os
from flask import Flask
from flask import render_template

root_dir = "app"
static_dir = os.path.join(root_dir, "assets")
template_dir = os.path.join(root_dir, "templates")
sessions_dir = os.path.join(root_dir, "sessions")
truth_save_dir = os.path.join(root_dir, "truth_saves")
example_dir = os.path.join(static_dir, "examples")
example_file = os.path.join(static_dir, "examples","explanation.json")
user_gns = "graph_names.json"

server = Flask(__name__, static_folder=static_dir,
               template_folder=template_dir)

server.config['SESSION_PERMANENT'] = True
server.config['SESSION_TYPE'] = 'filesystem'
server.config['SESSION_FILE_THRESHOLD'] = 100
server.config['SECRET_KEY'] = "Secret"
server.config['SESSION_FILE_DIR'] = os.path.join(root_dir, "flask_sessions")

@server.route('/', methods=['GET', 'POST'])
@server.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
