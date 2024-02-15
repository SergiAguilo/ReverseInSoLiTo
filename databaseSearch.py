
def databaseSearch(c, listTools):

    c.execute(f"""
        SELECT pmid
        FROM UsedToolsToPublication
        WHERE label IN {str(tuple(listTools))}
        GROUP BY pmid
        HAVING COUNT(DISTINCT label) = {len(listTools)};
            """)
    commonPmids=c.fetchall()
    listPmid = []
    for pmid in commonPmids:
        listPmid.append(pmid[0])
    return listPmid

def returnTools(c, limit, skip):
    c.execute(f"""
        SELECT *
        FROM Tools
        limit {limit}
        offset {skip}
            """)
    tools=c.fetchall()
    listTools = []
    for tool in tools:
        listTools.append(tool[0])
    return listTools

