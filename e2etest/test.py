from ruamel.yaml import YAML
import requests
import json
import logging

logger = logging.getLogger(__name__)

with open('e2etest/data/test_main_scenario.yml', 'r') as f:
    data = f.read()

yaml=YAML(typ="safe", pure=True)
data = yaml.load(data)
inputs = data['inputs']

for msg in inputs:
    payload = { 'sender': 'rasa', 'message': msg }
    r = requests.post('http://127.0.0.1:5005/webhooks/rest/webhook', data = json.dumps(payload))
    botres = [item['text'] for item in r.json()]
    botres = ''.join(botres)
    print(f"user >  {msg}")
    print("\n")
    print(f"bot  :  {botres}")

