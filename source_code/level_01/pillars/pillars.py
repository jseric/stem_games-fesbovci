import requests
import json
import time

def check_pillar(val):
    pillars = []
    for buffer_val in val:
        if (buffer_val == '{') or (buffer_val == '[') or (buffer_val == '('):
            pillars.append(buffer_val)
        elif (buffer_val == '}') or (buffer_val == ']') or (buffer_val == ')'):
            if len(pillars) == 0:
                return 'F'
        elif ( (pillars[-1] == '{') and (buffer_val == '}') ) or ( (pillars[-1] == '[') and (buffer_val == ']') ) or ( (pillars[-1] == '(') and (buffer_val == ')') ):
                pillars.pop()
            else:
                return 'F'
    if len(pillars) > 0:
        return 'F'
    return 'T'

while True:
    try:
        # Delay for 1 minute (60 seconds).
        time.sleep(1)

        get_req = requests.get('https://tech.stemgames.hr/api/competitive/v1/4292bf95-9793-48b5-9576-daa6d2685e20', headers = {"Authorization": "token gHSKVUBMlVjQ96RNjn2wyueBB0QWM7Lz"})
        input_data = check_pillar(get_req.json()['input_data'])
        url = 'https://tech.stemgames.hr/api/competitive/v1/4292bf95-9793-48b5-9576-daa6d2685e20/'+get_req.json()['submission_id']

        payload = {
            'data': input_data
        }
        # Adding empty header as parameters are being sent in payload
        headers = {
            "Authorization": "token gHSKVUBMlVjQ96RNjn2wyueBB0QWM7Lz",
            "Content-Type":"text/plain"
        }

        r = requests.post(url, data = input_data, headers = headers)
        print(r.content)
    except:
        pass
