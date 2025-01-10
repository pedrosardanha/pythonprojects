def liters_100km_to_miles_gallon(liters):
    miles_per_kilometer = 1 / 1.609344
    gallons_per_liter = 1 / 3.785411784
    mpg = (100 * miles_per_kilometer) / (liters * gallons_per_liter)
    return mpg

def miles_gallon_to_liters_100km(miles):
    kilometers_per_mile = 1.609344
    liters_per_gallon = 3.785411784
    l_100km = (100 * liters_per_gallon) / (miles * kilometers_per_mile)
    return l_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
