# Задание 8.1.2
# Вам необходимо создать класс на основе одной из 3-х придуманных вами на уроке абстракции. Прописать поля и методы, а
# также создать не менее 2х экземпляров данного класса которые будут эти методы вызывать.

class Human:
    def __init__(self, full_name=None, birth_date=None, phone_number=None, city=None, country=None, home_address=None):
        self.full_name = full_name
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.city = city
        self.country = country
        self.home_address = home_address

    def get_full_name(self):
        print(self.full_name)

    def get_birth_date(self):
        print(self.birth_date)

    def get_phone_number(self):
        print(self.phone_number)

    def get_city(self):
        print(self.city)

    def get_country(self):
        print(self.country)

    def get_home_address(self):
        print(self.home_address)


human1 = Human('Evgeniy Koshlakov', '21.05.1980', '+79*********', 'Yaroslavl',
               'Russia', 'Some address')
human2 = Human('Ivan Petrov', '01.01.1999', '+79*********', 'Moscow',
               'Russia', 'Some address')
human3 = Human('Ivan Petrov', '01.01.1999', '+79*********')
human3.city = 'Ivanovo'

print(human1.full_name)
print(human2.full_name)
print(human3.city)
