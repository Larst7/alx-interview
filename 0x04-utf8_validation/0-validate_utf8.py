#!/usr/bin/python3
"""utf-8 validation module"""

def validUTF8(data):
    """
    Determine if the given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): The list of integers representing the data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for byte in data:
        # Mask the byte to get the least significant 8 bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the character
            if byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            elif byte >> 7 == 0:
                continue
            else:
                return False
        else:
            # Check continuation byte (should start with '10')
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    # If num_bytes is not zero, then we have an incomplete character
    return num_bytes == 0

# Test cases (to be removed or commented out in production)
if __name__ == "__main__":
    data1 = [65]
    print(validUTF8(data1))  # True

    data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data2))  # True

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))  # False
