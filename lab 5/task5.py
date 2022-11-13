import random
import string


def get_random_password(n=None) -> str:
    ...  # TODO написать функцию генерации случайных паролей
    s = string.ascii_uppercase + string.ascii_lowercase + "0123456789"
    if n is None:
        return ''.join(random.sample(s, 8))
    else:
        return ''.join(random.sample(s, n))


print(get_random_password())
