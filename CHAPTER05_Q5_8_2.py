d = [['01', '0001', 'Male', 'Yamada', 'Tarou', 25, 'Tokyo'], ['01', '0002', 'Male', 'Satou', 'Takeshi', 27, 'Kanagawa'], ['01', '0003', 'Female', 'Tanaka', 'Yuko', 25, 'Saitama'], ['02', '0001', 'Male', 'Smith', 'Mike', 22, 'NewJersey'], ['02', '0002', 'Male', 'Turner', 'Tom', 27, 'Kansas'], ['02', '0003', 'Male', 'Jackson', 'David', 22, 'Florida']]

m_i ={}

for r in d:
    key = (r[0], r[1])
    info = r[2:]
    m_i[key] =info

print('n', 'i', sep='\t')
for key, info in m_i.items():
    print(key, info)

