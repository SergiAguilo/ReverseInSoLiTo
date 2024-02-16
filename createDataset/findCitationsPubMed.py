import requests

def get_citations_by_id(article_id, api_key):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi"
    params = {"dbfrom": "pubmed", "db": "pubmed", "id": article_id, "retmode": "json",
               "api_key" : api_key}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        
        links = data.get("linksets", [])[0].get("linksetdbs", [])

        citations = [link["links"] for link in links]
        return citations
    else:
        print(f"Error: {response.status_code}")
        return None

def insertCitations(c, list_citations, label):
    for citations in list_citations:
        for citation in citations:
            c.execute(f'''INSERT OR IGNORE INTO Publications
            values ({citation})''')
            c.execute(f'''INSERT OR IGNORE INTO ToolsToPublication
            values ("{label}", {citation})''')
    c.execute(f'''INSERT OR IGNORE INTO CacheToolsPublication
            values ("{label}")''')

def findCitations(c, conn, api_key):
    c.execute(f"""
            SELECT pmid, label
            FROM PublicationsForTool 
            where label NOT IN (select label from CacheToolsPublication )
            """)
    pmidsInTools=c.fetchall()

    for pmidInTool in pmidsInTools:
        pmid = pmidInTool[0]
        label = pmidInTool[1]
        list_citations = get_citations_by_id(pmid, api_key)
        if not list_citations:
            continue
        insertCitations(c, list_citations, label)
        conn.commit()


