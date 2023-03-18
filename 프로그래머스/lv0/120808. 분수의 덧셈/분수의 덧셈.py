def lcm(num1, num2):
    num = min([num1,num2])
    target = num
    while True:
        if not target % num1 and not target % num2:
            return target
        target += num
        

def gcd(num1, num2):
    target = min([num1, num2])
    while True:
        if target ==1 or ( not num1 % target and not num2 % target):
            return target
        target -= 1

        
def solution(numer1, denom1, numer2, denom2):
    _lcm = lcm(denom1, denom2)
    _numer = numer1*(_lcm//denom1) + numer2*(_lcm//denom2)
    _gcd = gcd(_numer, _lcm)
    return [_numer//_gcd, _lcm//_gcd]