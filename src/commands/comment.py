class Command():
    def __init__(self, args: list):
        self.argnum = 99999999 # hopefully no one ever needs more than 100 million words in a comment
        self.args = args

    def invoke(self):
        return {
            "error": ["N/A"]
        }