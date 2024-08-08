dog_r = {1: 'チワワ', 2: 'コーギー', 3: '柴犬', 4: 'シベリアンハスキー', 5: 'シェパード'}

class MyDictKeyError(Exception):
    def __init__(self, key):
        self.key = key
    def __str__(self):
        return '登録されていません {0}'.format(self.key)

def g_d_v(dict_tbl, key):
    if key not in dict_tbl:
        raise MyDictKeyError(key)
    else:
        return dict_tdl[key]

my_dict = {1: 'チワワ', 2: 'コーギー', 3: '柴犬'}

try:
    my_dog = g_d_v(my_dict, 5)
except MyDictKeyError as err:
    print(err)
    key = err.args[0]
    my_dict[key] = dog_r[key]
    print(key, dog_r[key], 'を my_dictに追加しました')
    my_dog = dog_r[key]

print(my_dog)
