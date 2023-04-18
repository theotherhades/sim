class Command():
    def __init__(self, args: list):
        self.argnum = 1
        self.args = args

    def invoke(self):
        print(self.args[0])