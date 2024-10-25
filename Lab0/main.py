from Operations import *
from BasicCalculator import BasicCalculator
from Logger import *
from FinancialCalculator import FinancialCalculator
from ScientificCalculator import ScientificCalculator

if __name__ == "__main__":
    logger = ConsoleLogger()

    basic_calc = BasicCalculator(logger)
    basic_calc.set_operation(Addition())
    basic_result = basic_calc.execute(5, 3)
    print(f"Basic Result: {basic_result}\n")

    basic_calc.set_operation(Division())
    basic_result = basic_calc.execute(10, 3)
    print(f"Basic Result: {basic_result}\n")

    scientific_calc = ScientificCalculator(logger)
    scientific_calc.set_operation(Sine())
    scientific_result = scientific_calc.execute(math.pi / 2)
    print(f"Scientific Result: {scientific_result}\n")

    scientific_calc.set_operation(Power())
    scientific_result = scientific_calc.execute(2, 3)
    print(f"Scientific Result: {scientific_result}\n")

    financial_calc = FinancialCalculator(logger)
    financial_calc.set_operation(CompoundInterest())
    financial_result = financial_calc.execute(1000, 0.05, 10)
    print(f"Financial Result: {financial_result}")
