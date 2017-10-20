from l1 import order.py

from l1 import calc

nodes, pools= order.execute(input("File name"))
print(calc.execute(nodes, pools))