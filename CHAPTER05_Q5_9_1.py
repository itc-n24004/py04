mountain_in_japan = {'fuji': 3776, 'kitadake': 3193, 'okuhodakadake': 3190, 'dummy': 0}
mountain_in_japan_s = sorted(mountain_in_japan.items(), key=lambda a: a[1], reverse=True)
print(mountain_in_japan_s)
