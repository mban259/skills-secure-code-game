'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')


def validorder(order: Order):

    payment: Decimal = Decimal(0)
    product: Decimal = Decimal(0)
    # net: Decimal = Decimal(0)

    for item in order.items:
        if not isinstance(item.quantity, int):
            return "Invalid order detected"
        # print("dd {} {}".format(item, net))
        if item.type == 'payment':
            payment += Decimal(str(item.amount))
        elif item.type == 'product':
            product += Decimal(str(item.amount)) * item.quantity
        else:
            return "Invalid item type: %s" % item.type

        if product > 1e6:
            return "Total amount payable for an order exceeded"

    # print(f"{payment} {product}")
    if not (abs(payment - product) < 1e-15):
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, payment - product)
    else:
        return "Order ID: %s - Full payment received!" % order.id
