#!/usr/bin/python3
"""This script resolves the lock boxes puzzle."""

def find_next_opened_box(boxes):
    """
    Finds the next opened box in the list of boxes.

    Args:
        boxes (list): A list of dictionaries representing the boxes.

    Returns:
        list or None: A list of keys contained in the opened box, or None if there are no more opened boxes.
    """
    for index, box in enumerate(boxes):
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None

def canUnlockAll(boxes):
    """
    Checks if all boxes can be opened.

    Args:
        boxes (list): A list containing all the boxes with their respective keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    opened_boxes = {}
    while True:
        if not opened_boxes:
            opened_boxes[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = find_next_opened_box(opened_boxes)
        if keys:
            for key in keys:
                try:
                    if opened_boxes.get(key) and opened_boxes.get(key).get('status') == 'opened/checked':
                        continue
                    opened_boxes[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in opened_boxes.values()]:
            continue
        elif len(opened_boxes) == len(boxes):
            break
        else:
            return False

    return len(opened_boxes) == len(boxes)

def main():
    """Entry point"""
    canUnlockAll([[]])

if __name__ == '__main__':
    main()