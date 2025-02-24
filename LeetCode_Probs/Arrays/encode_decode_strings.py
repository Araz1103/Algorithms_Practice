"""
Design an Algorithm to encode a list of strings to a single string
Then decode a single string to list of strings

The strings can contain UTF-8 Characters

Example I/P
I/P = ["araz", "12#", "*axd", "lolol12#!.;  sf", "yo oy oy"]
We want a single string: "........."
Then we can decode it to get back: ["araz", "12#", "*axd", "lolol12#!.;  sf", "yo oy oy"]
"""

# Intuition
# Basically since the individual strings can contain any character
# We need some 'separator or deliminator' in the single string to help us identify the individual strings
# There is no single unique character(s) we can use, since they can always be part of the individual strings
# So we think smart!
# What if we had an indication about the #num of chars in the individual string
# So we can count ahead and get the string
# Then again we find num chars, count ahead and extract the string
# In this way, the string can contain anything, but it doesn't matter to us!
# Now since the length of a string phrase can be 1, 10, 1000, ... so on!
# So we need a unique identifier to tell us when the length of a string is ended
# So we can capture that correctly!
# Can take anything like: "#", '!' or anything, since we are always looking for it 
# ^(not digits ofcourse, as will overlap with length)


def encode(list_strings):
    encoded_string = ""
    for string_phrase in list_strings:
        len_string = len(string_phrase)
        encoded_string += str(len_string)
        encoded_string += "!"
        encoded_string += string_phrase
    return encoded_string

def decode(encoded_string):
    # We know that the first letter of encoded string tells the #num chars to lookahead
    # We extract those chars as the phrase
    list_strings = []
    
    idx = 0 #starting @zero index, keep going until reach End of String
    while idx < len(encoded_string):
        # Keep taking for length until reach !
        n = ""
        char = encoded_string[idx]
        while char!="!":
            n+=char
            idx+=1
            char = encoded_string[idx]

        # Since reached !, now we know next elements are for string phrase
        n = int(n) #Length of string phrase
        string_phrase = ""
        for i in range(n):
            idx+=1
            string_phrase += encoded_string[idx]
        idx+=1 #Increment to check next #chars for next string phrase
        list_strings.append(string_phrase)
    return list_strings

ip_1 = ["araz", "123", "1#*", "amol"]
encoded_string = encode(ip_1)
print(encoded_string)
decoded_ip = decode(encoded_string)
print(decoded_ip)
print(ip_1==decoded_ip)
ip_2 = ["!12#", "*axd", "lolol12#!.;  sf", "yo oy oy"]
encoded_string = encode(ip_2)
print(encoded_string)
decoded_ip = decode(encoded_string)
print(ip_2==decoded_ip)
print(decoded_ip)



