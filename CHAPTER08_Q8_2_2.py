import pathlib
p = pathlib.Path('.')
for pt in p.glob('a*'):
    if pf.is_dir():
        print(pf)
