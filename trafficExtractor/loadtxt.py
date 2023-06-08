
def main() :
    file = open("../dataset/xss_1484.txt", 'r')
    lines = file.readlines()
    # debug
    print(lines)
    file.close()


if __name__ == "__main__" :
    main()
