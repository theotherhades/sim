class Command():
    def __init__(self, args: list, namespace: dict):
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
        elif self.args[1].isdigit() == False:
            return {
                "error": ["InvalidType", f"'{self.args[1]}' is not an integer."]
            }
        elif self.args[0] in self.namespace.keys():
            return {
                "error": ["NameCollision", f"The name '{self.args[1]} is already taken."]
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