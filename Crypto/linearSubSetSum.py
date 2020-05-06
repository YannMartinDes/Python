def linearSubsetSum (L, k) : # que si L est super-croissante !
    res = []
    s=k
    
    for i in range(len(L)-1,-1,-1) :
        if s >= L[i] :
            res.append(L[i])
            s = s - L[i]
            
    if s == 0 :
        return (res,k)
    else :
        return (False,k)
