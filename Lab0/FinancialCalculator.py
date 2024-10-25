from Calculator import *

class FinancialCalculator(Calculator):
    
    def execute(self, principal: float, rate: float, time: float) -> float:
        if self._operation is None:
            raise ValueError("No operation set. Please set an operation before calculating.")
        result = self._operation.calculate(principal, rate, time)
        self._logger.log(f"Executed {self._operation.__class__.__name__} with principal = {principal}, rate = {rate}, time = {time}: Result = {result}")
        return result