from sys import argv

def main() :
    # USAGE : python3 loadtxt.py [ original / encoded ] <txtFile>
    if len(argv) != 3 :
        print("[i] USAGE : python3 loadtxt.py [ original / encoded ] <txtFile>")
        exit(1)
    if argv[2][-4:] != '.txt' :
        print("[-] Please specify a txt file.")
        exit(1)
    else : file = open(argv[2], 'r')
        
    if argv[1] == "original" : load_txt(file)
    elif argv[1] == "encoded" : load_encoded_txt(file)
    else :
        print("[i] USAGE : python3 loadtxt.py [ original / encoded ] <txtFile>")
        exit(1)


def load_txt(fp) :
    lines = fp.readlines()
    # debug
    print(lines)
    fp.close()

def load_encoded_txt(fp) :    
    string = fp.read()
    lines = string.split("%0A")
    # debug
    print(lines)
    fp.close()

if __name__ == "__main__" :
    main()
