
# PySpark Conectors - by: Eleflow BigData

[![Build and Publish on PyPI](https://github.com/eleflow/pyspark-connectors/actions/workflows/python-publish.yml/badge.svg)](https://github.com/eleflow/pyspark-connectors/actions/workflows/python-publish.yml)

This library provides many connections and integrations with another data sources.

## Index

- [PySpark Conectors - by: Eleflow BigData](#pyspark-conectors---by-eleflow-bigdata)
  - [Index](#index)
  - [Installing](#installing)
  - [Development enviroment](#development-enviroment)
    - [Packaging project in a .whl lib](#packaging-project-in-a-whl-lib)
  - [Library development status](#library-development-status)
    - [Connectors](#connectors)
    - [Helpers and Utils](#helpers-and-utils)
  - [Version history](#version-history)

## Installing

```bash
pip install pyspark-connectors
```

## Development enviroment

For develop you must guarantee that you have the Python (3.8 or higher) and Spark (3.1.2 or higher) installed, if you have ready the minimum environment for development in Python language, proceed with these steps:

```bash
# Clonning the project
$ git clone git@github.com:eleflow/pyspark-connectors.git

# Inside of the project root folder
$ python -m venv .env

# If Windows
$ .\.env\Script\Activate.ps1 
# If linux dist
$ .\.env\Scripts\activate

# Installing requirements libraries
(.env) $ pip install -r .\requirements.txt
```

### Packaging project in a .whl lib

```bash
# Installing wheel package
(.env) $ pip install wheel

# Installing wheel contents
(.env) $ pip install check-wheel-contents

# Build and packaging project to .whl
(.env) $ python setup.py bdist_wheel
```

## Library development status

### Connectors

- [x] Google Sheets
- [x] Rest API
- [x] SQL Database
- [x] CosmosDB
- [ ] Elasticsearch
- [x] PipeDrive
- [ ] ActiveCampaign
- [ ] ReclameAqui
- [ ] Jira

### Helpers and Utils

- [ ] AWS Secrets Manager

## Version history

| Version | Date | Changes | Notes | Approved by |
| --- | --- | --- | --- | --- |
| 0.0.1a2 | 2022-05-08 | Initial development release | N/A | [@caiodearaujo](https://github.com/caiodearaujo) |
| 0.1.0 | 2022-06-01 | Initial release | N/A | [@caiodearaujo](https://github.com/caiodearaujo) |
| 0.2.0 | 2022-07-28 | New release with connectors stable | N/A | [@caiodearaujo](https://github.com/caiodearaujo) |

