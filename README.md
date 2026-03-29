# spotr_backend
Spotr app backend services

The cleanest way to run this application is to use uv as a dependency management tool.
It generates a virtual environment per application and doesn't require you to download
all project dependencies on your machine. The project dependencies live inside  pyproject.toml

1. Run: ```pip3 install uv```
2. Inside your IDE, point your python interpretor to .venv/bin/python
3. Run: ```uv sync``` (installs packages in the virutal env and generates the lock file)
4. Run: ```source .venv/bin/activate``` --> prepends your os' PATH variable with the .venv/bin/python location so it finds that python version first when running any python command
5. You can confirm this by running ```which python```
6. You're ready to run the app!
7. When done, run ```deactivate``` in the terminal

If you don't want to go through uv (Ie: you're running everything via pip) then install all dependencies 
with: ```pip install -r requirements.txt```
This implies that the requirements file is up to date. I will periodically update it, but I highly recommend using uv.
