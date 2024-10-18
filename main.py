import sys

import printing as printing

def printheader():
    print('''
                      -- Project SEKAI Song Scrapper --
               List your favorite Cover and Commissioned Songs
          
                          Song list are taken from:
      https://projectsekai.fandom.com/wiki/Category:Commissioned_Songs
          https://projectsekai.fandom.com/wiki/Category:Cover_Songs
    ''')

def manual():
    printheader()
    print('''      
    Usage :
    \tpython3 main.py [option]
          
    Option :
    \t-s --songs [group]     display songs from a specific group then exit
    \t-h --help              display this message then exit
          
    Group :
    \tl    leoneed
    \tm    moremorejump
    \tv    vividbadsquad
    \tw    wonderxshowtime
    \tn    niigo
    \to    others''')
    exit(1)

initial = {
    'l':1, 'leoneed':1,
    'm':2, 'moremorejump':2,
    'v':3, 'vividbadsquad':3,
    'w':4, 'wonderxshowtime':4,
    'n':5, 'niigo':5,
    'o':6, 'others':6
}

if len(sys.argv) < 2 or len(sys.argv) > 3:
    manual()
    exit(1)

option = sys.argv[1]

if len(sys.argv) == 2:
    
    if option in ['-r', '--rank', '-s', '--songs']:
        print('Missing group.')
        exit(1)

    else:
        manual()
        exit(1)

elif len(sys.argv) == 3:
    try:
        group = initial[sys.argv[2]]
    except:
        print('Unknown group.')
        exit(1)


    if option in ['-s', '--songs']:
        printheader()
        printing.printsong(group)
        exit(1)
    
    else:
        manual()
        exit(1)
