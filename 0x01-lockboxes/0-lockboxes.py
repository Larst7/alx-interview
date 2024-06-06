#!/usr/bin/python3
from typing import List

def canUnlockAll(boxes: List[List[int]]) -> bool:
    n = len(boxes)
    opened = [False] * n
    opened[0] = True  # The first box is initially opened
    keys = boxes[0]  # Start with the keys in the first box

    while keys:
        new_keys = []
        for key in keys:
            if 0 <= key < n and not opened[key]:
                opened[key] = True
                new_keys.extend(boxes[key])
        keys = new_keys

    return all(opened)

