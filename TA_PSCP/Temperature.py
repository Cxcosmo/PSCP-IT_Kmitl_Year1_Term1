"""Temperature"""
def c_to_f(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9 / 5) + 32
def f_to_c(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5 / 9
def c_to_k(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15
def k_to_c(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15
def f_to_k(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    return (fahrenheit - 32) * 5 / 9 + 273.15
def k_to_f(kelvin):
    """Convert Kelvin to Fahrenheit"""
    return (kelvin - 273.15) * 9 / 5 + 32
def c_to_r(celsius):
    """Convert Celsius to Rankine"""
    return (celsius + 273.15) * 9 / 5
def r_to_c(rankine):
    """Convert Rankine to Celsius"""
    return (rankine - 491.67) * 5 / 9
def main() :
    """Temperature"""
    temp = float(input())
    temp_old = input()
    temp_new = input()
    if temp_old == "C" and temp_new == "F" :
        temp = c_to_f(temp)
    elif temp_old == "F" and temp_new == "C" :
        temp = f_to_c(temp)
    elif temp_old == "C" and temp_new == "K" :
        temp = c_to_k(temp)
    elif temp_old == "K" and temp_new == "C" :
        temp = k_to_c(temp)
    elif temp_old == "F" and temp_new == "K" :
        temp = f_to_k(temp)
    elif temp_old == "K" and temp_new == "F" :
        temp = k_to_f(temp)
    elif temp_old == "C" and temp_new == "R" :
        temp = c_to_r(temp)
    elif temp_old == "R" and temp_new == "C" :
        temp = r_to_c(temp)
    elif temp_old == "F" and temp_new == "R" :
        temp = f_to_c(temp)
        temp = c_to_r(temp)
    elif temp_old == "R" and temp_new == "F" :
        temp = r_to_c(temp)
        temp = c_to_f(temp)
    elif temp_old == "K" and temp_new == "R" :
        temp = k_to_c(temp)
        temp = c_to_r(temp)
    elif temp_old == "R" and temp_new == "K" :
        temp = r_to_c(temp)
        temp = c_to_k(temp)
    print(f"{temp:.2f}")
main()
