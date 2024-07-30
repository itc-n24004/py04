d = [['0001', 'Male', 'Yamada', 'Tarou', 25, 'Tokyo'], ['0002', 'Male', 'Satou', 'Takeshi', 27, 'Kanagawa'], ['0003', 'Female', 'Tanaka', 'Yuko', 25, 'Saitama'], ['0004', 'Male', 'Suzuki', 'Ichirou', 35, 'Hokkaido']]
m_i = {}
for r in d:
    key = r[0]
    info = r[1:]
    m_i[key] = info

print('n', 'i', sep='\t')
for key, info in m_i.items():
    print(key, info)

