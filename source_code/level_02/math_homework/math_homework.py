import requests
import json
import time
import math

while True:
    try:
        time.sleep(1)
        get_req = requests.get('https://tech.stemgames.hr/api/competitive/v1/98bd6b3a-1c22-4cea-9665-17a74b25af0b', headers = {"Authorization": "token gHSKVUBMlVjQ96RNjn2wyueBB0QWM7Lz"})
        entire_input = get_req.json()['input']

        input_val = entire_input.split("\n")
        row1 = input_val[0].split(" ")
        row2 = input_val[1].split(" ")
        N = int(row1[0])
        M = int(row1[1])
        A = int(row2[0])
        B = int(row2[1])

        ctr = 0

        while M != N:
            b_price = (2 * B) / N
            a_price = A

            if (b_price <= a_price) and (N/2 >= M):
                N = math.floor(N/2)
                ctr += B
            else:
                N--
                ctr += A

        url = 'https://tech.stemgames.hr/api/competitive/v1/98bd6b3a-1c22-4cea-9665-17a74b25af0b/' + get_req.json()['submission_id']

        headers = {
            "Authorization": "token gHSKVUBMlVjQ96RNjn2wyueBB0QWM7Lz",
            "Content-Type":"text/plain"
        }
        reply = requests.post(url, data = str(ctr), headers = headers)
        print(reply.content)

    except:
        pass
