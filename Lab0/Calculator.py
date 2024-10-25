from abc import ABC, abstractmethod
from Operations import *

class Calculator(ABC):
    def __init__(self, logger):
        self._operation = None
        self._logger = logger

    def set_operation(self, operation: Operation):
        self._operation = operation
        self._logger.log(f"Operation set to {operation.__class__.__name__}")

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass