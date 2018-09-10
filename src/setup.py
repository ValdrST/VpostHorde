from distutils.core import setup 
import py2exe 

if __name__ == "__main__":
    setup(name="Vposthorde",
    version="0.01",
    description="Breve descripcion", 
    author="Valdr Stiglitz", 
    author_email="valdr.stiglitz@gmail.com", 
    url="www.url.com", 
    license="GNUv3", 
    scripts=["main.py"],
    console=["main.py"],
    options={"py2exe":{"bundle_files":1}},
    zipfile=None,
    )
