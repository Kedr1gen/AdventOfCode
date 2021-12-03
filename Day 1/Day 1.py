f = open ("sonar.txt")
str_msg = f.read()
msg = str_msg.split()
sliding = []
n = (len (msg))   #lenght of input
increased = 0
decreased = 0

for x in range(1, (n-1)):
    if x == 1:
        msg [x-1] = int (msg[x-1])
    msg [x] = int (msg[x])
    msg [x+1] = int (msg[x+1])
    sum_msg = msg [x-1] + msg [x] + msg [x+1]
    sliding.append (sum_msg)

# print(sliding)
len_sliding = len(sliding)

for c in range (1, len_sliding):  
    if sliding [c] > sliding [c-1]:
        increased = increased + 1
        # print ("increased")
    else:
        decreased = decreased +1
        # print ("decreased")
        
print ("Increased je: %d" % increased)
##
##if increased + decreased == n - 1:
##    print("Proběhlo správně!")

# loop, compare n and n+1 -> if n+1 is higher, increased +1
