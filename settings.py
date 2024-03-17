SEARCH_KEY = ""
SEARCH_ID = " "
COUNTRY = "IND"
SEARCH_URL = "https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&num=10&gl=" + COUNTRY
RESULT_COUNT = 15

import os
if os.path.exists("private.py"):
    from private import *
