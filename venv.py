import os # under construction, dont run, will break ur device

def venv(name):
    os.system(f"python -m venv {name}")
    os.system(f"source {name}/bin/activate")

venv("venv")
