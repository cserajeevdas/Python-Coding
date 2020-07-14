class bankaccount():
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def earn_money(self, amount):
        self.money += amount

    def withdraw_money(self, amount):
        self.money -= amount

    def show_balance(self):
        print(self.money)
def main():
    spidermans_account = bankaccount("SpiderMan", 1000)
    spidermans_account.show_balance()


if __name__=="__main__":
    main()
