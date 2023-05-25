class Command():
    def __init__(self, args: list, namespace: dict):
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
                        "type": "int",
                        "val": None
                    }
                }
            }
        elif self.args[1].isdigit() == False:
            if self.args[1].startswith("$"):
                if (self.args[1][1:] in self.namespace.keys()) and (self.namespace[self.args[1][1:]]["type"] == "int"):
                    return {
                        "error": ["N/A"],
                        "set": {
                            self.args[0]: {
                                "type": "int",
                                "val": self.namespace[self.args[1][1:]]["val"]
                            }
                        }
                    }
                elif self.namespace[self.args[1][1:]]["type"] != "int":
                    return {
                        "error": ["InvalidType", f"'{self.args[1]}' is not an integer."]
                    }
                elif self.args[1][1:] not in self.namespace.keys():
                    return {
                        "error": ["UnknownVariable", f"The variable '{self.args[1][1:]}' does not exist."],
                    }
            elif self.args[1].startswith("("):
                if self.args[1].endswith(")") == False:
                    return {
                        "error": ["InvalidSyntax", f"Math statement '{self.args[1]}' wasn't terminated"]
                    }
                else:
                    math_statement = self.args[1][1:-1]
                    # do this later
            else:
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