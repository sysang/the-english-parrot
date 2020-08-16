from ruamel.yaml import YAML
import requests
import json
import logging
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--model', required=True)
parser.add_argument('--scriptfile', required=True)
args = parser.parse_args()

model = args.model
model = model.replace('models/', '')
model = model.replace('.tar.gz', '')

scriptfile = args.scriptfile

with open(scriptfile, 'r') as f:
    scripts = f.read()

scriptfile = scriptfile.replace('e2etest/data/','')
scriptfile = scriptfile.replace('.yml','')

now = datetime.now()
resultfile = f"e2etest/results/{model}_{scriptfile}_{now.hour}{now.minute}.txt"

logger = logging.getLogger(__name__)
hdlr = logging.FileHandler(resultfile)
formatter = logging.Formatter('%(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

yaml=YAML(typ="safe", pure=True)
scripts = yaml.load(scripts)
scenario = scripts['scenario']

apiurl = 'http://127.0.0.1:5005/webhooks/rest/webhook'
for scene in scenario:
    print("\n***********************************************\n")
    logger.info("\n***********************************************\n")
    for speech in scene:
        payload = { 'sender': 'autotester', 'message': speech }
        r = requests.post(apiurl, data = json.dumps(payload))
        botres = [item['text'] for item in r.json()]
        botres = ''.join(botres)

        print(f"user >  {speech}")
        print("\n")
        print(f"bot  :  {botres}")

        logger.info(f"user >  {speech}")
        logger.info("\n")
        logger.info(f"bot  :  {botres}")

