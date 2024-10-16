# SOLID Calculator Project

## Author: Parfene Daniel

----

## Objectives:

* Implement 2 Principles of SOLID.

## Overview
This project implements a flexible and extendable calculator following the **SOLID principles** of software design. The calculator supports:

- **Basic Operations**: Addition, Subtraction, Multiplication, and Division.
- **Scientific Operations**: Sine and Power functions.
- **Financial Operations**: Compound Interest calculation.

The design allows for easy addition of new operations without modifying the existing codebase.

## Features

- **Modular Operations**: Each operation is encapsulated in its own class.
- **Basic Calculations**: Addition, Subtraction, Multiplication, Division.
- **Scientific Calculations**: Trigonometric and exponential functions.
- **Financial Calculations**: Compound interest.
- **Logging**: Console logging of each operation.
- **Flexible Operation Setting**: Users can dynamically switch between different operations.

## SOLID Principles

This project is designed according to the SOLID principles:

1. **Single Responsibility Principle (SRP)**: Each class is responsible for a single part of the program's functionality. For example:
   - `Addition`, `Subtraction`, etc., handle specific operations.
   - `BasicCalculator`, `ScientificCalculator`, and `FinancialCalculator` handle different types of calculations.
     ```python
     class Addition(Operation):
     def calculate(self, a: float, b: float) -> float:
        return a + b


2. **Open/Closed Principle (OCP)**: The calculator is open for extension but closed for modification. New operations can be added by extending the `Operation` abstract class.
     ```python
     class Modulus(Operation):
     def calculate(self, a: float, b: float) -> float:
        return a % b

3. **Liskov Substitution Principle (LSP)**: Any subclass of `Calculator` can replace the parent class without affecting the functionality.
     ```python
     basic_calc.set_operation(Modulus())
     basic_result = basic_calc.execute(10, 3)

4. **Interface Segregation Principle (ISP)**: Interfaces (abstract classes) are small and specific, e.g., `Operation` and `Logger`.
     ```python
     class Operation(ABC):
     @abstractmethod
     def calculate(self, a: float, b: float) -> float:
         pass

     class Logger(ABC):
     @abstractmethod
     def log(self, message: str) -> None:
         pass

5. **Dependency Inversion Principle (DIP)**: High-level modules like `Calculator` depend on abstractions (`Operation`, `Logger`), not concrete implementations.
     ```python
     class Calculator(ABC):
     def __init__(self, logger):
         self._operation = None
         self._logger = logger
     
     class BasicCalculator(Calculator):
     def execute(self, a: float, b: float = 0) -> float:
         if self._operation is None:
             raise ValueError("No operation set. Please set an operation before calculating.")
         result = self._operation.calculate(a, b)
         if result.is_integer():
             result = int(result)
         self._logger.log(f"Executed {self._operation.__class__.__name__} on {a} and {b}: Result = {result}")
         return result

## Class Structure

- **Operation (Abstract Class)**: The base class for all operations. New operations should extend this class.
- **BasicCalculator**: Handles basic arithmetic operations.
- **ScientificCalculator**: Supports scientific functions.
- **FinancialCalculator**: Calculates financial metrics, like compound interest.
- **Logger (Abstract Class)**: The base class for logging.
- **ConsoleLogger**: Logs messages to the console.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/calculator
    ```
2. Navigate to the project directory:
    ```bash
    cd calculator
    ```
## Usage

```python
from math import pi
from logger import ConsoleLogger
from calculators import BasicCalculator, ScientificCalculator, FinancialCalculator
from operations import Addition, Division, Power, Sine, CompoundInterest

logger = ConsoleLogger()

# Basic Calculator Usage
basic_calc = BasicCalculator(logger)
basic_calc.set_operation(Addition())
result = basic_calc.execute(5, 3)
print(f"Basic Result: {result}")

# Scientific Calculator Usage
scientific_calc = ScientificCalculator(logger)
scientific_calc.set_operation(Sine())
result = scientific_calc.execute(pi / 2)
print(f"Scientific Result: {result}")

# Financial Calculator Usage
financial_calc = FinancialCalculator(logger)
financial_calc.set_operation(CompoundInterest())
result = financial_calc.execute(1000, 0.05, 10)
print(f"Financial Result: {result}")
