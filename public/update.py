import requests
import re

def getupdate(group):
    url = ['https://projectsekai.fandom.com/wiki/Category:Cover_Songs', 'https://projectsekai.fandom.com/wiki/Category:Commissioned_Songs']
    songs = []
    flag = True

    print("Fetching page...")

    for i in url:
        if group == 6 and flag:
            songs.append([0])
            flag = False

        else:
            a = []
            x = getdata(i, group)
            for i in x:
                i = i.replace("&#39;", "'")
                if i not in a and not i.startswith("File:") :
                    a.append(i)
            songs.append(a)
            
    return songs

def getdata(url, group):
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
        html_content = re.split('</p><div style="-webkit-column-count:2;column-count:2;">|</div><p class="mw-empty-elt"></p></div></div>', html_content)[:-1]
        pattern = r'title="([^"]+)"'
        x = re.findall(pattern, html_content[group])
        return x
    
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
