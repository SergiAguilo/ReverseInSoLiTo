
def searchTools(c,json_data):
    for tool in json_data:
        if 'publications' not in tool:
            continue
        isPMID = False
        for publication in tool['publications']:
            if 'pmid' not in publication:
                continue
            isPMID = True
            c.execute(f'''INSERT OR IGNORE INTO PublicationsForTool
                    values ("{tool['@label']}",{publication['pmid']})''')
        if not isPMID:
            continue
        c.execute(f'''INSERT OR IGNORE INTO Tools
            values ("{tool['@label']}")''')