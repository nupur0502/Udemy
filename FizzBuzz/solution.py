def fizzBuzz(self, s):
        string = []
        for n in range(1, s + 1):
            if n % 3 == 0 and n % 5 == 0:
                string.append("FizzBuzz")
            elif n % 3 == 0:
                string.append("Fizz")
            elif n % 5 == 0:
                string.append("Buzz")
            else:
                string.append(n)

        return string