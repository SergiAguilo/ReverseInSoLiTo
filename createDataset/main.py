# Libraries
import sqlite3
import time
import argparse
import json

# Import functions
from CreateTables import createSQLTables
from searchToolsInOEB import searchTools
from findCitationsPubMed import findCitations
from cleanCitations import cleanPublicationsCitations

# Start time - Just to count how much the script lasts
start_time = time.time()

# Argument parser
parser = argparse.ArgumentParser(description='Creates a network of co-occurrences found in PubMed Articles from tools stored in OpenEBench (OEB)')

parser.add_argument("-d", "--database", help="Required. Database Name where the data will be stored. Not possible to update the database. It should have '.db' sufix",
required=True)

parser.add_argument("-i", "--input", help="Required. Path of the folder where the OEB tools information file is located",
required=True)

parser.add_argument("-a", "--api_key", help="No required. API key from PubMed to retrieve the publications with few restrictions. Default is None",
required=False)

args = parser.parse_args()

# Name of the database
DB_FILE = args.database

# Connect to the SQLite database
# If name not found, it will create a new database
conn = sqlite3.connect(DB_FILE)
c = conn.cursor()

api_key = None
if args.api_key:
    api_key = args.api_key

# Load the input file
with open(args.input, 'r') as json_file:
    json_data = json.load(json_file)

def main():
    print("Creating Table")
    createSQLTables(c)
    print("Parsing tools in OpenEBench")
    searchTools(c, json_data)
    conn.commit()
    print("Find citations in PubMed")
    findCitations(c, conn, api_key)
    print("Clean unused citations and publications to have an smaller dataset")
    cleanPublicationsCitations(c, conn)

if __name__=='__main__':
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    c.close()
