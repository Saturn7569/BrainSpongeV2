class Instance:
    def __init__(self):
        self.mem = [0 for _ in range(256)]
        self.ptr = 0

    def get_current(self):
        return self.mem[self.ptr]

    def set_current(self, val):
        self.mem[self.ptr] = val % 256


def interpret(line, instance: Instance):
    for pos, oper in enumerate(line):
        if isinstance(oper, list):
            while instance.get_current() != 0:
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
        case ",":
            print(f"{instance.get_current()} ", end="")
        case _:
            return ("SYNTAX", f"'{oper}': not a command")
    return None
