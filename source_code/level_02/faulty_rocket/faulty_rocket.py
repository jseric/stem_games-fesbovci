import requests
import json
import time

while True:
    try:
        get_req = requests.get('https://tech.stemgames.hr/api/competitive/v1/fec8307a-488d-4f24-88b5-97f47db80207', headers = {"Authorization": "token gHSKVUBMlVjQ96RNjn2wyueBB0QWM7Lz"})
        input_all = get_req.json()['input']

        input_val = input_all.split("\n")
        expression = input_val[0]
        input_val.pop(0)

        values = [0] * 26
        for val in input_val:
            values[ord(val[0]) - 97] = int(input_val[input_val.index(val)][2:], base = 2)

        result = values[ord(expression[0])-97]
        expression = expression[1:]

        for character in expression:
            if character == '|':
                temp = character
            elif character == '&':
                temp = character
            elif character == '^':
                temp = character
            else:
                var = values[ord(character)-97]
                if temp == '|':
                    result = result | var
                elif temp == '&':
                    result = result & var
                elif temp == '^':
                    result = result ^ var

        url = 'https://tech.stemgames.hr/api/competitive/v1/fec8307a-488d-4f24-88b5-97f47db80207/' + get_req.json()['submission_id']

        headers = {
            "Authorization": "token gHSKVUBMlVjQ96RNjn2wyueBB0QWM7Lz",
            "Content-Type": "text/plain"
        }
        reply = requests.post(url, data = "{:032b}".format(result), headers = headers)
        print(reply.content)

    except:
        pass
