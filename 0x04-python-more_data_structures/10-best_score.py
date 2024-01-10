#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    m_value = 0
    m_key = None
    for d, t in a_dictionary.items():
        if t > m_value:
            m_value = t
            m_key = d
    return m_key
