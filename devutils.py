import re
import json
from pygments import highlight, lexers, formatters


def showlist(list):
    formatted_json = json.dumps(list, indent=2)
    colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    # print(colorful_json.replace('"', ''))
    simplified_json = ""
    regex_curly_bracket = re.compile(r"^\{$")
    for char in colorful_json:
        if (
            char == '"'
            or char.find("]") != -1
            or char.find("],") != -1
            or char.find("}") != -1
            or char.find("},") != -1
            or char.find(",") != -1
            or regex_curly_bracket.match(char)
        ):
            continue

        simplified_json += char

    print("\n")
    for line in simplified_json.splitlines():
        if line.strip():
            print(line)
    print("\n")


