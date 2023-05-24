class Command():
    def __init__(self, args: list, namespace):
        self.argnum = 2
        self.args = args
        self.namespace = namespace

    def invoke(self):
        if self.args[0] in self.namespace.keys():
            return {
                "error": ["NameCollision", f"The name '{self.args[0]}' is already taken."]
            }
        elif len(self.args) == 1:
            return {
                "error": ["N/A"],
                "set": {
                    self.args[0]: {
                        "type": "string",
                        "val": None
                    }
                }
            }
        else:
            if self.args[1].startswith("$"):
                if self.args[1][1:] in self.namespace.keys():
                    return {
                        "error": ["N/A"],
                        "set": {
                            self.args[0]: {
                                "type": "string",
                                "val": str(self.namespace[self.args[1][1:]]["val"])
                            }
                        }
                    }
                else:
                    return {
                        "error": ["UnknownVariable", f"The variable '{self.args[1][1:]}' does not exist."],
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