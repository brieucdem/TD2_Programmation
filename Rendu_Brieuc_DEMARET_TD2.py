import math

class Fraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
        if denom == 0:
            raise ValueError("Denominator cannot be zero.")

    def display(self):
        return f"My fraction is: {self.num}/{self.denom}"

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def simplify(self):
        common_divisor = self.gcd(self.num, self.denom)
        self.num //= common_divisor
        self.denom //= common_divisor

    def add(self, other):
        denom_add = self.denom * other.denom
        num_add = self.num * other.denom + other.num * self.denom
        result = Fraction(num_add, denom_add)
        result.simplify()
        return result

    def mult(self, other):
        num_mult = self.num * other.num
        denom_mult = self.denom * other.denom
        result = Fraction(num_mult, denom_mult)
        result.simplify()
        return result

    @staticmethod
    def harmonic_series(n):
        H = Fraction(0, 1)
        for i in range(1, n + 1):
            H = H.add(Fraction(1, i))
        return H

    @staticmethod
    def leibniz_term(n):
        if n % 2 == 0:
            return Fraction(0, 1)
        else:
            return Fraction(1, n) if n % 4 == 1 else Fraction(-1, n)

    @staticmethod
    def leibniz_series(n):
        L = Fraction(0, 1)
        for i in range(1, n + 1):
            L = L.add(Fraction.leibniz_term(i))
        return L

if __name__ == '__main__':
    # Test cases with assertions
    try:
        # Test case 1: Creating a fraction with denominator 0
        invalid_fraction = Fraction(3, 0)
    except ValueError as e:
        assert str(e) == "Denominator cannot be zero."
        print("Test case 1 passed.")

    # Test case 2: Addition of fractions
    fra1 = Fraction(3, 4)
    fra2 = Fraction(1, 2)
    result = fra1.add(fra2)
    assert result.num == 5 and result.denom == 4, "Addition failed."
    print("Test case 2 passed.")

    # Test case 3: Multiplication of fractions
    result = fra1.mult(fra2)
    assert result.num == 3 and result.denom == 8, "Multiplication failed."
    print("Test case 3 passed.")

    # Test case 4: Simplify fractions
    fra3 = Fraction(6, 8)  # 6/8 can be simplified to 3/4
    fra3.simplify()
    assert fra3.num == 3 and fra3.denom == 4, "Simplification failed."
    print("Test case 4 passed.")

    '''
    Tests réalisés avec n=1000 par souci de puissance de calcul (trop long). Si on veut tester pour n=10000 comme demandé, il suffit de remplacer la valeur, la tolérence est arbitrairement fixée à 1e-3 pour vérifier le code
    '''

    # Test case 5: Harmonic series
    H_1000 = Fraction.harmonic_series(1000)
    expected_harmonic = math.log(1000) + 0.57721566490153286060651209
    assert math.isclose(H_1000.num / H_1000.denom, expected_harmonic, rel_tol=1e-3), "Harmonic series approximation incorrect."
    print("Test case 5 passed.")

    # Test case 6: Leibniz series
    L_1000 = Fraction.leibniz_series(1000)
    # Calculate the sum of the series
    sum_leibniz = L_1000.num / L_1000.denom
    # Calculate the expected value using the Leibniz formula
    expected_leibniz = math.pi / 4
    # Assert that the calculated sum is close to the expected value
    assert math.isclose(sum_leibniz, expected_leibniz, rel_tol=1e-3), "Leibniz series incorrect for n = 1000."
    print("Test case 6 passed.")

    print("All test cases passed successfully.")

