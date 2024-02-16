# Creating the Reverse InSoLiTo Dataset

These scripts take all the tools from OpenEBench and look which are the articles that references them. With this, we can see articles that cited more than one tool at once.

You can install the required libraries with the `requirements.txt` file.

## Create Database

For running the main script you need to specify the name of the databas with the `-d` flag, the tools information json file based on of the one from [OpenEBench](https://openebench.bsc.es/monitor/rest/search?=publications) with `-i` and your personal PubMed API key with the `-a` flag.

However, the json files only needs the following structure with the `@label` and `publications` with `pmid` fields:

```
[
	{
		"@label":"tool-name",
		"publications":[
			{
				"pmid": "1234"
			},
			{
				"pmid": "4567"
			}
		]
	}
]

```

Then, run the script:

```
python3 main.py -d databaseName -i toolsOEB -a XXXXXXXXX
```

As you query many times PubMed, these platform may restrict your access during few hours. If this happens, just rerun the script and it will continue with the last tool it has stored.

If you want to upload this data to Neo4j, run the script at [Neo4jImport](./Neo4jImport).
