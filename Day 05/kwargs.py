def suma(num1, num2, *args, **kwargs):
    print(f"The first value is {num1}")
    print(f"The second value is {num2}")

    for n in args:
        print(f"arg = {n}")

    for key, value in kwargs.items():
        print(f"{key} = {value}")


suma(1, 2, 100, 10, 40, 120, x=3, y=1, z={'key': 'value'})

args = [10, 20, 30, 40, 50]
kwargs = {'x': 'hi', 'y': 12, 'z': {'key': 'value'}}
suma(3, 4, *args, **kwargs)