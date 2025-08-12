def filter_by_state(state_list: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ state
    соответствует указанному значению, по умолчанию ключ state == 'EXECUTED'"""
    new_state = []
    if state == "EXECUTED":
        for i in range(len(state_list)):
            if state_list[i]["state"] == "EXECUTED":
                new_state.append(state_list[i])
        return new_state
    elif state == "CANCELED":
        for i in range(len(state_list)):
            if state_list[i]["state"] == "CANCELED":
                new_state.append(state_list[i])
        return new_state


def sort_by_date(state_list: list, direction_sort: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание),
    т. е. сначала самые последние операции. Функция возвращает новый список, отсортированный по дате('date'). """
    new_data_list = sorted(state_list, key=lambda state_lists: state_lists["date"], reverse=direction_sort)
    return new_data_list
