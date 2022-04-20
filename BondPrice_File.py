def getBondPrice(y, face, couponRate, m, ppy=1):
    pv = 0
    for i in range(1,ppy*m+1):
        pv += (couponRate/ppy)*(1+(y/ppy))**(-i)
    bondprice = face*(pv+(1+(y/ppy))**(-m*ppy))
    return(bondprice)
