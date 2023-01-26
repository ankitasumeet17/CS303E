# WORKSPACE

def removeAdjacentDuplicates(lst):
    i = 1
    while i < len(lst):
        if lst[i] == lst[i-1]:
            lst.pop(i)
            i -= 1
        i += 1
    return lst

#-------------------------------------------------------------------------------

def stringWithStars(string):
    lastStr = string[-1]

    if not string:
        return 0
    elif string[0] == lastStr:
        return str(string[0])
    else:
        return string[0] + '*' + stringWithStars(string[1:])

#-------------------------------------------------------------------------------

def removeNegatives(lst):
    if not lst:
        return []
    elif lst[0] >= 0:
        return [lst[0]] + removeNegatives(lst[1:])
    else:
        return removeNegatives(lst[1:])

#-------------------------------------------------------------------------------

def collatzLength(num):
    count = 0

    if num == 1:
        return count + 1
    elif num%2 == 0:
        num = num // 2
        count += 1
        return collatzLength(num) + count
    else:
        num = 3*num + 1
        count += 1
        return collatzLength(num) + count


def collatzLength(num):
    if num == 1:
        return 1
    elif num%2 == 0:
        num = num // 2
        return 1 + collatzLength(num)
    else:
        num = 3*num + 1
        return 1 + collatzLength(num)

#-------------------------------------------------------------------------------

def countUpperLower(string):
    if not string:
        return (0,0)
    else:
        x = 0
        y = 0

        if 97 <= ord(string[0]) <= 122:
            y += 1
        elif 65 <= ord(string[0]) <= 90:
            x += 1
        elif len(string) == 1:
            return (x,y)

        return (x + countUpperLower(string[1:])[0] , y + countUpperLower(string[1:])[1])

#-------------------------------------------------------------------------------
