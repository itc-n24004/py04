def list_average(a):
    try:
        return sum(a)/len(a)
    except:
        print('list_length:', len(a))
        return None

print(list_average([2.9, 3.5, 2,3]))
print(list_average([]))
