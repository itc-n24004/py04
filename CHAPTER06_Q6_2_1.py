class cylinder:
    pi = 3.14

    def __init__(self, r=1, h=1):
        self.r = float(r)
        self.h = float(h)

    def c_b_a(self):
        pi = cylinder.pi
        ra = self.r
        return pi * ra * ra
    def c_s_a(self):
        pi = cylinder.pi
        ra = self.r
        he = self.h
        return 2 * pi * ra * he
    def c_su_a(self):
        c = self.c_b_a()
        s = self.c_s_a()
        return 2 * c + s
    def c_v(self):
        c = self.c_b_a()
        he = self.h
        return c * he
    def s_r(self):
        ra = self.r
        he = self.h
        S = self.c_su_a()
        V = self.c_v()
        print('半径:{}, 高さ:{}, 表面積:{}, 体積:{}'.format(ra, he, S, V))

c1 = cylinder()
c1.s_r()
c2 = cylinder(2., 1.)
c2.s_r()
c3 = cylinder(2., 3.)
c3.s_r()
c4 = cylinder(1., 3.)
c4.s_r()

