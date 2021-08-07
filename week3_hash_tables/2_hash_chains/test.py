def _hash_func(s):
    bucket_count = 5
    _multiplier = 263
    _prime = 1000000007
    ans = 0
    for c in reversed(s):
        ans = (ans * _multiplier + ord(c)) % _prime
    return ans, ans % bucket_count

def hash_funct(s):
    bucket_count = 5
    _multiplier = 263
    _prime = 1000000007
    ans = 0
    i=0
    for c in s:
        ans = ans + ord(c)*_multiplier**i
        i+=1
    ans = ans % _prime
    return ans, ans % bucket_count

inpt = 'a'
while inpt != 'c':
    inpt = input()
    print(_hash_func(inpt))
    print(hash_funct(inpt))
