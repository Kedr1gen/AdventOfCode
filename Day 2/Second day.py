f = open ("direction_input.txt")

value = 0
horizontal = 0
depth = 0
aim = 0
final = 0

for line in f:
    line = line.strip() # get rid of \n at the end
    value = int(line[-1]) # without \n the number I want is last item of string
    direction = line[0] #first letter is enough to determine here
    # alternative would be to read until space, then compare stings
    
    if direction == "f":
        horizontal = horizontal + value
        depth = depth + (value*aim)
    elif direction == "u":
        aim = aim - value
    elif direction  == "d":
        aim = aim + value
    else:
        print ("ERROR")
        break


# print ("Values are " + str(horizontal) + " " + str(depth))
print ("Values are h: %d and d: %d" % (horizontal, depth))
final = horizontal * depth
print ("Final number is %d." % final)

f.close()


