class Command():
    def __init__(self, args: list, namespace: dict):
        self.argnum = 0
        self.namespace = namespace

    def invoke(self):
        print(self.namespace)
        return {
            "error": ["N/A"]
        }