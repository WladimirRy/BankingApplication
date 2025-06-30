from src.masks import get_mask_account, get_mask_card_number


def get_date(str_enter: str) -> str:
    """Функция принимает на вход строку с датой
    в формате "2024-03-11T02:26:18.671407" и
    возвращает строку с датой в
    формате "ДД.ММ.ГГГГ. ("11.03.2024")"""
    result = f"{str_enter[8:10]}.{str_enter[5:7]}.{str_enter[0:4]}"
    return result


def mask_account_card(str_enter: str) -> str:
    """Функция принимает на вход номер карты или счета и
    выводит информацию в форматах:
    ('ТИП КАРТЫ' XXXX XX** **** XXXX) - для карты,
    ('СЧЁТ' **XXXX) - для счёта."""
    digital_value = 0
    for i in str_enter:
        if i.isdigit():
            digital_value += 1
    if digital_value >= 17:
        result = get_mask_account(str_enter)
        return result
    else:
        result = get_mask_card_number(str_enter)
        return result
