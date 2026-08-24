from smartphone import Smartphone


catalog = [
    Smartphone(brand="IPhone", model="IPhone 17", phone_number="+79991112233"),
    Smartphone(brand="Samsung", model="Galaxy", phone_number="+79994445566"),
    Smartphone(brand="Nokia", model="Nokia N70", phone_number="+79997778899"),
    Smartphone(brand="Moto", model="Moto 202", phone_number="+79990001122"),
    Smartphone(brand="Xiaomi", model="Xiaomi 17", phone_number="+79993334455"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
