import edd

def main():
    version, mod = edd.getSettings()
    #edd.genFolder('mc-libs')
    edd.genFolder(f'mc-code/{version}/{mod}')

if __name__ == "__main__":
    main()