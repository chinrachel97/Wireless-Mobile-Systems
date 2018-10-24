# tp1 should be lower than tp2
def maximize(t1, t2):
    tpMinArr = []
    abVals = []
    tp1 = t1 * 2
    tp2 = t2 * 2
    a = 0.5
    b = 0.5

    for i in range(50):
        iPercent = (i+1)/100.0
        ai = a + iPercent
        bi = b - iPercent
        tp1Aug = tp1*(ai)
        tp2Aug = tp2*(bi)
        print(str(tp1)+"*"+str(ai)+"="+str(tp1Aug)+
            "    "+str(tp2)+"*"+str(bi)+"="+str(tp2Aug))
        minVal = abs(tp1Aug - tp2Aug)
        tpMinArr.append(minVal)
        abVals.append((ai*2, bi*2))

    bestMin = min(tpMinArr)
    abValsIndex = tpMinArr.index(bestMin)

    return (abVals[abValsIndex])

bestVals = maximize((1.218*(10**8)), (1.393*(10**8)))

throughputA = (1.218*(10**8))
throughputB = (1.393*(10**8))

print("testing: ")
print(throughputA*bestVals[0])
print(throughputB*bestVals[1])

print("ratio: ")
print(bestVals[0]/2, bestVals[1]/2)
