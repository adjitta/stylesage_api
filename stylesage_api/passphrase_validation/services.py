def fetch_count_validation(words):
    unique_word = []
    word_list = words.split(' ')
    for word in word_list:
        if word not in unique_word:
            unique_word.append(word)
        else:
            return False
    return True


def fetch_count_validation_anagram(words):
    unique_word = []
    word_list = words.split(' ')
    for word in word_list:
        word_sorted = sorted(word)
        word_sorted = ''.join(word_sorted)
        if word_sorted not in unique_word:
            unique_word.append(word_sorted)
        else:
            return False
    return True


count = fetch_count_validation('aa bb cc dd')
valid_anagram = fetch_count_validation_anagram('iiii oiii ooii oooi oooo')
print(valid_anagram)
