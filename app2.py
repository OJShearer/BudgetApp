from budgetClass import Budget

bud1 = Budget('Food')
with open('Food.txt', 'r') as file1:
     bud1.amount = float(file1.readline())

bud2 = Budget('Entertainment')
with open('Entertainment.txt', 'r') as file1:
     bud2.amount = float(file1.readline())

working = True

while working:
     print("Options: 1.View Budgets  2.Edit Budgets  3.Session History  4.Quit")
     control = int(input('Choose an option. '))


     if control == 1:
          control2 = True
          while control2 == True:
               print('You have 2 budgets: 1.Food  2.Entertainment, or 3.Back')
               view = int(input('Choose a budget to view '))

               if view == 1:
                    print(bud1)
               elif view == 2:
                    print(bud2)
               elif view == 3:
                    control2 = False
               else:
                    print('Invalid choice.')
               
     elif control == 2:
          control3 = True
          while control3 == True:
               print('Options: 1.Withdraw  2.Deposit  3.Transfer  4.Back')
               view = int(input('Choose an option. '))

               if view == 1:
                    print('Budgets: 1.Food  2.Entertainment')
                    b = int(input('Which budget would you like to withdraw from? '))
                    if b == 1:
                         val = float(input('How much to withdraw? '))
                         des = input('Reason ')
                         bud1.withdraw(val, des)
                    elif b == 2:
                         val = float(input('How much to withdraw? '))
                         des = input('Reason ')
                         bud2.withdraw(val, des)
                    else:
                         print('Invalid budget.')

               elif view == 2:
                    print('Budgets: 1.Food  2.Entertainment')
                    b = int(input('Which budget would you like to deposit into? '))
                    if b == 1:
                         val = float(input('How much to deposit? '))
                         des = input('Reason ')
                         bud1.deposit(val, des)
                    elif b == 2:
                         val = float(input('How much to deposit? '))
                         des = input('Reason ')
                         bud2.deposit(val, des)
                    else:
                         print('Invalid budget.')

               elif view == 3:
                    print('Budgets: 1.Food  2.Entertainment')
                    b = int(input('Which budget would you like to transfer from? '))
                    if b == 1:
                         val = float(input('How much to transfer? '))
                         bud1.transfer(bud2, val)
                    elif b == 2:
                         val = float(input('How much to transfer? '))
                         bud2.transfer(bud1, val)
                    else:
                         print('Invalid budget.')

               elif view == 4:
                    control3 = False

               else:
                    print('Invalid choice.')

     elif control == 3:
          bud1.history()
          bud2.history()

     elif control == 4:
          working = False

     else:
          print('Invalid choice.')
