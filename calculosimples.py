part_1, amount_1, value_1 = input().split()
part_1 = int(part_1)
amount_1 = int(amount_1)
value_1 = float(value_1)

part_2, amount_2, value_2 = input().split()
part_2 = int(part_2)
amount_2 = int(amount_2)
value_2 = float(value_2)


total = (amount_1 * value_1) + (amount_2 * value_2)

print("VALOR A PAGAR: R$ {:.2f}".format(total))
