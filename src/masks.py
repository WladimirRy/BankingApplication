def get_mask_card_number(str_enter: str) -> str:
    """Функция принимает на вход номер карты
    в виде числа и возвращает маску номера
    по правилу XXXX XX** **** XXXX."""
    result = f"{str_enter[:-12]} {str_enter[-12:-10]}** **** {str_enter[-4:]}"
    return result


def get_mask_account(str_enter: str) -> str:
    """Функция принимает на вход номер счета
    в виде числа и возвращает маску номера
    по правилу **XXXX."""
    result = f"{str_enter[:-21]} **{str_enter[-4:]}"
    return result
