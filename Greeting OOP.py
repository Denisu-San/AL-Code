class Greeting:
    # @classmethod
    def hello(self, firstName = None, secondName = None):
        if firstName is not None and secondName is not None:
            print(f"Hello! {firstName} {secondName}")
        elif firstName is not None and secondName is None:
            print(f"Hello! {firstName}")
        elif firstName is None and secondName is not None:
            print(f"Hello! {secondName}")
        else:
            print("Hello!")
    pass

# With decorator @classmethod
# Greeting.hello("Denis","Hoareau")
# Greeting.hello( None,"Hoareau")
# Greeting.hello("Denis", None)
# Greeting.hello()

# #no classmethod
# MyGreeting = Greeting()
# MyGreeting.hello("Denis", "Hoareau")