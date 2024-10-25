from abc import ABC, abstractmethod
import math

class Operation(ABC):
    @abstractmethod
    def calculate(self, a: float, b: float) -> float:
        pass

class Addition(Operation):
    def calculate(self, a: float, b: float) -> float:
        return a + b

class Subtraction(Operation):
    def calculate(self, a: float, b: float) -> float:
        return a - b

class Multiplication(Operation):
    def calculate(self, a: float, b: float) -> float:
        return a * b

class Division(Operation):
    def calculate(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class Power(Operation):
    def calculate(self, a: float, b: float) -> float:
        return math.pow(a, b)

class Sine(Operation):
    def calculate(self, a: float, b: float = 0) -> float:
        return math.sin(a)

class CompoundInterest(Operation):
    def calculate(self, principal: float, rate: float, time: float) -> float:
        """Formula: A = P(1 + r/n)^(nt) pentru rate anual vrode"""
        return principal * (1 + rate) ** time