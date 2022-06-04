# Ви є продук менеджером і зараз очолюєте команду з розробки нового продукту.
# На жаль, остання версія вашого продукту не проходить перевірку якості.
# Оскільки кожна версія розроблена на основі попередньої версії, всі версії після поганої версії також погані.
# Припустимо, у вас є n версій [1, 2, ..., n], і ви хочете знайти першу погану, через яку всі наступні будуть поганими.
# Вам надається функція isBadVersion(version) -. bool, який повертає, чи є версія поганою.
# Реалізуйте функцію пошуку першої поганої версії. Вам слід мінімізувати кількість викликів до функції.
def isBadVersion(version):
    bad = 9
    if version == bad:
        return False
    else: return True

versions = [1,2,3,4,5,6,7]
for i in versions:
    if isBadVersion(i) == False:
        print(f"bad version - {i}")
        break

# Для списку цілих чисел nums, відсортованого в зростаючому порядку,
# поверніть масив квадратів кожного числа, відсортованих у зростаючому порядку.

def rise_sort(list):
    list = [a**2 for a in list]
    return sorted(list)
list = [-4,-1,0,3,10]
print(rise_sort(list))

# Для списку цілих чисел nums перемістіть усі 0 в кінець, зберігаючи відносний порядок ненульових елементів.
# Зауважте, що ви повинні зробити це на місці, не створюючи копію масиву.


def shift_zero(list):
    for i in list:
        if i == 0:
            list.remove(0)
            list.append(0)
    return list

nums = [0,1,0,0,0,3,0,9,9,0,12]
print(shift_zero(nums))

# Дано два відсортованих списка list1 I list2 повернути один відсортований список що місить елементи list1 I list2.
# Example 1:

def union_sort(list_1,list_2):
    return sorted(list1+list2)

list1 = [1,2,4]
list2 = [1,3,4]
print(union_sort(list1,list2))

# Дано масив літер змінити його порядок на протилежний не виконуючи функцій revers та [::-1]

def flipping(s):
    for i in range(len(s) // 2):
        tmp = s[i]
        s[i] = s[len(s) - i - 1]
        s[len(s) - i - 1] = tmp
    return s

s = ["h","e","l","l","o"]
print(flipping(s))


# Написати функцію, яка приймає число n. А повертає значення числа фібоначі з порядковим номером N

def fib(indx):
    i = 0
    a = 0
    b = 1
    if indx == 0:
        return 0
    while i < indx-1:
        tmp = a
        a = b
        b = tmp + b
        i += 1
    return b

print(fib(4))