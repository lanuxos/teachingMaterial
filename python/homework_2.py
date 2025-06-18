# homework, if-else, grading
while True:
    grade = float(input('\nກະລຸນາປ້ອນຄະແນນເສັງຂອງທ່ານ >_ '))
    if grade >= 90:
        print('A')
    elif grade >= 80:
        print('B')
    elif grade >= 65:
        print('C')
    elif grade >= 50:
        print('D')
    else:
        print('F')