def binom_coeff(n, k, memoization_dict={}):
    if k == 0 or k == n:
        return 1
    
    if (n, k) in memoization_dict:
        return memoization_dict[(n, k)]
    
    coeff = binom_coeff(n - 1, k - 1, memoization_dict) + binom_coeff(n - 1, k, memoization_dict)
    memoization_dict[(n, k)] = coeff

    return coeff

n, k = int(input()), int(input())

print(binom_coeff(n, k))
