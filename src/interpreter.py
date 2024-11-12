class Instance:
    def __init__(self):
        self.mem = [0 for _ in range(256)]
        self.ptr = 0

    def get_current(self):
        return self.mem[self.ptr % 256]

    def set_current(self, val):
        self.mem[self.ptr % 256] = val % 256

    def move_ptr(self, pos):
        self.ptr += pos % 256

    def get_ptr(self):
        return self.ptr % 256

    def get_at(self, pos):
        return self.mem[pos % 2]


def interpret(line, instance: Instance):
    for pos, oper in enumerate(line):
        if isinstance(oper, list):
            while instance.get_current() != 0:
                # print(instance.get_current())
                err = interpret(line[pos], instance)
                if err:
                    return err
            continue
        err = run_oper(oper, instance)
        if err:
            return err

    return None


def run_oper(oper: str, instance: Instance):
    match oper:
        case "+":
            instance.set_current(instance.get_current() + 1)
        case "-":
            instance.set_current(instance.get_current() - 1)
        case ">":
            instance.move_ptr(1)
        case "<":
            instance.move_ptr(-1)
        case ";":
            print(f"{instance.get_current()} ", end="")
        case ".":
            print(f"{chr(instance.get_current())}", end="")
        case _:
            return ("SYNTAX", f"'{oper}': not a command")
    return None
