# Description: Converts a base 10 integer to a string representation of the integer in the specified base

def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)