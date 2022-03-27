class Human:
    def __init__(self, name_, gender_, age_, occupation_, country_):
        self.name = name_
        self.gender = gender_
        self.age = age_
        self.occupation = occupation_
        self.country = country_

    def do_work(self):
        if self.occupation == 'Tennis Player':
            print(self.name, " is a tennis player.")
        elif self.occupation == 'Actor':
           print(self.name, " is an actor.")
        else:
            print(self.name, "'s occupation is other.")

    def speaks(self):
        print(self.name, " says How are you?")

tom = Human("Tom", "Male", "53", "Actor", "USA")
tom.do_work()
tom.speaks()
