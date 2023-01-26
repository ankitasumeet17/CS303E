#score is a value between 0.0 and 1.0

score = input('Enter score between 0.0 and 1.0: ')
sval = float(score)

if sval >= 0.9:
    print('A')
elif sval >= 0.8:
    print('B')
elif sval >= 0.7:
    print('C')
elif sval >= 0.6:
    print('D')
elif sval < 0.6:
    print('F')
else:
    print('Out of range')
