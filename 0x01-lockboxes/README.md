# Lockboxes

This project contains a function that determines if all the boxes in a given list can be opened. Each box may contain keys to other boxes, and the function aims to check if all boxes can be opened using the available keys.

## Function

### canUnlockAll

**Prototype:** `def canUnlockAll(boxes: List[List[int]]) -> bool`

**Parameters:**
- `boxes`: A list of lists. Each inner list represents a box and contains keys to other boxes.

**Returns:** `True` if all boxes can be opened, otherwise `False`.

## Usage

To use this function, simply import it and call it with the appropriate parameters.

```python
canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True
