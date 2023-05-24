class Command():
    def __init__(self, args: list, namespace: dict):
        self.argnum = 1
        self.args = args
        self.namespace = namespace

    def invoke(self):
        if self.args[0].startswith("$"):
            var = self.args[0][1:]
            if var not in self.namespace.keys():
                return {
                    "error": ["UnknownVariable", f"The variable '{var}' does not exist."]
                }
            else:
                print(self.namespace[var]["val"])
        else:
            print(self.args[0])
        return {
            "error": ["N/A"]
        }