import json, http.client, urllib.request, subprocess
from pathlib import Path

YES = ("y", "ye", "yep", "yes", "yea", "yeah", "ofc", "alright")

def getSettings():
    settings = json.load(open('../settings.json'))
    return settings['version'], settings['mod-name']

def genFolder(s):
    try:
        Path(f'../{s}').mkdir(parents=True)
    except FileExistsError:
        pass

def linkExists(dom, path2file):
    conn = http.client.HTTPConnection(dom)
    conn.request('HEAD', path2file)
    response = conn.getresponse().status
    conn.close()
    return response in (200, 301, 302)

def getMappings(version):

    if not linkExists('raw.githubusercontent.com', f'/skyrising/mc-data/master/snapshot/{version}/client/mapping.tsrg'):
        print('[EDDxbot] Nope, bye! ^^')
        exit()
    
    s = input('[EDDxbot] They\'re! Do you want to download them? (y/n) ')

    if s.lower() not in YES:
        print('[EDDxbot] Ok then, bye! ^^')
        exit()
    
    downloadMappings(version)

def downloadMappings(version):
    try:
        print(f'Downloading mappings.tsrg...', end=' ')
        f = urllib.request.urlopen(f'https://raw.githubusercontent.com/skyrising/mc-data/master/snapshot/{version}/client/mapping.tsrg')

        with open(f'../mc-code/{version}/mappings.tsrg', 'wb') as local_file:
            local_file.write(f.read())
            print('Done!')

    except urllib.request.HTTPError():
        print('\n[EDDxbot] HTTP Error, bye! ^^')
    except urllib.request.URLError():
        print('\n[EDDxbot] URL Error, bye! ^^')

# java -jar cfr_0_132.jar *.class --outputdir out --comments false
def cmd(args):
    subprocess.run(args, shell=True)

