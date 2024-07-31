class Person:
    def __init__ (self, 
            name = '',
            nationality = '',
            birth = '',
            address = ''):
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.address = address


    def show_attributes(self):
        print("名前:", self.name)
        print("国籍:", self.nationality)
        print("生年月日:", self.birth)
        print("出身地:", self.address)


AuthorofAttackonTitan = Person('諫山創', '日本', '１９８９年８月２９日', '大分県日田市大山町')

AuthorofAttackonTitan.show_attributes()
