def f(temperature, temperature_type):
    t = 0
    
    if temperature < -273:
        return Exception("Dana temperatura nie istnieje!")
    elif temperature_type not in ["kelvin", "fahrenheit", "rankine"]:
        return Exception("Musisz wybrac jedna z podanych jednostek: (kelvin, fahrenheit, rankine)")
    
    if temperature_type.lower() == "fahrenheit":
        t = (temperature * 1.8) + 32
    elif temperature_type.lower() == "kelvin":
        t = temperature + 273.15
    elif temperature_type.lower() == "rankine":
        t = (temperature + 273.15) * 1.8
    return t


print(f(76, "fahrenheit"))
print(f(82, "kelvin"))
print(f(38, "rankine"))
print(f(30, "oooo"))
print(f(-550, "kelvin"))
