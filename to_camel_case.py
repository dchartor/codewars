def to_camel_case(text):
    return text[0] + text.title()[1:].replace('-', '').replace('_', '')
