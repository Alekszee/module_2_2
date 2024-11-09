First = int(input('Введите 1-е число: '))
Second = int(input('Введите 2-е число: '))
Third = int(input('Введите 3-е число: '))
if First == Second and First == Third and Second == Third:
    print('3')
elif First == Second or First == Third or Second == Third :
    print('2')
elif First != Second and First != Third and Second != Third :
    print('0')
