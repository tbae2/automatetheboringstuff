import pprint

# pprint module to pretty print the dict
message = "these are the characters to count in this string"

#instantiate a ddict to hold keys and counts of characters
count = {}

for character in message:
    # cool set default method to create a blank count in one line
    count.setdefault(character,0)
    count[character] += 1

# pprint.pprint to beautiffy the print output of the dict 
pprint.pprint(count)