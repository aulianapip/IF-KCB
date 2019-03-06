awal = [0, 0, 0, 0]
tujuan = [1, 1, 1, 1]
 
stack = []
stack.append(awal)

def nextState(state):
    if state == tujuan: return False
    petani = state[0]

    for i, s in enumerate(state):
        if s == petani:
            tryState = makeState(state, i)
            if testState(tryState) and isUnique(tryState):
                stack.append(tryState)
                return True
            
    return False       

def makeState(s, i):
    t = []
    for x in s: t.append(x)

    t[0] = 1 if t[0] == 0 else 0

    if t[0] == 0:
        if not testState(t):
            t[i] = 1 if t[i] == 0 else 0
    else:
        t[i] = 1 if t[i] == 0 else 0
    return t

def testState(s):
    if s[1] == s[2] and s[0] != s[1]: return False
    if s[2] == s[3] and s[0] != s[2]: return False
    return True

def isUnique(s):
    if s in stack: return False
    return True

while nextState(stack[-1]): pass

print "Puzzle : Petani, Harimau, Ayam, Gabah"

print "\nKeadaan awal"
print "Daerah awal : ", tujuan
print "Daerah tujuan : ", awal

print "\nTujuan"
print "Daerah awal : ", awal
print "Daerah tujuan : ", tujuan

print "\nSolusi"
for i, x in enumerate(stack): print i, x