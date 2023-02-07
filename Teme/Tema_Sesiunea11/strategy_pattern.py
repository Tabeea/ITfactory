'''
Beharioral pattern - Strategy
            Strategy is a behavioral design pattern that lets you define a family of algorithms,
            put each of them into a separate class, and make their objects interchangeable.

Usage examples:
Application which should be able to choose a sorting algorithm at runtime (Bubble sort, QuickSort and so on).
When implementing the shopping site: the user adds items to the basket and by the end on checkout,
the user can choose the payment strategy in runtime: PayPal, Credit Card and so on.
In a game where we can have different characters and each character can have multiple weapons to attack but at a
time can use only one weapon. The method attack() will have different implementation depends on which weapon is being used.
Useful when a client may need to apply a different compression algorithms

PROS:
    - You can swap algorithms used inside an object at runtime.
    - You can isolate the implementation details of an algorithm from the code that uses it.
    - You can replace inheritance with composition.
    - Open/Closed Principle. You can introduce new strategies without having to change the context.

CONS:
    - If you only have a couple of algorithms and they rarely change, there’s no real reason to overcomplicate
     the program with new classes and interfaces that come along with the pattern.
    - Clients must be aware of the differences between strategies to be able to select a proper one.
    - A lot of modern programming languages have functional type support that lets you implement different
    versions of an algorithm inside a set of anonymous functions. Then you could use these functions exactly
    as you’d have used the strategy objects, but without bloating your code with extra classes and interfaces.
'''

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context():
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        # ...

        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

        # ...


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def do_algorithm(self, data: List):
        pass


"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.

    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()


