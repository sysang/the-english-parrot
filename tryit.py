import re
import json

s = "[he](actor) [bought](materialpr) [a new car](goal)"

regex = re.compile(r"\[([\w\s]+)\]\((\w+)\)", re.IGNORECASE)

matches = regex.findall(s)

entities = dict()
for match in matches:
    entities[match[1]] = match[0]

# print(json.dumps(entities))
print(matches)
