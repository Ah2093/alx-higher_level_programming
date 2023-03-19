#!/usr/bin/python3
# 7-islower.py
#ahmed hamdi <ahmedhamdy20p1@gmailcom>

def islower(c):
    """Check for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
