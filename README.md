# My-Search-engine-
In this project, we'll build a search engine that uses filtering to reorder results. The engine will get results from the Google API, store them, then rank them based on filters we define. We'll end up with a basic search page and results list.

# Project Steps

Setup a programmable search engine Custom Search API
You can create one here
Create an API key for the engine
Create a module to search using the API
Create a Flask application to search and render results
Create filters to re-rank results before displaying them

# Code

app.py - the web interface
filter.py - the code to filter results
search.py - code to get the search results
settings.py - settings needed by the other files
storage.py - code to save the results to a database

# Local Setup
To follow this project, please install the following locally:

Python 3.9+
Required Python packages (pip install -r requirements.txt
# Other files
You'll need to download a list of ad and tracker urls from here. We'll use this to filter out bad domains. Please save it as blacklist.txt

# Run
Run the project with:

pip install -r requirements.txt
flask --debug run --port 5001
