#4th bit
#/usr/bin/python

def fourth_bit(number):
    bin_number=string(bin(number))
    print (bin_number[-4])
    return bin_number[-4]
    
fourth_bit(5)
