def data_reverse(data):
    bytes_list = [data[i:i+8] for i in range(0, len(data)+1, 8)]
    reversed = bytes_list[::-1]
    reversed_data = [bit for byte in reversed for bit in byte]
    
    print(reversed_data)
    return reversed_data

data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1])