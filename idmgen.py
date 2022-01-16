'''
IDM name generator v0.0001
Conceived from review of https://github.com/wjt/flitwemmmmm - was trying to see
how this worked and then said 'Welp, I can just do wacky string exercises in
Python.'

At some point would like to maybe jam this into a web front end. Should
also probably make this a function proper :)
'''

import random
t = ''
fh = open('data').readlines()

while t != 'q':
    # The line below is how many times the data list is iterated thru
    iterlist = [1, 2, 3]
    c = 0  # Reset counter

    t = input('Please enter a word - q to quit: ')

    if t != 'q':
        counter = int(input('Please enter iteration int: ') or 5)

    newarr, titlearr = [], []
    titlearr.append(t)  # Add the entered word to start of list
    for each in fh:
        # Fill newarr with all track titles in data file
        newarr.append(each.strip())

    while c < counter and t != 'q':
        # Loop either 1, 2 or 3 times (pending iteration int)
        for iters in range(0, random.choice(iterlist)):
            # Select a random song title from the list
            randtit = random.choice(newarr)
            # Append the song title to new title, index 1
            # through 10, skipping every other char
            titlearr.append(randtit[1:100:2])  # Was sliced as 1:10:2
        titlefin = ''.join(titlearr)  # Munge it all together
        print(titlefin)  # Print it
        titlearr = [t]  # Reset to originally entered word
        titlefin = ''  # Clear the title
        c += 1  # Increase the counter
