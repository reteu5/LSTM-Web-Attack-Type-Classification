from loadpcap import open_tshark
from loadtxt import load_txt
from sys import argv
from os import listdir
from trace import Trace
import numpy as np


def main() :
    # USAGE: python3 main.py <FilePath>
    if argv[1][-5:] == '.pcap' :
        pcapFileName = argv[1]
        # Get a list of packets from a pcap file
        listofPackets = open_tshark(pcapFileName)
        print(listofPackets)
    elif argv[1][-4:] == '.txt' :
        # Get a list of pcap files from a text file
        txtFileName = argv[1]
        listofPackets = load_txt(txtFileName)
        print(listofPackets)
    else :
        print("[-] Please specify a pcap/txt file.")
        exit(1)
    
if __name__ == '__main__' :
    main()