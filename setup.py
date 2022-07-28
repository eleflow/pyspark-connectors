import io
from setuptools import setup, find_packages

with io.open('README.md', mode='r') as doc:
    LONG_DESCRIPTION = doc.read()
    
VERSION = '0.2.0'

setup(
    name="pyspark-connectors",
    version=VERSION,
    author="Eleflow BigData",
    author_email="caio.araujo@eleflow.com.br",
    description="The easy and quickly way to connect and integrate the Spark project with many others data sources.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url="https://github.com/eleflow/pyspark-connectors/",
    packages=find_packages(exclude=("tests*", "samples*", "docs*",)),
    keywords="pyspark databricks integrator connector cosmosdb sql nosql sqlserver oracle mysql postgres mariadb pipedrive activecampaign googlesheet restapi",
    python_requires=">=3.8",
    license="MIT",
    install_requires=[
        "pyspark == 3.2.1",
        "requests == 2.27.1",
        "google-api-python-client == 2.47.0",
        "google-auth-httplib2 == 0.1.0",
        "google-auth-oauthlib == 0.5.1",
        "azure-cosmos == 4.2.0",
        "unidecode"
    ],
)