# IT WILL PROCESS RECORDS FROM A DATABASE
# it will calculate totals 
#applying business rules
#using looops and conditions
# organise logic into functions

#create a sample data
orders = [
    {"id": 1, "customer_name": "mary", "items": 3, "price_per_item": 500},
    {"id": 2, "customer_name": "Austin","items": 1, "price_per_item": 1500},

]
# calculate orders total
def calculate_total (order):
    return order["items"] *order["price_per_item"]

# applybusiness rules
def apply_discount(total):
    if total >2500:
        return total * 0.9
    return total

# process all orders
def process_orders(orders):
    for order in orders:
        total = calculate_total(order)
        final_total = apply_discount(total)

        print("order id:", order["id"])
        print("customer:",order["customer_name"])
        print("final total:",final_total)
        print ("-" * 30)
process_orders(orders)
