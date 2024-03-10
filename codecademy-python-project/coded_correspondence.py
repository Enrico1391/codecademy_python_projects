# Coded Correspondence/Cryptography Puzzles (coded_correspondence.py)
# Use Python to decipher and encode messages

# Declare variable for alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Declare variable for encoded message in Caesar Cipher
encoded_Caesar_message_1 = '\
xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh.\
 muhu oek qrbu je tusetu yj? y xefu ie!\
 iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'

# Define function to decode the Caesar message
def decode_Caesar(message=encoded_Caesar_message_1, offset=10):
    decoded_Caesar = ''
    for c in message:
        if c in alphabet:
            find_decode_index = (alphabet.find(c) + offset)  - len(alphabet)
            decoded_Caesar += alphabet[find_decode_index]
        else:
            decoded_Caesar += c
    return decoded_Caesar

print(f'\nCaesar Decodification No.1:\
\n{decode_Caesar().title()}\n')

# Declare variable for a message to be encoded in Caesar Cipher
my_message_Caesar = '\
Hello, my friend. I received your message.\
 Decoding it, was fun and challenging!! I\'ve learned a lot.'

# Define function to encode the Caesar message
def encode_Caesar(message=my_message_Caesar, offset=10):
    encoded_message = ''
    for c in message:
        if c in alphabet:
            find_encode_index = (alphabet.find(c) - offset)  % len(alphabet)
            encoded_message += alphabet[find_encode_index]
        else:
            encoded_message += c
    return encoded_message

print(f'Caesar Encoding No.1:\n{encode_Caesar()}\n')

# Decode two new encoded Caesar messages
encoded_Caesar_message_2 = 'jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.'

print(f'Caesar Decodification No.2:\
\n{decode_Caesar(encoded_Caesar_message_2, 10).title()}\n')

encoded_Caesar_message_3 = '\
bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!'

print(f'Caesar Decodification No.3:\
\n{decode_Caesar(encoded_Caesar_message_3, 14).title()}\n')

# Brute force an encoded Caesar message with no offset
encoded_Caesar_message_4 = '\
vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx.\
 px\'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.'

for i in range(1, 26):
    brute_decode = decode_Caesar(encoded_Caesar_message_4, i)
    if brute_decode.count('e') > 10:
        print(f'Caesar Decodification No.4:\
        \nThe correct Brute Force Attempt is No.{i}:\
        \n{brute_decode.title()}\n')
        break

# Declare variables for encoded message in Vigenère Cipher and its keyword
encoded_Vigenère_message = '\
txm srom vkda gl lzlgzr qpdb? fepb ejac!\
 ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!'
keyword = 'friends'

# Define function to find the Vigenère message to be decoded comparative string
def msg_decode_comparative(message=encoded_Vigenère_message, key=keyword):
    comp_string = ''
    counter = 0
    for c in message:
        if c in alphabet:
            comp_string += key[counter % len(key)]
            counter += 1
        else:
            comp_string += c
    return comp_string

decode_cmp_string = msg_decode_comparative()
print(f'The Comparative String is:\n{decode_cmp_string}\n')

# Define function to decode the Vigenère message
def decode_Vigenère(message=encoded_Vigenère_message, key=decode_cmp_string):
    decoded_Vigenère = ''
    for c1, c2 in zip (message, key):
        if c1 in alphabet and c2 in alphabet:
            find_decode_index = (alphabet.find(c1) + alphabet.find(c2))\
                                              % len(alphabet)
            decoded_Vigenère += alphabet[find_decode_index]
        else:
            decoded_Vigenère += c1
    return decoded_Vigenère

print(f'Vigenère Decodification:\n{decode_Vigenère().title()}\n')

# Declare variable for a message to be encoded in Vigenère
my_message_Vigenère = '\
thanks for these cryptographic challenges. it was a tough\
 but rewarding experience. talk to you soon.'
my_keyword = 'goodbye'

# Define function to find the Vigenère message to be encoded comparative string
def msg_encode_comparative(message=my_message_Vigenère, key=my_keyword):
    comp_string = ''
    counter = 0
    for c in message:
        if c in alphabet:
            comp_string += key[counter % len(key)]
            counter += 1
        else:
            comp_string += c
    return comp_string

encode_cmp_string = msg_encode_comparative()

# Define function to encode the Vigenère message
def encode_my_Vigenère(message=my_message_Vigenère, key=encode_cmp_string):
    encoded_Vigenère = ''
    for c1, c2 in zip (message, key):
        if c1 in alphabet and c2 in alphabet:
            find_encode_index = (alphabet.find(c1) - alphabet.find(c2)) % len(alphabet)
            encoded_Vigenère += alphabet[find_encode_index]
        else:
            encoded_Vigenère += c1
    return encoded_Vigenère

print(f'Vigenère Encoding:\n{encode_my_Vigenère()}\n')
