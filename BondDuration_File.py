def getBondDuration(y, face, couponRate, m, ppy = 1):
    bp = 0
    bpt = 0
    cf = face*couponRate
    for i in range(1, m):
        temp = cf*(1+y)**(-i)
        bp += temp
        bpt += temp*i
    ten = cf*(1+y)**(-m)+face*(1+y)**(-m)
    bp += ten
    bpt += ten*m
    return(bpt/bp)
