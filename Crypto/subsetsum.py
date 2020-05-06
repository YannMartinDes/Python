def subsetSum(L, k) :
    if k == 0 : return True

    for i in range(len(L)) :
        if subsetSum (L[:i] + L[i+1:], k - L[i]) :
            print(L[i]) ; return True
    return False
