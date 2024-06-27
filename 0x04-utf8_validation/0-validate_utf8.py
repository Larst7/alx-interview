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
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    
    # Masks to check the leading bits of a byte
    masks = [0b10000000, 0b11100000, 0b11110000, 0b11111000]
    # Expected patterns for leading bits for characters of different lengths
    patterns = [0b00000000, 0b11000000, 0b11100000, 0b11110000]
    
    for byte in data:
        # Check the first byte
        if num_bytes == 0:
            # Determine the number of bytes in this character
            if (byte & masks[0]) == 0:
                num_bytes = 1
            elif (byte & masks[1]) == patterns[1]:
                num_bytes = 2
            elif (byte & masks[2]) == patterns[2]:
                num_bytes = 3
            elif (byte & masks[3]) == patterns[3]:
                num_bytes = 4
            else:
                return False
            
            # If this character needs more bytes, check the continuation bytes
            if num_bytes > 1:
                num_bytes -= 1
            else:
                num_bytes = 0
        else:
            # Check continuation byte
            if (byte & masks[1]) != 0b10000000:
                return False
            num_bytes -= 1
    
    # If num_bytes is not zero, it means we expected more continuation bytes
    return num_bytes == 0

