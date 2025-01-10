def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_year_leap(year) and month == 2:
        return 29
    else:
        return month_lengths[month - 1]

def day_of_year(year, month, day):
    if month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None
    
    day_count = day
    for m in range(1, month):
        day_count += days_in_month(year, m)
        
    return day_count

# Testando a função day_of_year
print(day_of_year(2000, 12, 31))  # Deve retornar 366, pois 2000 é um ano bissexto

# Adicionando mais casos de teste
test_years = [1900, 2000, 2016, 1987, 2021]
test_months = [2, 2, 1, 11, 3]
test_days = [28, 29, 31, 30, 15]
test_results = [59, 60, 31, 334, 74]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    dy = test_days[i]
    print(f"{yr}-{mo:02d}-{dy:02d} -> ", end="")
    result = day_of_year(yr, mo, dy)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fracassado")
