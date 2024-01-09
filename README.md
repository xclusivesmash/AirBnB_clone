# AirBnB Clone Project

## Description
> This project is based on using programming tools to create a full web application (airbnb) clone. It encapsules basic features such as data storage models, HTML/CSS templating, API, front-end integration, etc. More features can easily be added to match the actual website.

## Learning Objectives
- How to create a Python package.
- How to create a command intepreter in Python using the `cmd` module.
- What is and how to implement unit testing in a larger project.
- How to serialize and deserialize a class.
- How to write and read a json file.
- How to manage `datetime`
- What is `uuid`
- What is `*args` and `**kwargs`, and how to use them.
- How to handle named arguments in a function.

## Requirements
- OS: `Ubuntu 20.04 LTS`
- Language(s): `Python3x`, `HTML/CSS`, `SQL`, `Bash`, `Javascript`
- Style Guide: `PEP8`, `shellcheck`, `pycodestyle (version 2.8.*)`
- Editors: `vi`, `vim`, or `emacs`
- All files must be executable.
- All modules, classes, and functions should have documentation.
- All tests should be inside a folder `tests`.
- The [unittest module](https://intranet.alxswe.com/rltoken/op1-rQGlw0wwwqNBsn1yaw) should be used for tests.
- All tests will be executed using `python3 -m unittest discover tests`.

## Execution
The shell works like this in interactive mode:
```$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

It also works like this in non-interactive mode:
```$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: `echo "python3 -m unittest discover tests" | bash`
<br>

## Authors
- Siphamandla Matshiane, [![Twitter](http://i.imgur.com/wWzX9uB.png)](https://www.twitter.com/sbumatshiane916)
- Opeoluwa Muritala, [![Twitter](http://i.imgur.com/wWzX9uB.png)](https://www.twitter.com/)

## LICENSE
- [ALX Software Engineering Programme](https://www.alxafrica.com/software-engineering/)
