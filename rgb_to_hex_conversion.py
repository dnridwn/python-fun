import math

def decToHex(dec):
    remainder = quotient = dec
    hex = ''
    
    while quotient > 0:
        remainder = quotient % 16
        quotient = math.floor(quotient / 16)
        if remainder > 9:
            hex = chr(remainder + 55) + hex
        else:
            hex = str(remainder) + hex
       
    if hex == '':
        return '00'
    
    return hex.zfill(2)
    
def limit(n):
    if n > 255:
        n = 255
    return n
    
def rgb(r, g, b):
    return decToHex(limit(r)) + decToHex(limit(g)) + decToHex(limit(b))


print(rgb(255, 255, 255))

# The following are examples of expected output values:
# rgb(255, 255, 255) // returns FFFFFF
# rgb(255, 255, 300) // returns FFFFFF
# rgb(0,0,0) // returns 000000
# rgb(148, 0, 211) // returns 9400D3