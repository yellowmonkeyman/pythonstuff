
def multiply_by_nine_fifths(celsius):
    return celsius*(9/5)

def get_fahrenheit(celsius):
    return multiply_by_nine_fifths(celsius) + 32

print("The temperature is {} degrees F".format(get_fahrenheit(15)))