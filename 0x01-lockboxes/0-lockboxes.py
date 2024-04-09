#!/usr/bin/python3
"""
This module contains a function to solve the Lockboxes problem.
"""


def canUnlockAll(boxes):
    """
    Determines if boxes can be unlocked.
    """
    # Initialize a set to keep track of opened boxes
    unlocked_boxes = {0}  # Start with the first box unlocked.

    # Initialize a set to keep track of opened boxes
    key_s = set(boxes[0])  # Initialize with keys from the first box.

    # Iterate until there are no more keys or all boxes are opened
    while key_s:
        new_key_s = set()

        for key in key_s:
            if key < len(boxes) and key not in unlocked_boxes:
                unlocked_boxes.add(key)
                new_key_s.update(boxes[key])

        # Update the set of keys with newly found keys
        key_s = new_key_s

    return len(unlocked_boxes) == len(boxes)
