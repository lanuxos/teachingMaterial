# while loop
# single line statement
# while init_var < 10: init_var += 1

init_var = 0
while init_var < 10:    # sentinel controlled repetition value
    print(init_var)
    init_var += 1
# False condition
else:
    print('Final while value:', init_var)

# while loop with break statement
init_break = 0
while init_break < 10:
    print('break at 7: ', init_break)
    if init_break == 7:
        break
    init_break += 1

# while loop with continue statement
init_continue = 0
while init_continue < 10:
    print('continue at 6', init_continue)
    if init_continue == 6:
        init_continue += 2
        continue
    init_continue += 1

# while loop with pass statement
init_pass = 0
while init_pass < 10:
    print('pass at 5', init_pass)
    if init_pass == 5:
        pass
        print('nothing happen here')
    init_pass += 1

# # en/decrypted script
# i = 0
# encode_string_list = []
# encode_message = input('Please input your text >_ ')
# encoded_phrase = []
# while i < len(encode_message):
#     ordinary_code = ord(encode_message[i]) # return unicode form of character
#     # print(ordinary_code)
#     # encrypted_func = 33 + (((123 - 33) / 10)) * ordinary_code
#     encrypted_func = 123 * ordinary_code
#     # print(encrypted_func)
#     encode_string_list.append(encrypted_func)
#     encoded_phrase.append(chr(encrypted_func))
#     i += 1
# print('\nEncrypted string list: ', encode_string_list)
# print('\nEncoded phrase: ', ''.join(encoded_phrase))
# # decrypted script
# j = 0
# decode_message = ""
# while j < len(encode_string_list):
#     decode_func = encode_string_list[j]
#     # print(decode_func)
#     # code_function = (decode_func - 33) * (10 / (123-33))
#     code_function = decode_func / 123
#     # print(code_function)
#     temp_text = chr(int(code_function)) # encode number -> character
#     # print(temp_text)
#     decode_message = decode_message + str(temp_text)
#     j += 1
    
# print('\nDecrypted text: ', decode_message)