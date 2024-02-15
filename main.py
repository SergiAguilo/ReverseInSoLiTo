from flask import Flask, request, jsonify
import argparse
import sqlite3
from databaseSearch import databaseSearch, returnTools

# Argument parser
parser = argparse.ArgumentParser(description='Creates a network of co-occurrences found in PubMed Articles from tools stored in OpenEBench (OEB)')

parser.add_argument("-d", "--database", help="Required. Database Name where the data will be stored. Not possible to update the database. It should have '.db' sufix",
required=True)

args = parser.parse_args()

# Name of the database
DB_FILE = args.database

# Connect to the SQLite database
# If name not found, it will create a new database
conn = sqlite3.connect(DB_FILE, check_same_thread=False)
c = conn.cursor()




app = Flask(__name__)

@app.route('/search')
def search():
    search_terms = request.args.getlist('tool')
    results = databaseSearch(c, search_terms)

    return jsonify(results)

@app.route('/listTools')
def listTools():
    limit = request.args.getlist('limit')
    skip = request.args.getlist('skip')
    if not limit:
        limit = [10]
    if not skip:
        skip = [0]
    print(limit, skip)
    results = returnTools(c, limit[0], skip[0])

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)