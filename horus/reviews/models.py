from django.db import models

from horus.service.models import Bank, Hotel, Restaurant
from horus.users.models import User

# Create your models here.


class Review(models.Model):
    rate = models.IntegerField()
    comment = models.TextField(max_length=180)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"rate:{self.rate} from:{self.user}"

    class Meta:
        abstract = True


class ReviewBank(Review):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__() + f", to bank: {self.bank}"

    @classmethod
    def get_by_bank(cls, bank_id):
        return cls.objects.filter(bank=bank_id)


class ReviewHotel(Review):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__() + f", to hotel: {self.hotel}"

    @classmethod
    def get_by_hotel(cls, hotel_id):
        return cls.objects.filter(hotel=hotel_id)


class ReviewRestaurant(Review):
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__() + f", to Restaurant: {self.Restaurant}"

    @classmethod
    def get_by_Restaurant(cls, Restaurant_id):
        return cls.objects.filter(Restaurant=Restaurant_id)
