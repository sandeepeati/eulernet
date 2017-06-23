def pe44():
    ps = set()
    i = 2
    while True:
        i += 1
        s = (3*i*i - i) // 2
        for Pj in ps:
            if s-Pj in ps and s-2*Pj in ps: 
                return s-2*Pj
        ps.add(s)

print(pe44())


euler_emergency_key = '1142930-3xpy9sdyQ1KD5cLQhitLbbBDVKHSwbMpEa9uwTrJ'
