#  we found the 4 non trivial answers and the product of denominators is "100"


numList = [x for x in range(11,100) if x % 10 != 0]
wantedList = []

for n in range(0,len(numList)):
    for d in range(0,len(numList)):
        if d > n :
            numer = str(numList[n])
            denom = str(numList[d])

            if (numer[1] == denom[0]) or (numer[0] == denom[1]):
                if ((numList[n] / numList[d]) == (int(numer[0]) / int(denom[1]))) or ((numList[n] / numList[d]) == (int(numer[1]) / int(denom[0]))):
                    wantedList.append([numList[n], numList[d]])

print(wantedList)

