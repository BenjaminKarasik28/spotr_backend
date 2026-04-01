# spotr_backend
Spotr app backend services

The cleanest way to run this application is to use uv as a dependency management tool.
It generates a virtual environment per application and doesn't require you to download
all project dependencies on your machine. The project dependencies live inside  pyproject.toml

1. Install ```uv``` with your package manager of choice: https://docs.astral.sh/uv/getting-started/installation/#pypi
2. If you are running this inside the IDE terminal, point your Python interpretor to .venv/bin/python
3. Run: ```uv sync``` (installs exact versions of packages from the lock file exist and removes extras) Typically you'd run this after you clone this project, or run ```uv add <dependency>```, or want a fresh app
4. You're ready to run the app! ```uv run uvicorn app.main:app --reload```


If you don't want to go through uv (Ie: you're running everything via pip) then install all dependencies 
with: ```pip install -r requirements.txt```
This implies that the requirements file is up to date. I will periodically update it, but I highly recommend using uv.
```uv run uvicorn app.main:app --reload``` won't work here, you'll need the pip/pip3 equivalent.

Extra deps/apps I use:
1. PyCharm for app development
2. Postman for api testing
   
Troubleshooting:
1. If ```uv run uvicorn app.main:app --reload``` doesn't run, perhaps your Python version is pointing to the globally installed one. You need to point it to the one inside .venv so it can use the correct dependencies:
   1. Run: ```source .venv/bin/activate``` --> prepends your os' PATH variable with the .venv/bin/python location so it finds that python version first when running any python command
   2. You can confirm this by running ```which python``` (it should point to the one inside .venv)
   3. Proceed to step 4 above
   4. When done, run ```deactivate``` in the terminal
