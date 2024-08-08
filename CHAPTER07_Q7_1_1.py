name_age = {'hatsune': 16, 'satou': 22, 'yonezu': 33}

def dict_info(dict_tbl, key):
    try:
        return dict_tbl[key]
    except:
        return 'key is not found'

print(dict_info(name_age, 'satou'))
print(dict_info(name_age, 'yamada'))
