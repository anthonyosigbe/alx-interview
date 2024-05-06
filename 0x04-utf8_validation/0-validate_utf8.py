#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    A method to verify whether a dataset is a valid UTF-8 encoding.
    """
    byte_count = 0

    filter_1 = 1 << 7
    filter_2 = 1 << 6

    for i in data:

        filter_byte = 1 << 7

        if byte_count == 0:

            while filter_byte & i:
                byte_count += 1
                filter_byte = filter_byte >> 1

            if byte_count == 0:
                continue

            if byte_count == 1 or byte_count > 4:
                return False

        else:
            if not (i & filter_1 and not (i & filter_2)):
                    return False

        byte_count -= 1

    if byte_count == 0:
        return True

    return False
