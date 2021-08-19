"""
Password Manager
crypte file
By Ulysse Valdenaire
11/08/2021
"""

def code_cesar(word_to_code, keys, security):
    """
    crypte a string with a key (int) and a security(int)
    """
    finalCode = ''#will be the password crypted at the end
    security = int(security)
    #if the security level is < 1, we don't do the rest of the function
    if security < 1:
        finalCode = word_to_code
    #else, we crypte the password
    else:
        #we create the alphabet list
        list_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
                        "x", "y", "z"]
        new_list = []#we create a new list which will contains the encoded message
        list_keys= list(str(keys))
        index = len(list_keys)
        while index > 0:
            index -= 1
            list_keys[index] = int(list_keys[index])   
        n = 0
        for i in range(len(word_to_code)):
            for j in range(len(list_alphabet)):
                if word_to_code[i] == list_alphabet[j]:
                    for k in range(list_keys[n]):
                        j = j+1
                        if j >= 26:
                            j = 0 
                    n += 1
                    if n >=len(list_keys):
                        n = 0
                    new_list.append(list_alphabet[j])   
        new_list = "".join(new_list)
        #we crypte the crypted password again
        finalCode = code_cesar(new_list, keys, security - 1)
        
    return finalCode

def decode_cesar(word_to_decode, keys, security):
    """
    decrypte a string with the same key and the same security level
    """
    security = int(security)
    finalWord = ''
    if int(security) < 1:
        finalWord = word_to_decode
    else:
        #we create the alphabet list
        list_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
                        "x", "y", "z"]
        new_list = []#we create a new list which will contains the encoded message
        list_keys= list(str(keys))
        index = len(list_keys)
        while index > 0:
            index -= 1
            list_keys[index] = int(list_keys[index])   
        n = 0
        for i in range(len(word_to_decode)):
            for j in range(len(list_alphabet)):
                if word_to_decode[i] == list_alphabet[j]:
                    for k in range(list_keys[n]):
                        j = j-1
                        if j < 0:
                            j = 25
                    n += 1
                    if n >=len(list_keys):
                        n = 0
                    (new_list.append(list_alphabet[j]))        
        new_list = "".join(new_list)
        finalWord = decode_cesar(new_list,keys,security - 1)
    return finalWord