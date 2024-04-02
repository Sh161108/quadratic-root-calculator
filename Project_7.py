import math

def quadratic(a, b, c):
    """
    Calculate the roots of a quadratic equation.

    Args:
    a (float): Coefficient of x^2
    b (float): Coefficient of x
    c (float): Constant term

    Returns:
    tuple: Roots of the quadratic equation
    """
    if a == 0:
        print("This is not a quadratic equation.")
        return None

    Discriminant = b**2 - 4 * a * c

    if Discriminant < 0:
        print("No real roots")
        x1 = (-b + math.sqrt(abs(Discriminant)) * complex(0, 1)) / (2 * a)
        x2 = (-b - math.sqrt(abs(Discriminant)) * complex(0, 1)) / (2 * a)
        return x1, x2
    
    elif Discriminant == 0:
        print("Real and equal roots")
        x1 = (-b + math.sqrt(Discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(Discriminant)) / (2 * a)
        return x1, x2
    else:
        print("Real and distinct roots")
        sqrt_discriminant = math.sqrt(Discriminant)
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (-b - sqrt_discriminant) / (2 * a)
        return x1, x2

def main():
    a = float(input("Give the value of a: "))
    b = float(input("Give the value of b: "))
    c = float(input("Give the value of c: "))

    print(f"{a}x^2 + {b}x + {c} = 0")
    ask = input("Is this your equation: ")

    if ask.lower() != "yes":
        quit()
    else:
        print("Ok, these are the roots of the following equation:")
        roots = quadratic(a, b, c)
        if roots:
            print(f"x1 = {roots[0]}, x2 = {roots[1]}")

if __name__ == "__main__":
    main()
