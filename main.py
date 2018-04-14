import random
import time

def ask_input(text=""):
    try:
        enteredNumber = (input(("Enter a 3-digit number:" if text == "" else text) + "\n>>>> "))
        startTime()

        if len(str(abs(enteredNumber))) != 3:
            raise ValueError
        else:
            return str(enteredNumber)

    except ValueError as valueE:
        return ask_input("You exactly need to provide 3-digit number:")
    except Exception as error:
        startTime()
        return ask_input("You did not entered number, please enter a number:")

def findForMatch(answer, guessNumber):
    cows = bulls = 0
    i = 0
    temp = list(guessNumber)

    for x in list(answer):
        if answer[i] == guessNumber[i]:
            cows += 1
        if x in temp:
            temp.remove(x)
            bulls += 1
        i += 1

    bulls -= cows

    return [cows,bulls]

def startTime():
    global startedTime

    if startedTime == 0:
        startedTime = time.time()

print "\nWelcome to cows and bulls game!\n"
print "We have a number and you need to guess it, we'll try to give some hints. You need to find out the actual number."
print "TIP: Number does not start with zero\n"

answer = str(random.randint(100, 999))
guessNumber = 0
attempts = 0
startedTime = 0

# print answer # Print answer (for debugging purpose)

while answer != guessNumber:
    # print guessNumber # for debugging purpose
    guessNumber = ask_input("" if guessNumber == 0 else " ")
    [cows, bulls] = findForMatch(answer, guessNumber)
    attempts += 1

    if cows != 3:
        print "You got", cows, "cows and", bulls, "bulls. Try again."

diff = int(time.time() - startedTime)
minutes, seconds = diff // 60, diff % 60
print "\nCongrats! You got all the cows correct in", attempts, "attempts and you took " + str(minutes).zfill(2) + ':' + str(seconds).zfill(2), 'seconds'

# Save user data for future statistics
with open('history.txt', 'a') as historyFile:
    historyFile.write(answer+'|'+str(attempts)+'|'+str(diff)+"\n")
