class Command():
    def __init__(self, args: list):
        self.argnum = 2
        self.args = args

    def invoke(self):
        if self.args[1].isdigit() == False:
            return {
                "error": ["InvalidType", f"'{self.args[1]}' is not an integer."]
            }
        else:
            return {
                "error": ["N/A"],
                "set": {
                    self.args[0]: {
                        "type": "int",
                        "val": int(self.args[1])
                    }
                }
            }