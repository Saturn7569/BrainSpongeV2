chars = {"LOOP_START": "[", "LOOP_END": "]", "valid_chars": "+-*/[].,"}


def parse_line(_line, _pos=0, _loop=False):
    pos = _pos
    tokens = []

    current_token: str = ""

    while True:
        current_token = ""
        if pos >= len(_line):
            if _loop:
                return [], ("SYNTAX", "Loop not closed"), pos
            break
        current_token = _line[pos]
        if current_token.isspace():
            pos += 1
            continue
        if current_token == chars["LOOP_END"]:
            if not _loop:
                return [], ("SYNTAX", "Not in loop"), pos
            current_token = ""
            break
        if current_token == chars["LOOP_START"]:
            tok, err, pos = parse_line(_line, pos + 1, True)
            if err:
                return [], err, pos
            tokens.append(tok)
            pos += 1
            continue
        tokens.append(current_token)
        pos += 1

    if current_token:
        tokens.append(current_token)

    return tokens, None, pos
