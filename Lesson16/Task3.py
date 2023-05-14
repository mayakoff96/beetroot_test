class Product:

    def __init__(self, product_type, name, price):
        self.type = product_type
        self.name = name
        self.price = price


class ProductStore:

    def __init__(self):
        self.products = []
        self.income = 0

    def add(self, product, amount):
        if amount <= 0:
            raise ValueError('Amount must be a positive integer')

        product.price *= 1.3

        for stored_product in self.products:
            if stored_product.name == product.name:
                stored_product.amount += amount
                break
        else:
            product.amount = amount
            self.products.append(product)

    def set_discount(self, identifier, percent, identifier_type='name'):
        if percent < 0 or percent > 100:
            raise ValueError('Discount percentage must be between 0 and 100.')

        for product in self.products:
            if identifier.type == 'name' and product.name == identifier:
                product.price *= (100 - percent) / 100
            elif identifier_type == 'type' and product.type == identifier:
                product.price *= (100 - percent) /100

    def sell_product(self, product_name, amount):
        for product in self.products:
            if product.name == product_name:
                if amount > product.amount:
                    raise ValueError('Insufficient quantity in stock')

                product.amount -= amount
                self.income += product.price * amount
                break
        else:
            raise ValueError('Product not found is store.')

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [(product.name, product.type, product.price, product.amount) for product in self.products]

    def get_product_info(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product.name, product.amount
        else:
            raise ValueError('Product not found in store')


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)
print(s.get_product_info('Ramen') == ('Ramen', 290))
