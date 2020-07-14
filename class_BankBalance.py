class bankaccount():
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def earn_money(self, amount):
        print("Earning money", amount)
        self.money += amount

    def withdraw_money(self, amount):
        print("Withdrawing money", amount)
        self.money -= amount

    def show_balance(self):
        print("Accout Balance", self.money)
def main():
    my_account = bankaccount("SpiderMan", 1000)
    my_account.show_balance()
    my_account.earn_money(200)
    my_account.show_balance()
    my_account.withdraw_money(500)
    my_account.show_balance()


if __name__=="__main__":
    main()
