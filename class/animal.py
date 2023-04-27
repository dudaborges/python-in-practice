class Animal:
    def __init__(self, name, race, age):
        self.name = name
        self.race = race
        self.age = age

    def makeSoundDog(self):
        print("Au au au au au")

    def makeSoundCat(self):
        print("Miau miau miau miau")


dog = Animal('Jully', 'Pug', '7 anos')
print(vars(dog))
print(dog.name)
dog.makeSoundDog()

cat = Animal('Bibi', 'Siamês', '3 anos')
print(vars(cat))
print(cat.name)
cat.makeSoundCat()

