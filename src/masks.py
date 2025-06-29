def get_mask_card_number(s: str) -> str:
    """Функция принимает на вход номер карты
    в виде числа и возвращает маску номера
    по правилу XXXX XX** **** XXXX."""
    result = f"{s[0:4]} {s[4:6]}** ****  {s[-4:]}"
    return result


def get_mask_account(s: str) -> str:
    """Функция принимает на вход номер счета
    в виде числа и возвращает маску номера
    по правилу **XXXX."""
    result = f"**{s[-4:]}"
    return result