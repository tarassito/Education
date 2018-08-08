# SOLID
# https://www.youtube.com/watch?v=CrD8yf58xEI - World of tanks example. Clear explanation!!!
# Single Responsibility - A class should have only one reason to change


class Order:

    def __init__(self, customer, cart):
        self.customer = customer
        self.cart = list(cart)

    def charge(self):
        print('Charging...')
        # get money from client

    def send_mail(self):
        print('Emailing...')
        # send message to client mail

    def generate_coupon(self):
        print('Generating coupon...')
        # generate coupon for client

# How to check?
# 1. Describe the class responsibility on human language. There should not be "and" or "or".
    # Class Order processes client order charging money AND generating coupon AND send message to client mail.

# 2. Change methods to questions. Each question should have sense for this class.
    # Class Order, may you send mail to client? Have no sense for Order, this method is better for class Mailer.

# 3. Find reasons to change the class. It should be only one reason.
    # For example, I want to change mail pattern or coupon discount rate.


class Order:

    def __init__(self, customer, cart):
        self.customer = customer
        self.cart = list(cart)

    def charge(self):
        print('Charging...')


class Mailer:

    def send_mail(self, content, customer):
        print('Emailing...')


class Coupon:

    def __init__(self, code=None):
        code = code if code is not None else Coupon.generate_code()

    @staticmethod
    def generate_code():
        print('Generating code...')




