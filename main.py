import sys, os
import json
# get this file's directory independent of where it's run from
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "../"))
sys.path.append(os.path.join(here, "../vendored"))

import datamuse
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def run(event, context):
    return json.dumps(datamuse.search_datamuse_wordenp(event['query']['clue']))

print("aa")
print(run())