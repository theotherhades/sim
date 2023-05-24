import commands.log as log
import commands.comment as comment
import commands.var_string as var_string
import commands.var_int as var_int
import commands.err as err
import commands.kw_del as kw_del
import commands.ns as ns

class Lang():
    def __init__(self, file: list):
        self.file = file
        self.commands = {
            "log": log.Command,
            "#": comment.Command,
            "": comment.Command, # Stop it raising IllegalCommand when it hits an empty line
            "string": var_string.Command,
            "int": var_int.Command,
            "err": err.Command,
            "del": kw_del.Command,
            "ns": ns.Command
        }
        self.namespace = {}
        self.curline = 0

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

            self.curline += 1
            self.parse_line(line_array_two_electric_boogaloo)

    def parse_line(self, line: list):
        command = line[0]
        args = line[:0] + line[0+1:]

        # Account for comments starting with "#" that don't have a space (for example: "#comment")
        if command.startswith("#"):
            command = "#"
        elif command not in self.commands.keys():
            Error("IllegalCommand", f"The command '{command}' wasn't recognized by the interpreter, maybe check for typos and try again?", self.curline).invoke()
        else:
            match command:
                case "string" | "int" | "del" | "ns":
                    commandclass = self.commands[command](args, self.namespace)
                
                case default:
                    commandclass = self.commands[command](args)

            if len(args) > commandclass.argnum:
                Error("TooManyArgs", f"The command '{command}' takes {commandclass.argnum} arg(s) but {len(args)} were given.", self.curline).invoke()
            else:
                command_results = commandclass.invoke()
                if command_results["error"][0] != "N/A":
                    Error(command_results["error"][0], command_results["error"][1], self.curline).invoke()
                if "set" in command_results.keys():
                    for k, v in command_results["set"].items():
                        self.namespace[k] = v
                if "unset" in command_results.keys():
                    for i in command_results["unset"]:
                        if i not in self.namespace.keys():
                            Error("UnknownItem", f"'{i}' does not exist in namespace.", self.curline).invoke()
                        else:
                            del self.namespace[i]

class Error():
    def __init__(self, errtype: str, err: str, curline: int = None):
        self.colors = {
            "RED": "\033[0;31m",
            "RESET": "\033[0m"
        }
        self.errtype = errtype
        self.err = err
        self.curline = curline
    
    def invoke(self):
        print(f"{self.colors['RED']}ERR{f' (line {self.curline})' if self.curline != None else ''}: {self.errtype}: {self.err}{self.colors['RESET']}")
        quit()