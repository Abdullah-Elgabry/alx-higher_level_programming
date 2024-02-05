#!/usr/bin/python3
"""this module aim to ++ atributes ->> object"""


def add_attribute(object, attribute, att_val):
    """this will ++ atributes ->> obj
    Args:
        object: the targeted object
        attribute : atributes name
        att_val : attribute val
    Raises:
        TypeError: will raise if cannot add
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attribute, att_val)
