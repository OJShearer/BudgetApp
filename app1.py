from budgetClass import Budget

bud1 = Budget('Food')
file1 = open('Food.txt', 'w')
file1.write(str(bud1.amount))
file1.close()

bud2 = Budget('Entertainment')
file1 = open('Entertainment.txt', 'w')
file1.write(str(bud2.amount))
file1.close()