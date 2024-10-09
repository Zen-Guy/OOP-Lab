# Write a program for pretty groccery bill

sum = 0
num = int(input('Number of distinct items: '))
bill = []
for i in range(num):
    iName = input(f'Item number {i+1}: ')
    iQuantity = int(input(f'Number of {iName}: '))
    iPrice = int(input(f'Price of single {iName}: '))
    sum += iQuantity * iPrice
    bill.append(iName)
    bill.append(iQuantity)
    bill.append(iPrice)
ind = 0
print('*************************BILL*******************************')
print('Item Name            Item Quantity                 Item Price')
for i in range(num):
    print(f'{bill[ind]}        {bill[ind+1]}                {bill[ind+2]}')
    ind += 3
print('************************************************************')
print(f'Total amount to be paid:                                {sum}')
print('************************************************************')
