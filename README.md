# spotr_backend
Spotr app backend services

The cleanest way to run this application is to use uv as a dependency management tool.
It generates a virtual enviroenemtn per application and doesn't require you to download
all project dependencies on your machine. The project dependencies live inside  pyproject.toml

1. pip3 install uv
2. If you're using PyCharm (I am), then point your python interpretor to .venv/bin/python
3. uv sync (installs packages in the virutal env and generates the lock file)
4. source .venv/bin/activate
5. You're ready to run the app!

If you don't want to go through uv (Ie: you're running everything via pip) then install all dependencies 
with: pip install -r requirements.txt
This implies that the requirements file is up to date. I will periodically update it, but I highly recommend using uv.
