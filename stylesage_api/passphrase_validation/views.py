from django.http import HttpResponse
from .services import get_count_of_basic_valid_passphrases, get_count_of_valid_advanced_passphrases


def get_basic_passphrase_validation(request):
    passphrases = request.body.decode("utf-8")
    count_valid_passphrases = get_count_of_basic_valid_passphrases(passphrases)
    return HttpResponse(count_valid_passphrases)


def get_advanced_passphrase_validation(request):
    passphrases = request.body.decode("utf-8")
    count_valid_passphrases = get_count_of_valid_advanced_passphrases(passphrases)
    return HttpResponse(count_valid_passphrases)
