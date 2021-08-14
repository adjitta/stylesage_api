def get_count_of_basic_valid_passphrases(passphrases):
    count_valid_passphrases = 0
    passphrases_list = passphrases.split('\n')
    passphrases_list = sanitize(passphrases_list)
    for passphrase in passphrases_list:
        if is_basic_passphrase_valid(passphrase):
            count_valid_passphrases += 1
    return count_valid_passphrases


def get_count_of_valid_advanced_passphrases(passphrases):
    count_valid_passphrases = 0
    passphrases_list = passphrases.split('\n')
    passphrases_list = sanitize(passphrases_list)
    for passphrase in passphrases_list:
        if is_advanced_passphrase_valid(passphrase):
            count_valid_passphrases += 1
    return count_valid_passphrases


def is_basic_passphrase_valid(passphrases):
    unique_passphrase = []
    passphrase_list = passphrases.split(' ')
    for passphrase in passphrase_list:
        if passphrase not in unique_passphrase:
            unique_passphrase.append(passphrase)
        else:
            return False
    return True


def is_advanced_passphrase_valid(passphrases): #cambiar passphrase
    unique_passphrase = []
    passphrases_list = passphrases.split(' ')
    for passphrase in passphrases_list:
        passphrase_sorted = sorted(passphrase)
        passphrase_sorted = ''.join(passphrase_sorted)
        if passphrase_sorted not in unique_passphrase:
            unique_passphrase.append(passphrase_sorted)
        else:
            return False
    return True


def sanitize(passphrases_list):
    passphrases_list = [passphrase.strip() for passphrase in passphrases_list]
    passphrases_list = [passphrase for passphrase in passphrases_list if len(passphrase) > 0]
    return passphrases_list
