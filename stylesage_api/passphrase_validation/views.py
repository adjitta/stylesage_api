from django.shortcuts import render
from django.http import HttpResponse
from .services import fetch_count_validation, fetch_count_validation_anagram


def get_passphrase_validation(request):
    count_valid_passphrases = 0
    word_list = ['aa bb cc dd', 'aa bb cc dd aa', 'aa bb cc dd aaa', 'uu, uu, aa']
    for word in word_list:
        valid_passphrase = fetch_count_validation(word)
        if valid_passphrase:
            count_valid_passphrases += 1
    return HttpResponse(count_valid_passphrases)


def get_passphrase_anagram_validation(request):
    count_valid_passphrases = 0
    word_list = ['abcde fghij', 'abcde xyz ecdab', 'a ab abc abd abf abj', 'iiii oiii ooii oooi oooo']
    for word in word_list:
        valid_passphrase = fetch_count_validation_anagram(word)
        if valid_passphrase:
            count_valid_passphrases += 1
    return HttpResponse(count_valid_passphrases)
