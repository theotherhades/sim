class Command():
    def __init__(self, args: list):
        self.argnum = 2
        self.args = args

    def invoke(self):
        return {
            "error": [self.args[0], self.args[1]]
        }