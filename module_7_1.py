class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"



class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        with open(self.__file_name, 'a') as file:
            pass

    def get_products(self):
        products = []
        with open(self.__file_name, 'r') as file:
            for line in file:
                if len(line.strip().split(', ')) == 3:
                    name, weight, category = line.strip().split(', ')
                    products += [str(Product(name, float(weight), category))]

        return '\n'.join(products)

    def add(self, *products):

        products_in_shop = [i.split(', ')[0] for i in self.get_products().split('\n')]
        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name not in products_in_shop:
                    file.write(str(product)+'\n')
                    products_in_shop += [product.name]
                else:
                    print(f"Продукт {product.name} уже есть в магазине")


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1, p2, p3)
print(str(s1.get_products()))
