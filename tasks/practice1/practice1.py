def concatenate_strings(a: str, b: str) -> str:
    """
    Функция для сложения двух строк.
    Результат сложения запишите в переменную result.

    :param a: число
    :param b: число
    :return: результат сложения
    """

    result = a + b

    return result


def calculate_salary(totpal_compensation: int) -> float:
    """
    Функция расчета зарплаты, которую сотрудник получит после
    вычета налогов. Ставка налогообложения равна 13%.

    :param total_compensation: сумма зарплаты до вычета налога
    :return: сумма заплаты после вычета налога
    """

    tax_rate = 0.13
    result = totpal_compensation * (1 - tax_rate)

    return result
