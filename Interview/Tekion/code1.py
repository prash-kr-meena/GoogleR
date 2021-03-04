"""
input_list = [
"p1 sell s1 1500 200",
"p2 buy s2 900 500",
"p3 buy s1 600 250",
"p4 buy s1 1200 270",
"p10 sell s2 1000 400",
"p5 sell s3 300	800",
"p6	sell s3 100	750",
"p7 buy s3 500 900",
"p20 sell s4 200 100",
"p21 sell s4 200 150",
"p22 buy s4 200 300"
this is infinite
]

person type stock qty	price

p1	sell	s1	1500	200            {"s1"  : [(1500,200) (), ()]}  { "" }
p2	buy		s2	900		500
p3	buy		s1	600		250
p4	buy		s1	1200	270    +300 more for s1??

p5	sell	s3 	300		800
p6	sell	s3 	100		750      cost get more preference then time, if cost is same then go for time
p7  buy     s3  500     900    +200 requirement

p20 sell 	s4	200		100
p21 sell 	s4	200		150
p22 buy     s4  200     300

p23	buy		s2	900		500  + 800 more
p10	sell	s2	1000	400

p11 sell    s2  1000    300    left 200 quantities


Trades

p3:s1:600:200
p4:s1:900:200

p7:s3:100:750
p7:s3:300:800

p22:s4:200:100

p2:s2:900:400
p23:s2:100:400
p23:s2:800:300
"""

# {"s1": [(1500, 200)(), ()]}
# {""}
from collections import OrderedDict

buyers: dict[str, list] = OrderedDict()
sellers: dict[str, list] = OrderedDict()


def stock_buy_sell(person, type, stock_name, qty, price) -> None:
    if type == "sell":
        sellers_price = price
        sellers_qty = qty

        if buyers.get(stock_name) is not None:
            buyers_quotes = buyers.get(stock_name)
            # []
            for quote in buyers_quotes:
                buyers_quote_qty = quote[0]
                buyers_quote_price = quote[1]

                if sellers_price <= buyers_quote_price:  # (qty, price)
                    if sellers_qty > buyers_quote_qty:  # Buyer  & sell qty will get disolved
                        sellers_qty = sellers_qty - buyers_quote_qty
                        ## remove this quote form quote_list
                        del quote
                    else:  # sellers_qty < buyers_quote_qty:
                        pass
                    min_qty = min(sellers_qty, buyers_quote_qty)
                    pass
            pass
        else:
            push_it_into_bucket(price, qty, stock_name, type)
        pass
    else:  # buy
        pass

    push_it_into_bucket(price, qty, stock_name, type)

    pass


def push_it_into_bucket(price, qty, stock_name, type):
    if type == "buy":
        if stock_name in buyers:
            buyers.get(stock_name).append((qty, price))
        else:
            buyers[stock_name] = [(qty, price)]

    elif type == "sell":
        if stock_name in sellers:
            # some kind of insertion sort that will take O(n), becasue all the other elements will be sorted
            current_sell_pairs = sellers.get(stock_name)
            current_sell_pairs.append((qty, price))
            pair_sorted_by_price = sorted(current_sell_pairs, key=lambda pair: pair[1])
            sellers[stock_name] = pair_sorted_by_price
        else:
            sellers[stock_name] = [(qty, price)]


if __name__ == '__main__':
    person, type, stock, qty, price = input().strip().split()
    qty = int(qty)
    price = int(price)
    stock_buy_sell(person, type, stock, qty, price)
