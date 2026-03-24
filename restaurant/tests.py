from django.test import TestCase
from .models import Booking

class BookingTest(TestCase):
    def test_create_booking(self):
        booking = Booking.objects.create(
            first_name="Test",
            reservation_date="2026-03-25",
            reservation_slot=10
        )
        self.assertEqual(booking.first_name, "Test")