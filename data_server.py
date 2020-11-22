from flask import Flask, request, send_file, abort
import subprocess
from data_tools import *

BASE_DIR = os.getcwd()


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    output = f"<h1>home data directory</h1>"
    output += str(ulify([make_url(request.base_url, f) for f in get_contents(os.getcwd())]))  # str(get_hierarchy(os.getcwd()))
    return output

@app.route('/', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def dir_listing(req_path):
    # https://stackoverflow.com/questions/23718236/python-flask-browsing-through-directory-with-files

    # Joining the base and the requested path
    abs_path = os.path.join(BASE_DIR, req_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_file(abs_path)

    # Show directory contents
    output = f"<h1>{req_path}</h1>"
    output += str(ulify([make_url(request.base_url, f) for f in get_contents(abs_path)]))
    return output  # render_template('files.html', files=files)

@app.route('/SQL', defaults={'query': ''}, methods=['GET'])
def sql(query=''):
    if 'query' in request.args:
        query = str(request.args['query'])
    else:
        return "Error: No query provided. Please specify a SQL Query."
    
    # Example "csvsql --query \"select Open from 'AAPL' where Open > 400\" Marketdata/YahooFinance/AAPL.csv"
    data = subprocess.check_output(f"csvsql --query {query}", shell=True)

    return data


app.run()