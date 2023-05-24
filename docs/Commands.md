# Commands
Commands follow the syntax:
```
cmd [args]
```
Args is a list of arguments, separated by spaces. For example:
```
cmd arg1 arg2 arg3
```
Comments are prefixed with a hashtag ("`#`")

For example:
```
# This is a comment
```

---
## err
**Args**<br>
error_name, error_msg

**Usage**
```
err error_name error_msg
```

**Behaviour**<br>
Throws an error and ends the program. Looks something like this:
```
ERR (line 1): ExampleError: This is an error thrown by the `err` command.
```

**Example**
```
err ExampleError "This is an error thrown by the `err` command."
```

---
## log
**Args**<br>
msg

**Usage**
```
log msg
```

**Behaviour**<br>
Writes `msg` to the terminal.

**Example**
```
log "Hello, world!"
```

---
## int
**Args**<br>
name, value (optional)

**Usage**
```
int name [value]
```

**Behaviour**<br>
Sets variable `name` to `value` (or `null` if no value is specified) with type `int`.

> **Note**
>
> Variables are strictly typed: if declared with `int`, the variable will always be an integer.

**Examples**<br>
Create a variable called `num` and set it to `1`:
```
int num 1
```
Create a variable with no currently assigned value:
```
int num
```

---
## string
**Args**<br>
name, value (optional)

**Usage**
```
string name [value]
```

**Behaviour**<br>
Sets variable `name` to `value` (or `null` if no value is specified) with type `string`.

**Examples**<br>
Create a variable called `name` and set it to `Abraham Lincoln`:
```
string name "Abraham Lincoln"
```
Create a variable with no currently assigned value:
```
string name
```

---
## del
**Args**<br>
var

**Usage**
```
del var
```

**Behaviour**<br>
Deletes the variable `var` if it exists.

**Examples**<br>
Create, and then delete, a string called `name`:
```
string name
del name
```
`del` can also be used to delete multiple variables at a time:
```
string first_name
string last_name
del first_name last_name
```
> **Note**
>
> There is a technical limitation with `del`: no more than 100 million variables can be deleted at a time. Practically, however, it is unlikely you will ever need to do this.

---
## ns
**Args**<br>
(none)

**Usage**
```
ns
```

**Behaviour**<br>
Logs the current namespace.

> **Note**
>
> `ns` is intended for debug use only; it is unlikely you will ever need it for anything other than this.

**Example**
```
ns
```