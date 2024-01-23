"""Demonstrate creating money using a factory method."""
from money_factory import MoneyFactory


def run(factory: MoneyFactory):
    """Interactively ask for some values and create money."""

    print(f"The currency is '{factory.get_currency()}'", "\n")
    print("Input value(s) of money to create, separated by space.")
    print("Example: 1 100 0.5\n")

    while True:
        response = input("Values to create (empty line to quit): ").strip()
        if not response:
            return
        print("Creating cash:")
        for arg in response.split():
            value = float(arg)
            try:
                cash = factory.create_cash(value)
                print(cash)
            except Exception as e:
                print("Error:", str(e))

def get_country_code() -> str:
    print("Specify a 2-character country code for the currency to use.")
    print("For example, TH is country code for Thailand.")
    ccode = ""
    while len(ccode) != 2:
        ccode = input("Please input 2-character country code: ")
        ccode = ccode.strip()
    return ccode.upper()


if __name__ == '__main__':
    # Get the country code and create a factory for that country
    country_code = get_country_code()
    money_factory = MoneyFactory.get_instance(country_code)
    run(money_factory)
