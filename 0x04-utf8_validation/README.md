# UTF-8 Validation

## Project Overview

This project involves writing a Python function to validate whether a given dataset represents a valid UTF-8 encoding. The function will ensure that each character in the dataset follows the UTF-8 encoding rules, where characters can be 1 to 4 bytes long.

## Learning Objectives

- Understanding UTF-8 encoding scheme
- Applying bitwise operations in Python
- Handling data at the byte level
- Using logical operations to validate data

## Requirements

- The project must be implemented in Python 3.
- Your code should adhere to PEP 8 style guidelines.
- The code will be executed on Ubuntu 20.04 LTS using Python 3.4.3.
- All files should end with a new line and the first line should be `#!/usr/bin/python3`.
- Create a `README.md` file at the root of the project directory.
- All files must be executable.

## Usage

### Function Prototype

```python
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing the data bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """

