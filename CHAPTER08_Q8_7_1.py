import json

name_list = {
        'tanaka': {
            '年齢':20,
            '血液型':'A',
            '性別':'男性'
        },

        'satou': {
            '年齢':19,
            '血液型':'O',
            '性別':'女性'
        },

        'suzuki': {
            '年齢':20,
            '血液型':'AB',
            '性別':'男性'
        }
}
with open('name_list.json', 'w')as f1:
    json.dump(name_list, f1)

with open('name_list.json', 'r') as f2:
    name_list_l = json.load(f2)

for key, val in name_list_l.items():
    print(key, val)
