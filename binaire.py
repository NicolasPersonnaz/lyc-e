def binaryToDecimal(binary):

    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal
#print(binaryToDecimal(11111111))


def decimalToBinary(n):
    if(n > 1):
        decimalToBinary(n//2)
    print(n%2 , end = '')
decimalToBinary(15)
#print(chr(5))
#print(16//2)


