def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""

    if number in range(11,15):
     return final_result.format(number, "ов")
    elif number % 10 == 1:
        return final_result.format(number, "")
    elif 1<number % 10 < 5:
        return final_result.format(number, "a")
    elif number > 4:
        return final_result.format(number, "ов")

final_result = "{} процент{}"
for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))
