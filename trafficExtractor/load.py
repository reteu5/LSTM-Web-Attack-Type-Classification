from subprocess import Popen, PIPE

def trim_tshark(tshark_data):
    decoded_string = tshark_data.decode()
    # 비어있는 줄이 있다면 해당 줄은 건너뛰는 코드 추가

    solePackets = decoded_string.split('\n')[:-1]
    return solePackets

def open_tshark (pcap = None):
    # get HTTP GET method URI queries
    tshark_output = Popen(['tshark', '-r', pcap, '-T', 'fields', '-e', 'http.request.uri.query'], stdout=PIPE)
    # Save every traffic from a single pcap file
    wild_output = tshark_output.stdout.read()
    # Save as a list format / line by line
    packetlist = trim_tshark(wild_output)
    
    return packetlist


# tshark -r <pcap> -T fields -e http.request.uri.query
# tshark -r <pcap> -Y http.request.uri.query | wc -l