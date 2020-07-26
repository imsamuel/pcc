"""A collection of functions for working with cities."""

from cities import city_country


def test_city_country():
    """Does a simple city and country pair work?"""
    santiago_chile = city_country("Santiago", "Chile")
    assert santiago_chile == "Santiago, Chile"


def test_city_country_population():
    """Can I include a population argument?"""
    santiago_chile = city_country("Santiago", "Chile", 5000000)
    assert santiago_chile == "Santiago, Chile - population 5000000"
