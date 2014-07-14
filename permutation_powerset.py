## Permutations

def insert(lst, i, elm):
    return lst[0:i] + [elm] + lst[i:]

def permutations(lst):
    if lst == []:
        return [[]]

    ps = permutations(lst[1:])
    return [insert(p,i,lst[0]) for p in ps for i in range(0, len(p)+1)]

print permutations([1,2,3])


############################################### 


## Permutations in order in PiCat

perm([]) = [[]].
perm(Lst) = Ps =>
	Ps = [[E|P] : E in Lst, P in perm(Lst.delete(E)))]
		
		
############################################### 

## Power Set

def power_set(set):
    if set == []:
        return [[]]

    P1 = power_set(set[1:])
    return P1+[[set[0]] + s for s in P1]

print (power_set([1,2,3]))
