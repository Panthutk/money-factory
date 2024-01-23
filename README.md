## Factory Method Assignment

1. Read [factory method pattern](https://refactoring.guru/design-patterns/factory-method) on refactoring.guru.

2. Python Code Example: <https://en.wikipedia.org/wiki/Factory_method_pattern>


## Instructions

You will add these files to the `wallet` project from week 1.

In order to distinguish versions of your code, please add a TAG named `lab2` to your wallet code:

```
cd lab1-yourname
git tag -a -m "Wallet code for Lab 2" lab2
git push --tags
```

Copy these files to your wallet directory:
```
factory_demo.py                Demo code you can run in Python
money_factory.py               Starter code for this lab
test_money_factory.py          Unit tests for your money_factory
```


## Implement Concrete MoneyFactories for Thai and Malaysian Money

Complete the code in `money_factory.py`.

In `MoneyFactory` write:

- `MoneyFactory.get_instance(country_code)` - *class method* creates a single instance of each concrete money factory. One instance for each country code.  Create the instances the first time it is requested.  The parameter is the standard 2-character country code, in uppercase.

In `MalayMoneyFactory` and `ThaiMoneyFactory` implement these methods:

- `create_cash(value)` create and return some currency (Coin or Banknote)
- `get_currency()` return the string name of the currency (not the country code)

## Domain Knowledge

The Malaysian currency is "Ringgit". Since 2012 Malaysia has these denominations for money:

- Coins 0.05, 0.10, 0.20, 0.50 Ringgit (colloquially called *Sen*)
- Banknotes 1, 5, 10, 50, and 100 Ringgit. Other values were discontinued in 2012.

The Thai currency is 'Baht' (of course). The current values in production are:

- Coins 0.25, 0.50, 1, 2, 5, and 10 Baht
- Banknotes 20, 50, 100, 500, and 1000 Baht
