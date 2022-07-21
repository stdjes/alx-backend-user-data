#!/usr/bin/env python3
""" Regex-ing
"""


import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ that returns the log message obfuscated"""
    for field in fields:
        log_msg = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return log_msg
