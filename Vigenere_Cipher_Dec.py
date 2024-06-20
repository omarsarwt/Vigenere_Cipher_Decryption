# Created by JOYBOY
# Prepared Dictionary for alphabet and its Index alpha_nums => a:0, b:1 and so on ... / nums_alpha => 0:a , 1:b and so on ...
alpha_nums = {chr(i): i - 97 for i in range(97, 123)}
nums_alpha = {i: chr(i + 97) for i in range(26)}


original_dec = input("Enter your Encryption cipher : ")
NF_enc = original_dec.lower()
keyword = input("Enter your keyword : ").lower()
enc, dec, junk = '', '', []

# Isolate junk data from alphabet data 
for i in range(len(NF_enc)):
	if 'a' <= NF_enc[i] <= 'z' :
		enc+= NF_enc[i]
	else:
		junk.append(i)
		junk.append(NF_enc[i])

# Repeat keyword same length of input
repeat_kw = keyword*(round(len(enc) / len(keyword)))
N_repeat_kw = repeat_kw[:len(enc)]

# Decrypt Message
for i in range(len(enc)):
	enc_char, kw_char = enc[i], N_repeat_kw[i]
	if 'a' <= enc_char <= 'z' and 'a' <= kw_char <= 'z' :
		diff = alpha_nums[enc_char] - alpha_nums[kw_char]
		if diff < 0 :
			diff += 26
		dec += nums_alpha[diff]
	else:
		dec+=enc[i]

# Print Cleartext message all in LowerCase
Final_dec = list(dec)
for i in range(0,len(junk),2):
	Final_dec.insert( junk[i], junk[i+1])
Final_dec = ''.join(Final_dec)
print("[+] Decrypted Cipher : ", Final_dec)

# Print Cleartext message in matched pattern with Original Input
M_pattern = ''
for i in range (len(Final_dec)):
	if 'A' <= original_dec[i] <= 'Z' :
		M_pattern+=Final_dec[i].upper()
	else:
		M_pattern+=Final_dec[i]
print("[+] Decrypted Cipher Matched Pattern : ", M_pattern)
