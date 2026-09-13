def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

    print("\nInput data is '25'")
    try:
        print(f"Temperature is now {input_temperature('25')}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("\nInput data is 'abc'")
    try:
        print(f"Temperature is now {input_temperature('abc')}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("\nInput data is '100'")
    try:
        print(f"Temperature is now {input_temperature('100')}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("\nInput data is '-50'")
    try:
        print(f"Temperature is now {input_temperature('-50')}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()