import pytest

from market_place.models import StorageBox
from booking.models import Booking, Profile


@pytest.fixture
def user_profile(db):
    data = {
            "first_name": "Denis",
            "last_name": "Techer",
            "email": "valentinjerome@tele2.fr",
            "date_of_birth": "1923-01-26"
        }
    return Profile.objects.create(**data)

@pytest.fixture
def storage_box(db, user_profile):
    box_data = {
    "storage_type": "",
    "title": "Valoir propos plante billet. Image blanc tromper longtemps préparer. Fidèle asseoir arme disposer.",
    "description": "Inquiétude traverser passé voir journée entourer combien fenêtre. Avec nom donner trace. Calme décider rapport prouver beaux satisfaire faux. Épaule jusque haut marche. Autre savoir président cheveu prière secrétaire elle. Coeur bois te large sûr absence traverser danger. Côté fête dehors rêver discuter. Joie prochain puisque muet. Ministre voir secret sourd. Sac juste chair étouffer compagnie bureau. Est traverser intéresser envie voici. Discussion plante curieux demi bon fort.",
    "surface": "22",
    "street_number": "9",
    "route": "rue de Bonnet",
    "postal_code": "40682",
    "monthly_price": "12",
    "city": "Saint Clémence"
}
    return StorageBox.objects.create(
        owner=user_profile,
        **box_data,
    )

BOOKING_START_DATE = "2023-08-23"
BOOKING_END_DATE = "2023-08-30"
AVAILABLE_START_DATE = "2024-08-23"
AVAILABLE_END_DATE = "2024-08-30"

@pytest.fixture
def booking(db, storage_box, user_profile):
    return Booking.objects.create(
        tenant=user_profile,
        storage_box=storage_box,
        start_date=BOOKING_START_DATE,
        end_date=BOOKING_END_DATE,
    )


def test_available_on_different_period(booking):
    storage_box = booking.storage_box
    assert storage_box.available_on_period(AVAILABLE_START_DATE, AVAILABLE_END_DATE)
def test_not_available_on_booked_period(booking):
    storage_box = booking.storage_box
    assert not storage_box.available_on_period(BOOKING_START_DATE, BOOKING_END_DATE)
    
def test_not_available_on_start_of_booked_period(booking):
    storage_box = booking.storage_box
    assert not storage_box.available_on_period(BOOKING_START_DATE, AVAILABLE_START_DATE)
    
def test_not_available_on_end_of_booked_period(booking):
    storage_box = booking.storage_box
    assert not storage_box.available_on_period(BOOKING_END_DATE, AVAILABLE_END_DATE)
