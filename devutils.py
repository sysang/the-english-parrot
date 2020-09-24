import re
import json
from pygments import highlight, lexers, formatters


def showlist(list):
    formatted_json = json.dumps(list, indent=2)
    colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    simplified_json = ""
    regex_bracket = re.compile(r"\}$|\},$|\]$|\],$")
    regex_square_open_bracket = re.compile(r"\w+\:\s\[$")
    regex_curly_open_bracket = re.compile(r"\{$")

    for line in colorful_json.splitlines():
        if regex_bracket.search(line):
            continue

        if regex_square_open_bracket.search(line):
            line += ']'

        if regex_curly_open_bracket.search(line):
            line += '}'

        simplified_json += line + '\n'

    for line in simplified_json.splitlines():
        print(line)


