#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing the data bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for byte in data:
        # Ensure byte is in the range of a valid byte
        if byte < 0 or byte > 255:
            return False

        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7) != 0:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0

# Test cases (to be removed or commented out in production)
data1 = [65]
print(validUTF8(data1))  # True

data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data2))  # True

data3 = [229, 65, 127, 256]
print(validUTF8(data3))  # False

