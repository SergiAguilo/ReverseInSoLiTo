
def cleanPublicationsCitations(c,conn):
    # Store publications with >1 relationship
    c.execute('''DROP TABLE IF EXISTS UsedPublications''')
    c.execute('''CREATE TABLE UsedPublications AS
        SELECT pmid
        FROM Publications
        WHERE pmid IN (
            SELECT pmid
            FROM ToolsToPublication
            GROUP BY pmid
            HAVING COUNT(*) > 1);
        ''')
    conn.commit()
    # Store the relationships of the publications with >1 relationships
    c.execute('''DROP TABLE IF EXISTS UsedToolsToPublication''')
    c.execute('''CREATE TABLE UsedToolsToPublication AS
        SELECT *
        FROM ToolsToPublication
        WHERE pmid IN (
            SELECT pmid
            FROM ToolsToPublication
            GROUP BY pmid
            HAVING COUNT(*) > 1);
        ''')
    conn.commit()