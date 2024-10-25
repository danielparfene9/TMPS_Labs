from Calculator import *

class BasicCalculator(Calculator):
    def execute(self, a: float, b: float = 0) -> float:
        if self._operation is None:
            raise ValueError("No operation set. Please set an operation before calculating.")
        result = self._operation.calculate(a, b)
        if result.is_integer():
            result = int(result)
        self._logger.log(f"Executed {self._operation.__class__.__name__} on {a} and {b}: Result = {result}")
        return result