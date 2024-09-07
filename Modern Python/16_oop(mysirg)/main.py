class Customer:
    __counter = 1
    def __init(self):
        self.id = Customer.__counter
        Customer.__counter +=1
    @staticmethod
    def get_counter():
        return Customer.__counter
    @staticmethod
    def set_counter(new_counter):
        if type(new_counter) == int:
            Customer.__counter = new_counter
        else:
            print("Invalid")


counter = Customer.get_counter()
print(counter)