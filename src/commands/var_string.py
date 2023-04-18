class Command():
    def __init__(self, args: list):
        self.argnum = 2
        self.args = args

    def invoke(self):
        return {
            "error": ["N/A"],
            "set": {
                self.args[0]: {
                    "type": "string",
                    "val": self.args[1]
                }
            }
        }