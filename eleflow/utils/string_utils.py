import re, unidecode

def normalize_string(s):
    return unidecode.unidecode(s.lower())

def to_snake_case(s):
    s = normalize_string(s)
    s = s.replace(' (', '').replace(')', '')
    return '_'.join(re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', s.replace('-', ' '))).split()).lower()