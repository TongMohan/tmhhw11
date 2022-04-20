def getBondPrice_Z(face, couponRate, times, yc):
    pv = 0
    for t,y in zip(times,yc):
        pv += couponRate*(1+y)**(-t)
    bondprice = face*(pv+(1+y)**(-t))
    return(bondprice)
