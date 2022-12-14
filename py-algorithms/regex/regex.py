"""Regex practice"""
import re

# match = re.search(pattern, str)
# re.sub(pat, replacement, str) -- returns new string with all replacements,
# a, X, 9, < -- ordinary characters just match themselves exactly. The meta-characters which do not match themselves because they have special meanings are: . ^ $ * + ? { [ ] \ | ( ) (details below)
# . (a period) -- matches any single character except newline '\n'
# \w -- (lowercase w) matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_]. Note that although "word" is the mnemonic for this, it only matches a single word char, not a whole word. \W (upper case W) matches any non-word character.
# \b -- boundary between word and non-word
# \s -- (lowercase s) matches a single whitespace character -- space, newline, return, tab, form [ \n\r\t\f]. \S (upper case S) matches any non-whitespace character.
# \t, \n, \r -- tab, newline, return
# \d -- decimal digit [0-9] (some older regex utilities do not support \d, but they all support \w and \s)
# ^ = start, $ = end -- match the start or end of the string
# \ -- inhibit the "specialness" of a character. So, for example, use \. to match a period or \\ to match a slash. If you are unsure if a character has special meaning, such as '@', you can try putting a slash in front of it, \@. If its not a valid escape sequence, like \c, your python program will halt with an error.
# 001 A very simple solution:

strn = 'an example word:cat!!'
match = re.search(r'\sword:\w\w\w', strn)
if match:
    print(match.group())
match = re.search(r'iii', 'piiig')
if match:
    print(match.group())
match = re.search(r'\d\w\d', 'pi1i2ig')
if match:
    print(match.group())
match = re.search(r'\d+\w\d', 'pi12i2ig')
if match:
    print(match.group())
match = re.search(r'^\d+\w\d', 'pi12i2ig')
if match:
    print(match.group())
strn = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', strn)
if match:
    print(match.group()) 
strn = 'purple al.ice-b@goo-gle.com monkey dishwasher'
match = re.search(r'[\w.-]+@[\w.-]+', strn)
if match:
    print(match.group())  
strn = 'purple al.123ice-b@goo-gle.com monkey dishwasher'
match = re.search(r'[\w.-]+@[\w.-]+', strn)
if match:
    print(match.group())
strn = 'purple al.123ice-b@goo-gle.com monkey dishwasher'
match = re.search(r'[0-9]+', strn)
if match:
    print(match.group())  
strn = 'purple al.123ice-b@goo-gle.com monkey dishwasher'
match = re.findall('g', strn)
if match:
    print(match)  
strn = 'purple al.123ice-b@goo-gle.com monkey dishwasher'
match = re.search(r'[a-z,\s.0-9]+', strn)
if match:
    print(match.group()) 

eml = 'Content-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\nTo: Recipient <recipient@example.com>\nFrom: Author <author@example.com>\nSubject: Simple test message\n\nThis is the body of the message.'

match = re.search('Subject:\s(.+?)\n', eml)
if match:
    print(match.group(1))

match = re.search('\n\n(.+?)\.', eml)
if match:
    print(match.group(1))

print('==== rplc ====')
strn = 'purple <= >= [] | --al.123ice-b@goo-gle.com monkey dishwasher'
strn = re.sub('[<,>,=,-]', '', strn)
print(strn)

# split at comma or dot
inp = "100,000,000.000"
res = re.split(r"[\.,]", inp)
print('\n'.join(map(str, res)))


strings = ['abcNdgM', 'abcdg', 'MrtyNNgMM']

for s in strings:
    # Repeat the cycles of transforming M/N with previous or subsequent characters:
    while True:
        s_new = re.sub(r'N.', '', re.sub(r'(.)M', r'\1\1', s))
        # print('s_new:', s_new)
        if s == s_new:
            break
        s = s_new
    # Remove any remaining Ms and Ns:
    s = re.sub(r'[MN]+', '', s)
    print(s)


inp = 'Today is the greatest day ever'
l = inp.split()
helper = []
for i in l:
    helper.append(len(i))

greatest = max(helper)
#print(greatest)

for i in l:
    if len(i) == greatest:
        print(i)

l = inp.split()
l_dict = dict()
for i in l:
    for j in l:
        if i.count(j) > 1:
            l_dict[i] = i.count(j)
        if len(l_dict) != 0:
            for i in l_dict:
                print(i)
            
            break
