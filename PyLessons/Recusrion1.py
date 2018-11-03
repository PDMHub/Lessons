
def bit_str3(n, s, s2):
    if(n==1):
        print("returned s = " + s)
        return s[n-1], s2[n-1]
    a=[]
    for digit in bit_str3(1,s, s2) :
        print("digit = " + digit)
        for bits in bit_str3(n-1,s, s2) :
            print("bits = {0} with n= {1}".format(bits, n))
            a.append(digit+bits)
    return a

def bit_str2(n, s, fName):
    #print ("MAIN return, fName = {}, n = {}".format(fName, n))
    print (("n = {}".format(n).rjust(n*5)))
    #print (("n = {}".format(n).zfill(n*5)))
    if(n==1):
        #print ("IF n==1 return, fName = {}, n = {}".format(fName, n))
        return s
    a=[]
    #print(a)
    for digit in bit_str2(1, s, "digit-For") :
        #print ("digit-For, fName = {}, n = {}".format(fName, n))
        for bits in bit_str2(n-1, s, "bits-For"):
            # print ("bits-For, fName = {}, n = {}".format(fName, n))
            #print("digit+bits=" + (digit+bits))
            a.append(digit+bits)
            #print(a)
    # print ("return a, fName = {}, n = {}".format(fName, n))
    return a

def f1 (n, x):
    zz = []
    if n==1:
        return x
    for a in f1(1, x):
        print(a)
    return x+a 

#print (f1(5, 'abcdg'))

#print bit_str(3,'abc')
#print (bit_str3(3,'abc', 'def'))
print (bit_str2(3, "abc", "firstRun"))