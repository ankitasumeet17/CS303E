# CS 303E Quiz 3D
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Fancy Functions
def followsRule(num):
    import math

    if math.sqrt(num) == int(math.sqrt(num)):
        perfSqrt = True
    else:
        perfSqrt = False

    return perfSqrt


def rangeOfNums(lower, upper):

    count = 0
    for i in range(lower, upper+1):
        if followsRule(i) == True:
            count = count + 1

    return count


# Problem 2: Phone Class
class Phone:
    def __init__(self, brand, volume=5, toggleMute="unmuted"):
        self.__brand = brand
        self.__volume = volume
        self.__toggleMute = toggleMute

    def toggleMute(self):
        if self.__toggleMute == not self.__toggleMute

        if self.__toggleMute == "muted":
            self.__toggleMute = "unmuted"

    def increaseVolume(self):
        if self.__volume < 10:
            self.__volume = self.__volume + 1

    def decreaseVolume(self):
        if self.__volume > 0:
            self.__volume = self.__volume - 1

    def __str__(self):
        if self.__toggleMute == "unmuted":
            return "This " + str(self.__brand) + " phone is currently at " + str(self.__volume) + " volume."
        if self.__toggleMute == "muted":
            return "This " + str(self.__brand) + " phone is currently " + str(self.__toggleMute) + " ."
