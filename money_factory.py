import abc
from cash import *
from cash import Money


class MoneyFactory(abc.ABC):
    """Abstract base class for factory class that creates money."""

    instances = {}  # dict: country_code -> country money factory

    @classmethod
    def get_instance(cls, country_code: str) -> 'MoneyFactory':
        """Get a singleton money factory for a given currency.

        :param country_code: 2-letter code for the country
        :returns: a MoneyFactory for that country.
        """
        if country_code not in cls.instances:
            # Create a new instance of the appropriate subclass
            if country_code == "MY":
                cls.instances[country_code] = MalayMoneyFactory()
            elif country_code == "TH":
                cls.instances[country_code] = ThaiMoneyFactory()
            else:
                raise ValueError(f"Unknown country code {country_code}")
        return cls.instances[country_code]

    @abc.abstractmethod
    def get_currency(self) -> str:
        """Return the name of the currency created by this factory."""
        raise NotImplementedError("not implemented")

    @abc.abstractmethod
    def create_cash(self, value: int | float) -> Money:
        """Create money in a country's own currency.

        :param value: the value of money item to create
        :returns: Money having the requested value, if the value is valid
        :raises ValueError: if the value is not valid for the
                       country's own currency.
        """
        raise NotImplementedError("not implemented")

    def __str__(self):
        """Describe this money factory."""
        name = type(self).__name__
        # strip off "MoneyFactory" suffix
        if name.endswith('MoneyFactory'):
            name = name[:-12]
            return f"Factory for {name} money"
        return name


class MalayMoneyFactory(MoneyFactory):
    def __init__(self):
        self.instances['MY'] = self

    def create_cash(self, value) -> Money:
        if value in [0.01, 0.1, 0.2, 0.5]:
            return Coin(value, "Ringgit")
        elif value in [1, 5, 10, 20, 50, 100]:
            return Banknote(value, "Ringgit")
        raise ValueError(f"{value} is not valid for Malaysian currency")

    def get_currency(self) -> str:
        return "Ringgit"


class ThaiMoneyFactory(MoneyFactory):
    def __init__(self):
        self.instances['TH'] = self

    def create_cash(self, value) -> Money:
        if value in [0.25, 0.5, 1, 2, 5, 10]:
            return Coin(value, "Baht")
        elif value in [20, 50, 100, 500, 1000]:
            return Banknote(value, "Baht")
        raise ValueError(f"{value} is not valid for Thai currency")

    def get_currency(self) -> str:
        return "Baht"
