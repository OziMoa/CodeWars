"""DESCRIPTION:
In this kata we mix some tasty fruit juice. We can add some components with certain amounts. Sometimes we pour out a bit of our juice. Then we want to find out, which concentrations our fruit juice has.

Example:

You take an empty jar for your juice
Whenever the jar is empty, the concentrations are always 0
Now you add 200 units of apple juice
And then you add 200 units of banana juice
Now the concentration of apple juice is 0.5 (50%)
Then you pour out 200 units
The concentration of apple juice is still 50%
Then you add 200 units of apple juice again
Now the concentration of apple juice is 0.75, while the concentration of banana juice is only 0.25 (300 units apple juice + 100 units banana juice)
Complete the functions in order to provide this functionality. The test code for the example above can be found in the test fixture.
"""

class Jar():
    def __init__(self):
        # your code here
        self.total = 0
        self.mixture = {}
        pass

    def add(self, amount, kind):
        # your code here
        if kind not in self.mixture:
            self.mixture[kind] = amount

        else:
            self.mixture.update({kind: self.mixture[kind] + amount})
        print(self.mixture[kind])
        self.total += amount
        pass

    def pour_out(self, amount):
        # your code here
        for i in self.mixture:
            self.mixture.update({i: self.mixture[i] - self.get_concentration(i)*amount})
        self.total -= amount
        pass

    def get_total_amount(self):
        # your code here
        return self.total
        pass

    def get_concentration(self, kind):
        # your code here
        try:
            self.mixture[kind] / self.total
        except KeyError:
            return 0
        return self.mixture[kind] / self.total
