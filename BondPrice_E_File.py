def getBondPrice_E(face, couponRate, m, yc):
    pv = 0
    for i,y in enumerate(yc):
        pv += couponRate*(1+y)**(-i-1)
    bondprice = face*(pv+(1+y)**(-m))
    return(bondprice)
