class nigiri:
    c = "にぎり"
    to = "ねた"
    ba = "しゃり"

    def show_attributes(self):
        print("top:{}, base:{}, category:{}".format(self.to, self.ba, self.c))


class katsuo(nigiri):
    to = "かつお"
    top = "生姜とねぎ"
    price = 100

    def show_attributes(self):
        super().show_attributes()
        print("price:{}円".format(self.price))
        print("topping:{}".format(self.top))
k1 = katsuo()
k1.show_attributes()
