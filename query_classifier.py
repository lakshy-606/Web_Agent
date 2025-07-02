# query_classifier.py

import re

# Define patterns or phrases typical of invalid intents (e.g., commands, reminders)
INVALID_PATTERNS = [
    r"\b(add|remove|buy|call|text|remind|walk|play|open|get)\b.*",    # e.g. add apples, walk my dog
    r"\b(set|schedule|create)\b.*\b(reminder|alarm|event)\b",     # e.g. set a reminder
    r"^\s*(turn on|turn off|switch on|switch off)\b",             # e.g. turn on the light
    r"\b(grocery|todo|shopping|playlist|music)\b.*",              # e.g. grocery list
]

def is_valid_query(query: str) -> bool:
    if not query or len(query.split()) < 3:
        return False  # Too short to be meaningful

    for pattern in INVALID_PATTERNS:
        if re.search(pattern, query, re.IGNORECASE):
            return False

    return True
