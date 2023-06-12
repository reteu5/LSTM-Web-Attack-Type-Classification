from loadpcap import open_tshark
from sys import argv
from os import listdir
from trace import Trace
import numpy as np


def main() :
    # USAGE: python3 main.py <pcapFile>
    if argv[1][-5:] != '.pcap' :
        print("[-] Please specify a pcap file.")
        exit(1)
    else :
        pcapFileName = argv[1]
    
    # Get a list of packets from a pcap file
    listofPackets = open_tshark(pcapFileName)
    print(listofPackets)


if __name__ == '__main__' :
    main()