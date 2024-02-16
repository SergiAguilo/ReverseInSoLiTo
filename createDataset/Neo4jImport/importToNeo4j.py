
# Import libraries
from neo4j import GraphDatabase
import configparser
import sys

config_path = sys.argv[1]


def readIni(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    dict_config = {}
    for section in config.sections():
        for key in config[section]:
            dict_config[key] = config[section][key]
    return dict_config


def createNodes(driver, publicationsFile, toolsFile):
    with driver.session() as session:

        # Create Publication nodes
        # :Publication: Label of the node
        # id: Primary key of publication
        print("Creating Publications nodes")
        session.run("""
                LOAD CSV WITH HEADERS FROM "file:///%s" AS csv
                CREATE (:Publication {pmid:csv.pmid})
                """ % (publicationsFile))
        
        # Index for Publication nodes
        print("Creating Publications index")
        session.run("""
                CREATE INDEX index_publications FOR (n:Publication) ON (n.pmid)
                """)
        
        # Create Publication nodes
        # :Publication: Label of the node
        # id: Primary key of publication
        print("Creating Tools nodes")
        session.run("""
                LOAD CSV WITH HEADERS FROM "file:///%s" AS csv
                CREATE (:Tool {label:csv.label})
                """ % (toolsFile))

def createEdges(driver, edgesFile):
    with driver.session() as session:
        print("Tool-Tool citations")
        session.run("""
            LOAD CSV WITH HEADERS FROM "file:///%s" AS csv
            MATCH (t:Tool {label:csv.label}),(t2:Publication {pmid:csv.pmid})
            CREATE (t)-[:ISCITED]->(t2)
        """ % edgesFile)

def main():
    dict_config = readIni(config_path)

    # URL of the Neo4j Server
    uri = dict_config['url_neo4j_server']
    # Driver to connect to the Server with the author and the password
    # To be able to use it, you need to open your neo4j server before
    driver = GraphDatabase.driver(uri, auth=(dict_config['user'], dict_config['password']))
    
    # Remove previous data
    with driver.session() as session:
        print("Removing all data in the database")
        # Delete all the previous graph
        session.run("""MATCH ()-[r]->() DELETE r""")
        # session.run("""MATCH (r) DELETE r""")
        # session.run("""DROP INDEX index_publications IF EXISTS""")
    
    # createNodes(driver, dict_config["publication_nodes"], dict_config["tool_nodes"])
    createEdges(driver, dict_config["publication_tools_edges"])

if __name__ == '__main__':
    main()
