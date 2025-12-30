def word_count(text):
    words = text.split()
    return len(words)

def char_count_dict(text):
    return dict((char, text.lower().count(char)) for char in set(text.lower()))

def sorted_char_count_list(char_count_dict):
    '''create list of dictionaries each with char and num'''
    return sorted(
        [{'char': char, 'num': num} for char, num in char_count_dict.items()],
        key=lambda x: x['num'],
        reverse=True
    )
    