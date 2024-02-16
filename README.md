# ReverseInSoLiTo
API that search tools and retrieve the common articles where these tools have been cited.

## Requirements

Python 3.5 or later is needed. The script depends on standard libraries, plus the ones declared in [requirements.txt](requirements.txt).
 
 * In order to install the dependencies you need `pip` and `venv` Python modules.
	- `pip` is available in many Linux distributions (Ubuntu package `python-pip`, CentOS EPEL package `python-pip`), and also as [pip](https://pip.pypa.io/en/stable/) Python package.
	- `venv` is also available in many Linux distributions (Ubuntu package `python3-venv`). In some of these distributions `venv` is integrated into the Python 3.5 (or later) installation.

* The creation of a virtual environment and installation of the dependencies in that environment is done running:

```bash
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Download Database

```
wget https://zenodo.org/api/records/10666656/files/databaseReverse.db.gz
gunzip databaseReverse.db.gz
```

Also, you can create manually the database in [createDataset](./createDataset)


## Usage

Run the script:

```
python3 main.py -d databaseReverse.db
```

Then, go to [localhost:5000](localhost:5000) and you can do the two following queries:

- List all the tools available in the database (limit default 10 and skip default is 0):

```
localhost:5000/listTools

localhost:5000/listTools?limit=10&skip=0
```

- Search common articles where tools are referenced:

```
localhost:5000/search


localhost:5000/search?tool=ps2&tool=ps2-v3&tool=3d-pssm
```
