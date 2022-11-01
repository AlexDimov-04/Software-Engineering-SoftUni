class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product == product_name:
                return product

    def remove(self, product_name: str):
        current_product = self.find(product_name)
        if current_product:
            self.products.remove(current_product)

    def __repr__(self):
        output = '\n'.join([f"{product.name}: {product.quantity}" for product in self.products])
        return output
