class Interpreter:
    def __init__(self, tokens):
        self.tokens = tokens
        self.mem = [0 for _ in range(255)]
        self.ptr = 0
