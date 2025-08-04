# #For 2 params
# class Greeting:
#     @classmethod
#     def hello(self, firstname = None, secondname = None):
#         if firstname is not None and secondname is not None:
#             print(f"Hello {firstname} {secondname}")
#         else:
#             print("Hello")

# #with @classmethod
# Greeting.hello("Denis", "Hoareau")

# #no classmethod
# MyGreeting = Greeting()
# MyGreeting.hello("Denis", "Hoareau")




# #For no parameters
# class Greeting:
#     def hello(self):
#         print("Hello")

# MyGreeting = Greeting()
# MyGreeting.hello()




# #For only 1 parameter
# class Greeting:
#     def hello(self, firstname = None):
#         if firstname is not None:
#             print(f"Hello {firstname}")
#         else:
#             print("Hello")

# #create and object and call method
# MyGreeting = Greeting()
# MyGreeting.hello("Denis")