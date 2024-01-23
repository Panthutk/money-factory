"""Factories for creating different currencies."""
import abc
from cash import *


class MoneyFactory(abc.ABC):
    """Abstract base class for factory class that creates money."""

    # Class variable that keeps track of factory instances that
    # have been created.
    # We need only one instance of each type of money factory,
    # e.g. one ThaiMoneyFactory, one MalaiMoneyFactory
    # So, after you create it the first time, add it to the 'instances'
    # dictionary and return it next time.

    instances = {}   # dict: country_code -> country money factory

    @abc.abstractmethod
    def get_currency(self) -> str:
        """Return the name of the currency created by this factory."""
        # Each subclass should implement this method.
        raise NotImplementedError("not implemented")

    @abc.abstractmethod
    def create_cash(self, value: int|float) -> Money:
        """Create money in a country's own currency.

        :param value: the value of money item to create
        :returns: Money having the requested value, if the value is valid
        :raises ValueError: if the value is not valid for the
                 country's own currency.
        """
        # Each subclass should implement this method.
        raise NotImplementedError("not implemented")

    @classmethod
    def get_instance(cls, country_code: str) -> 'MoneyFactory':
        """Get a singleton money factory for a given currency.
        
        :param country_code: 2-letter code for the country
        :returns: a MoneyFactory for that country.
        """
        #TODO
        raise ValueError(f"Unknown country code {country_code}")
        
    def __str__(self):
        """Describe this money factory."""
        name = type(self).__name__
        # strip off "MoneyFactory" suffix
        if name.endswith('MoneyFactory'):
            name = name[:-12]
            return f"Factory for {name} money"
        return name


class MalayMoneyFactory(MoneyFactory):
    """Factory for Malaysian money.
    
    Valid values for Malay money are
    Coins: TODO document this
    Banknotes: TODO document this
    """

    def __init__(self):
        pass

    def create_cash(self, value) -> Money:
        """Return a Money object of the requested value.

        :param value: a valid value for Malaysian currency.
        :raises ValueError: if value is not valid for this currency
        """
        raise ValueError(f"{value} is not valid for Malaysian currency")

    def get_currency(self) -> str:
        """Get the string name of the currency."""
        return ""


class ThaiMoneyFactory(MoneyFactory):
    """Factory for Thai money.
    
    Valid values for Thai money are
    Coins: TODO document this
    Banknotes: TODO document this
    """
    # Use MalayMoneyFactory as an example
    pass        

