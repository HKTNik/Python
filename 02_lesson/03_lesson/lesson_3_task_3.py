from address import Address
from mailing import Mailing


address1 = Address("123456", "Москва", "Брусилова", "27", "67")
address2 = Address("789012", "Казань", "Ленина", "1", "4")

trip = Mailing(to_address=address1, from_address=address2, cost=9, track="Air")

print(f"Отправление {trip.track} из {trip.from_address} в {trip.to_address}."
      f"Стоимость {trip.cost} рублей.")
