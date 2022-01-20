def convert_time(duration: int) -> str:
    sec = duration
    min = sec / 60
    hour = sec / 3600
    day = sec / 86400
    if duration <= 60:
        return f'{sec} сек'
    elif 60 <= duration <= 3600:
        return f'{min} мин {sec % 60} сек'
    elif 3600 <= duration <= 86400:
        return f'{hour} час {min % 60} мин {sec % 60} сек'
    else:
        return f'{day} дн {hour % 24} час {min % 60} мин {sec % 60} сек'


duration = 400153
result = convert_time(duration)
print(result)

# Не понятно почему выводятся дробные числа, где возникла ошибка формата?