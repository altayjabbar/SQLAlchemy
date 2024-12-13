from models import Address,User,session

user1 = User(name = 'John',age = 54)
user2 = User(name = 'Frex', age = 23) 


address1 = Address(city='Baki', state = 'Feyzulla Qassimzade',zip_code = '100023')
address2 = Address(city='Gence', state='Nizami Rayonu', zip_code='200100')
address3 = Address(city='Sumqayit', state='Absheron', zip_code='300200')

user1.addresses.extend([address1,address2])
user2.addresses.append(address3)

session.add(user1)
session.add(user2)

session.commit()