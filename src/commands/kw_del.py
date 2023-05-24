class Command():
    def __init__(self, args: list, namespace: dict):
        self.argnum = 99999999
        self.args = args
        self.namespace = namespace

    def invoke(self):
        return {
            "error": ["N/A"],
            "unset": self.args
        }