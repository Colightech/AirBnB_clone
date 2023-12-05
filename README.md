# AirBnB Clone - The Console

## Project Overview

Welcome to the AirBnB clone project! This project focuses on building a command-line interface to manage AirBnB objects, laying the foundation for subsequent tasks like HTML/CSS templating, database storage, API, and front-end integration.

## Project Details

- **Author:** Guillaume
- **Weight:** 5
- **Start Date:** Dec 4, 2023, 6:00 AM
- **End Date:** Dec 11, 2023, 6:00 AM
- **Checker Release Date:** Dec 9, 2023, 12:00 PM

## Concepts and Learning Objectives

### Concepts Explored

- Python packages
- AirBnB clone
- Command interpreter
- Serialization and deserialization
- Abstracted storage engine (File storage)
- Unit testing

### Learning Objectives

By the end of this project, you should be able to:

- Create a Python package
- Develop a command interpreter using the cmd module
- Implement unit testing in a large project
- Serialize and deserialize a class
- Read and write JSON files
- Manage datetime in Python
- Understand UUID, *args, and **kwargs
- Handle named arguments in a function

## Requirements

### Python Scripts

- **Allowed Editors:** vi, vim, emacs
- **Python Version:** 3.8.5
- **Execution Environment:** Ubuntu 20.04 LTS
- **Code Style:** Pycodestyle (version 2.8.*)

### README.md File

- Detailed description of the project
- Explanation of the command interpreter:
  - How to start it
  - How to use it
  - Examples

### AUTHORS File

- List of all contributors to the repository

### Branches and Pull Requests

- Use branches and pull requests on GitHub for team organization

## How to Use

### Interactive Mode

```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

### Non-Interactive Mode

$ echo "help" | ./console.py
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

### Running Test

$ echo "python3 -m unittest 
