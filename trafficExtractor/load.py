from subprocess import Popen, PIPE

def trim_tshark(tshark_data):
    decoded_string = tshark_data.decode()
    solePackets = decoded_string.split('\n')[:-1]
    return solePackets