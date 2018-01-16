import fizzbuzz


def test_fizzbuzz_0():
    assert fizzbuzz.fizzbuzz(15) == "FizzBuzz"


def test_fizzbuzz_3():
    assert fizzbuzz.fizzbuzz(3) == "Fizz"


def test_fizzbuzz_5():
    assert fizzbuzz.fizzbuzz(5) == "Buzz"


def test_fizzbuzz_4():
    assert fizzbuzz.fizzbuzz(4) == "4"
