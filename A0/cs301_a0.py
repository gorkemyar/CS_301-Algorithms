N = 2


def wPrefers(prefer, w, m, m1):
    for i in range(N):

        if (prefer[w][i] == m1):
            return True
        if (prefer[w][i] == m):
            return False


def stableMarriage(WomenpreferMen, MenpreferWomen):

    wPartner = [-1 for i in range(N)]

    mFree = [False for i in range(N)]

    freeCount = N

    while (freeCount > 0):
        m = 0
        while (m < N):
            if (mFree[m] == False):
                break
            m += 1
        i = 0

        while i < N and mFree[m] == False:
            w = MenpreferWomen[m][i]
            if (wPartner[w] == -1):
                wPartner[w] = m
                mFree[m] = True
                freeCount -= 1

            else:
                m1 = wPartner[w]
                if (wPrefers(WomenpreferMen, w, m, m1) == False):
                    wPartner[w] = m
                    mFree[m] = True
                    mFree[m1] = False
            i += 1

    print("Woman ", " Man")
    for i in range(N):
        print(i, "\t", wPartner[i])


WomenpreferMen = [[0, 1], [0, 1]]

MenpreferWomen = [[0, 1], [0, 1]]
stableMarriage(WomenpreferMen, MenpreferWomen)
