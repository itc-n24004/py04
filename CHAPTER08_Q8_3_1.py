import collections
data = 'あああああいえぢじぺん'
count = collections.Counter(data)
res_dict = collections.defaultdict(list)
for ch, cnt in count.items():
    res_dict[cnt].append(ch)
print(res_dict[1])
