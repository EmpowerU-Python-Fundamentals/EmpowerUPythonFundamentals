import re

def find_secret_message(paragraph):
    words = re.findall(r'\b\w+\b', paragraph.lower())
    
    seen = set()
    duplicates = []
    
    for word in words:
        if word in seen:
            if word not in duplicates:
                duplicates.append(word)
        else:
            seen.add(word)
    
    return ' '.join(duplicates)
