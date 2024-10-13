from Calculator import *
from fractions import Fraction

class ScientificCalculator(Calculator):
    def execute(self, a: float, b: float = 0) -> Fraction:
        if self._operation is None:
            raise ValueError("No operation set. Please set an operation before calculating.")
        result = self._operation.calculate(a, b)
        result_fraction = Fraction(result).limit_denominator()
        self._logger.log(f"Executed {self._operation.__class__.__name__} on {a} and {b}: Result = {result_fraction}")
        return result_fraction