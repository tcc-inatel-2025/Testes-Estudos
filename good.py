"""Simple script to demonstrate adding two numbers with proper style."""


def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    result = a + b
    return result


def main() -> None:
    """Run an example using add_numbers."""
    x = 5
    y = 10
    result = add_numbers(x, y)
    print(f"The result is: {result}")


if __name__ == "__main__":
    main()
