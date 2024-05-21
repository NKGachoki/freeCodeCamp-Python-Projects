"""Module providing a function that arranges and solves the list of arithmetic problems."""
from arithmetic_arranger import arithmetic_arranger

print("Output of arithmetic_arranger function where 2nd arg == 'False'")
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print()
print("Output of arithmetic_arranger function where 2nd arg == 'True'")
print(arithmetic_arranger(["32 + 8","1 - 3801","9999 + 9999","523 - 49"], True))
