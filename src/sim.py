import commands.log as log
import commands.comment as comment
import commands.var_string as var_string
import commands.var_int as var_int

class Lang():
    def __init__(self, file: list):
        self.file = file
        self.commands = {
            "log": log.Command,
            "#": comment.Command,
            "string": var_string.Command,
            "int": var_int.Command
        }
        self.namespace = {}

    def parse_lines(self):
        for line in self.file:
            line = line.strip()
            line_array = []
            next_item = ""
            readmode = "default"
            for char in line:
                if char == "\"" and readmode == "default":
                    readmode = "string"
                    continue
                elif char == "\"" and readmode == "string":
                    readmode = "default"
                else:
                    next_item += char
                if readmode == "default" and char == " ":
                    line_array.append(next_item)
                    next_item = ""
            line_array.append(next_item)

            line_array_two_electric_boogaloo = []
            for item in line_array:
                line_array_two_electric_boogaloo.append(item.strip())

            self.parse_line(line_array_two_electric_boogaloo)

    def parse_line(self, line: list):
        command = line[0]
        args = line[:0] + line[0+1:]

        if command not in self.commands.keys():
            Error("IllegalCommand", f"The command '{command}' wasn't recognized by the interpreter, maybe check for typos and try again?").invoke()
        else:
            commandclass = self.commands[command](args)
            if len(args) > commandclass.argnum:
                Error("TooManyArgs", f"The command '{command}' takes {commandclass.argnum} arg(s) but {len(args)} were given.").invoke()
            else:
                command_results = commandclass.invoke()
                if command_results["error"][0] != "N/A":
                    Error(command_results["error"][0], command_results["error"][1]).invoke()
                if "set" in command_results.keys():
                    for k, v in command_results["set"].items():
                        self.namespace[k] = v
            print(self.namespace)

class Error():
    def __init__(self, errtype: str, err: str):
        self.colors = {
            "RED": "\033[0;31m",
            "RESET": "\033[0m"
        }
        self.errtype = errtype
        self.err = err
    
    def invoke(self):
        print(f"{self.colors['RED']}ERR: {self.errtype}: {self.err}{self.colors['RESET']}")
        quit()