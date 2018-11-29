import edd, os.path, sys
from pathlib import Path 



def main(rmp):
    version, mod = edd.getSettings()
    
    print(f'[EDDxbot] Checking if {version} is at .minecraft/versions...', end=' ')
    versionjar = Path(f'~/AppData/Roaming/.minecraft/versions/{version}/{version}.jar').expanduser()

    if not versionjar.exists():
        print('\n[EDDxbot] Nope, remember to play that version at least once before running this script')
        print('[EDDxbot] Bye! ^^')
        exit()
    else:
        print('Done!')

    if rmp:
        remap(version, versionjar.__str__())
    
    decompile(version, rmp, versionjar.__str__())

def decompile(version, remap, default_versionjar):
    print('==[CFR]==')

    versionjar = f'../mc-code/{version}/mapped-{version}.jar'

    if not remap:
        versionjar = default_versionjar

    cfr = 'libs/cfr_0_132.jar'
    outdir = f'../mc-code/{version}/mapped-src'
    edd.genFolder(outdir)

    command = [
        'java','-jar', cfr,
        versionjar,
        '--outputdir', outdir,
        '--caseinsensitivefs','true', '--comments'
        ]
        
    edd.cmd(command)
    print('[EDDxbot] Done! :D')

def remap(version, versionjar):

    if os.path.isfile(f'../mc-code/{version}/mapped-{version}.jar'):
        print(f'[EDDxbot] Oh, so there\'s a mapped-{version}.jar...')
        print('[EDDxbot] Remap skipped')
        return

    print(f'[EDDxbot] Looking in mc-code/{version} for "mappings.tsrg"...', end=' ')

    if not os.path.isfile(f'../mc-code/{version}/mappings.tsrg'):
        print('\n[EDDxbot] Mappings not found')
        print(f'[EDDxbot] Checking if {version} mappings are available on github...')
        edd.getMappings(version)
    else:
        print('Done!')

    
    print(f'[EDDxbot] Remapping {version}.jar...\n==[SpecialSource]==')

    specialsource = 'libs/SpecialSource-1.8.6.jar'
    outjar = f'../mc-code/{version}/mapped-{version}.jar'
    mappings = f'../mc-code/{version}/mappings.tsrg'

    command = [
        'java','-jar', specialsource,
        '--in-jar', versionjar,
        '--out-jar', outjar,
        '--srg-in', mappings
        ]
    edd.cmd(command)
    print('[EDDxbot] Done!')

if __name__ == "__main__":

    rmp = False
    if len(sys.argv) == 2:
        rmp = sys.argv[1] == '--remap'
    main(rmp)

