def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None  # Argumento inválido
    days_in_months = [31, 29 if is_year_leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_months[month - 1]

# Casos de teste
test_years = [1900, 2000, 2016, 1987, 2020, 2023]
test_months = [2, 2, 1, 11, 2, 5]
test_results = [28, 29, 31, 30, 29, 31]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fracassado")
