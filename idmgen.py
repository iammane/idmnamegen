# IDM name generator v1 - 1/16/2022
# Conceived from review of https://github.com/wjt/flitwemmmmm - was trying to see
# how this worked and then said 'Welp, I can just do wacky string exercises in
# Python.'

# At some point would like to maybe jam this into a web front end.
# Changelog:
# 1/16/2022 - Refactored into a function rather than a straight through
# script. Could still be cleaner but maybe another day.


import random

def runTheIDM(t, newarr, counter):
    c = 0
    iterlist = [1, 2, 3]
    titlearr = []
    titlearr.append(t)
    while c < counter:
        # Loop either 1, 2 or 3 times - this keeps resulting phrase short
        for _ in range(0, random.choice(iterlist)):
            # Select a random song title from the list
            randtit = random.choice(newarr)
            # Append the song title to new title, index 1
            # through 100, skipping every other char
            titlearr.append(randtit[1:100:2])
        titlefin = ''.join(titlearr)  # Munge it all together
        print(titlefin)  # Print it
        titlearr = [t]  # Reset to originally entered word
        titlefin = ''  # Clear the title
        c += 1  # Increase the counter

if __name__ == '__main__':
    t = ''
    fh = open('data').readlines()
    newarr = []
    for each in fh:
        newarr.append(each.strip())
    while t.lower() != 'q':
        t = input('Please enter a word - q to quit: ')
        if t.lower() == 'q':
            break
        else:
            counter = int(input('Please enter an iteration integer: ') or 5)
        runTheIDM(t, newarr, counter)