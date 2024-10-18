import os
from tabulate import tabulate

from scrapping import getupdate

groupname = {
    0:'Leo/need',
    1:'MORE MORE JUMP!',
    2:'Vivid BAD SQUAD',
    3:'Wonderlands x Showtime',
    4:'25-ji, Nightcord de.',
    5:'VIRTUAL SINGER & Other'
}

def printsong(group):
    x = getupdate(group)
    print()
    print(groupname[group])
    print()
    
    songs = [(i+1, j) for i, j in enumerate(x[0])]
    with open('cov_tmp.dat', 'w') as f:
        headers = ['No.', 'Cover Song Title']
        f.write(tabulate(songs, headers=headers, tablefmt='grid'))
        f.write('\n')
    with open('cov_tmp.dat', 'r') as f:
        cov = f.readlines()

    songs = [(i+1, j) for i, j in enumerate(x[1])]
    with open('com_tmp.dat', 'w') as f:
        headers = ['No.', 'Commissioned Song Title']
        f.write(tabulate(songs, headers=headers, tablefmt='grid'))
        f.write('\n')
    with open('com_tmp.dat', 'r') as f:
        com = f.readlines()

    os.remove('cov_tmp.dat')
    os.remove('com_tmp.dat')

    for i in range(max(len(com), len(cov))):
        if group == 5:
            data2 = com[i][:-1]
            print(f"{data2}")
        else:
            data1 = cov[i][:-1] if i < len(cov) else ""
            data2 = com[i][:-1] if i < len(com) else ""
            print(f"{data1}\t\t{data2}")