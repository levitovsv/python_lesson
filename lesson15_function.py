def create_record (name,tel,address):
    """" create record"""
    record ={
        'name': name,
        'tel':  tel,
        'address': address
    }
    return record


user1= create_record("Vasya","0506427337","Dnipro")
user2= create_record("Petya","0502427337","Kiev")
print(user1)
print (user2)

def person_award(award,*person):
    for i in person:
        print ("Awawrd "+award+" nagrazdaetsya "+ i )

person_award("За отвагу","Vasya","Petyya")