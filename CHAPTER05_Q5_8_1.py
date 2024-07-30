c_c ={'Iceland': {'code': '354', 'capital': 'Reykjavik'}, 'Ireland': {'code': '353', 'capital': 'Dublin'}, 'Azerbaidjan': {'code': '994', 'capital': 'Baku'}}
def g_k(x):
    if not isinstance(x, dict):
        return x
    m_str = ''
    for key, val in x.items():
        m_str += (' ' + str(key) + ' ' + g_k(val))
    return m_str

for key1, val1 in c_c.items():
    print(key1, g_k(val1))

