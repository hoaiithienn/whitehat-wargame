import hashlib

flag = str('w31l_c0m3_t0_w4rg4m3_2O21')
flag = flag.encode('utf-8')

h = hashlib.sha1(flag)

print(f'sha1({flag}) \n = {h.hexdigest() }')
