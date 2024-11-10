class Interpreter:
    def __init__(self, tokens):
        self.tokens = tokens
        self.mem = [0 for _ in range(255)]
        self.ptr = 0
        self.pos = 0

    def load_tokens(self, tok):
        self.tokens = tok
        self.pos = 0
