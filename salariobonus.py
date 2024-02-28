name = input()

salary = float(input())

sales = float(input())

commission = sales * 15 / 100

total = salary + commission

print("TOTAL = R$ {:.2f}".format(total))
