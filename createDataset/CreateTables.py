

def createSQLTables(c):
        
    # Publications table - It will be used to create Publication nodes
    # pmid: PMID of the publication
    c.execute('''DROP TABLE IF EXISTS Publications''')
    c.execute('''CREATE TABLE IF NOT EXISTS "Publications" (
                    "pmid" INTEGER NOT NULL,
                    PRIMARY KEY("pmid")
                );''')
    
    # Tools table - It will be used to create Tools nodes
    c.execute('''DROP TABLE IF EXISTS Tools''')
    c.execute('''CREATE TABLE IF NOT EXISTS "Tools" (
                    "label" TEXT NOT NULL,
                    PRIMARY KEY("label")
                );''')
    
    # Publications describing a tool table 
    c.execute('''DROP TABLE IF EXISTS PublicationsForTool''')
    c.execute('''CREATE TABLE IF NOT EXISTS "PublicationsForTool" (
                    "label" TEXT NOT NULL,
                    "pmid" INTEGER NOT NULL
                );''')

    # Tools to publications table - Relationships about the co-occurrences
    # between the tools and the articles that they are cited
    # c.execute('''DROP TABLE IF EXISTS ToolsToPublication''')
    c.execute('''CREATE TABLE IF NOT EXISTS "ToolsToPublication" (
                    "label" TEXT NOT NULL,
                    "pmid" INTEGER NOT NULL,
                    FOREIGN KEY("label") REFERENCES "Tools"("label"),
                    FOREIGN KEY("pmid") REFERENCES "Publications"("pmid"),
                    unique(label, pmid)
                );''')
    
    # Cache tools publications
    # c.execute('''DROP TABLE IF EXISTS CacheToolsPublication''')
    c.execute('''CREATE TABLE IF NOT EXISTS "CacheToolsPublication" (
                    "label" TEXT NOT NULL,
                    PRIMARY KEY("label")
                );''')
    
    # Used Publications table
    c.execute('''DROP TABLE IF EXISTS UsedPublications''')
    c.execute('''CREATE TABLE IF NOT EXISTS "UsedPublications" (
                    "pmid" TEXT NOT NULL,
                    PRIMARY KEY("pmid")
                );''')
    
    # >2 relationships between tool and publication table
    c.execute('''DROP TABLE IF EXISTS UsedToolsToPublication''')
    c.execute('''CREATE TABLE IF NOT EXISTS "UsedToolsToPublication" (
                    "label" TEXT NOT NULL,
                    "pmid" INTEGER NOT NULL,
                    FOREIGN KEY("label") REFERENCES "Tools"("label"),
                    FOREIGN KEY("pmid") REFERENCES "UsedPublications"("pmid"),
                    unique(label, pmid)
                );''')
    
