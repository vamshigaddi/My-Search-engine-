SEARCH_KEY = "AIzaSyC5-4WLDS8Ww53XYUZp6oeb8FsA-cXmpyY"
SEARCH_ID = "b2925ac52333c4ec2"
COUNTRY = "IND"
SEARCH_URL = "https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&num=10&gl=" + COUNTRY
RESULT_COUNT = 15

import os
if os.path.exists("private.py"):
    from private import *