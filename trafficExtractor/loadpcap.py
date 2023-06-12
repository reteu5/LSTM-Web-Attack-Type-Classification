from subprocess import Popen, PIPE

def trim_tshark(tshark_data):
    decoded_string = tshark_data.decode()
    
    # 비어있는 줄과 무관하게 context 살아있는 버전
    #solePackets = decoded_string.split('\n')[:-1]

    # 비어있는 줄이 있다면 해당 줄은 건너뛰는 코드
    solePackets = [line for line in decoded_string.split('\n') if line]
    
    return solePackets

# get HTTP GET method URI queries
def open_tshark (pcap = None):
    try:
        tshark_output = Popen(['tshark', '-r', pcap, '-T', 'fields', '-e', 'http.request.uri.query'], stdout=PIPE)
        # Read every traffic from a single pcap file
        wild_output = tshark_output.stdout.read()
        # Save as a list format / line by line
        packetlist = trim_tshark(wild_output)

        return packetlist
    except FileNotFoundError: print("[-] tshark command not found.")
    except Exception as e: print(f"[-] An error occured : {e}")


# tshark -r <pcap> -T fields -e http.request.uri.query
# tshark -r <pcap> -Y http.request.uri.query | wc -l