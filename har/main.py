import json

filename = 'data.har'
with open(filename) as f:
    response = json.loads(f.read())['log']['entries']
    for res in response:
        try:
            subjects = json.loads(res['response']['content']['text'])['dsRecMattList']
            for subject in subjects:
                print(subject['SBJ_NO'])
                print(subject['SCH_YEAR'])
                print(subject['SMT_NM'])
                print(subject['CDT'])
                print(subject['CMP_DIV_NM'])
                print(subject['CULT_ARA_NM'])
        except:
            print('error')
