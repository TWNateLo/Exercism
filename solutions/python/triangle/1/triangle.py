def equilateral(sides):
    if sides[0] > 0 and sides[1] > 0 and sides[2] > 0 and sides[0]+sides[1] >= sides[2] and sides[0] == sides[1] == sides[2]:
        return(True)
    else:
        return(False)

def isosceles(sides):
    sides = sorted(sides)
    if sum(sorted(sides)[:2]) >= sorted(sides)[2] and all(s > 0 for s in sides) and len(set(sides)) <= 2:
       return(True) 
    else:
        return(False)


def scalene(sides):
    sides = sorted(sides)
    if sum(sides[:2]) >= sides[2] and all(s > 0 for s in sides) and len(set(sides)) == 3:
       return(True) 
    else:
        return(False)