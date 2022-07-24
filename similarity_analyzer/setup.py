import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.0'
PACKAGE_NAME = 'similarity_analyzer'
AUTHOR = 'Author'
AUTHOR_EMAIL = 'author@email.com'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'Document similarity analyzer by keywords based on the TF-IDF criterion'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"


setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      )
