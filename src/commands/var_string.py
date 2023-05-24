class Command():
    def __init__(self, args: list, namespace):
        self.argnum = 2
        self.args = args
        self.namespace = namespace

    def invoke(self):
        if len(self.args) == 1:
            return {
                "error": ["N/A"],
                "set": {
                    self.args[0]: {
                        "type": "int",
                        "val": None
                    }
                }
            }
        else:
            return {
                "error": ["N/A"],
                "set": {
                    self.args[0]: {
                        "type": "string",
                        "val": self.args[1]
                    }
                }
            }