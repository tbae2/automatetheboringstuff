#! python3
# mclip.py practice multi clip board program
# never worked with system clipboard before 

import sys,pyperclip



textResponses = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}


if len(sys.argv) < 2:
    print('Usage: python mclip.py[keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # fist command line argument is the keyphrase

if keyphrase in textResponses:
    pyperclip.copy(textResponses[keyphrase])
    print('Text for ' + keyphrase + ' copied to keyboard')
    print(f'Text for {keyphrase} copied to keyboard')
else:
    print(f'There is no value for {keyphrase}')