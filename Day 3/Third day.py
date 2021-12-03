f = open ("diagnostics.txt")

value = 0
gama = 0 # most common bits
epsilon = 0 # least common bits in each place
num = 0
check = 0
power = 0
ones = []
gama_bin = []
epsilon_bin = []


for line in f:
    line = line.strip() # get rid of \n at the end
    line_len = len(line)
    #print(line)
    ## GOIN THROUGH SINGLE LINE OF BINARY CODE
    for n in range (line_len):
        num = int(line[n])
        #print (num)
        if check == 0: ##CONSRUCTING APROPRIATELLY LONG LISTS
            ones.append (num)
            gama_bin.append (2)
            epsilon_bin.append (2)
        else:
            ones[n] = ones[n] + num
    check = check + 1

## CONSTRUCTING BINARY GAMA AND EPSILON        
for x in range (line_len):
    if ones[x] > (check/2):
        gama_bin [x] = 1
        epsilon_bin [x] = 0
    else:
        gama_bin [x] = 0
        epsilon_bin [x] = 1

## CONVERT BIN TO DECIMAL
for c in range (line_len):
    epsilon = epsilon + (epsilon_bin[c]*2**(line_len - c - 1))
    gama = gama + (gama_bin[c]*2**(line_len - c - 1))
    #print ("Epsilon je %d a gama %d" % (epsilon, gama))

print ("Epsilon je %d a gama %d" % (epsilon, gama))
power = epsilon * gama
print ("Power is %d" % power)
#print (ones, epsilon_bin, gama_bin)

##number = 
##dec_number = int(number, 2)
##print('The decimal conversion is:', dec_number)
##
### print ("Values are " + str(horizontal) + " " + str(depth))
##print ("Values are h: %d and d: %d" % (horizontal, depth))
##final = horizontal * depth
##print ("Final number is %d." % final)

f.close()


