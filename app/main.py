import random
import argparse

class CREATE_CODE:

    LENGTH = 8
    def __init__(self, value=None) -> None:
        if value is not None:
            self.LENGTH = value

        self.lower_bound = int('1' + ('0' * (self.LENGTH-1)))
        self.upper_bound = int('9' + ('9' * (self.LENGTH-1)))

    def value(self):
        return random.randint(self.lower_bound, self.upper_bound)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a random code with a customizable length.")
    parser.add_argument("length", type=int, nargs="?", default=8, help="Length of the generated code (default is 8)")
    args = parser.parse_args()
    obj = CREATE_CODE(args.length)
    print(obj.value())