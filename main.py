from random import randint


def restaurant():
    tables = f"свободных столиков - {randint(1, 10)}"
    print(tables)
    menu = input("Первое, Второе, десерт, Горячие напитки, бар - что желаете?: ")
    if menu == 'Первое':
        first = ['Caprese Salad - 5000 tg', 'Spinach and Artichoke Dip - 4000 tg']
        input1 = input(f"Выберайте - {first}")
        if input1 == 'Caprese Salad':
            money1 = 5000
            input2 = input('желаете второе?')
            if input2 == 'Да':
                second = ['Grilled Salmon - 2000 tg', 'Chicken Marsala - 1000 tg']
                input3 = input(f'Выберайте - {second}')
                if input3 == 'Grilled Salmon':
                    money3 = 2000
                    pp = money3 + money1
                    input6 = input('Вы хотите десерт')
                    if input6 == 'Да':
                        dessert = ['Chocolate Lava Cake - 500 tg', 'Tiramisu - 500 tg']
                        input90 = input(f'{dessert}: ')
                        if input90 == 'Chocolate Lava Cake':
                            money5 = 500
                            pp2 = pp + money5
                            input4 = input('Хотите горячие напитки? - ')
                            if input4 == 'Да':
                                hotDrink = ['Chai Latte - 200 tg', 'Mexican Hot Chocolate - 200 tg']
                                input88 = input(f"{hotDrink}: ")
                                if input88 == 'Chai Latte':
                                    money7 = 200
                                    pp4 = money7 + pp2
                                    input8 = input('Хотите что нибудь из бара? - ')
                                    if input8 == 'Да':
                                        bar = ['Margarita - 8000 tg', 'Old Fashioned - 8000 tg']
                                        input91 = input(f'{bar}: ')
                                        if input91 == 'Margarita':
                                            money100 = 8000
                                            pp4000 = money100 + pp4
                                            print(f"ваш чек {pp4000}")
                                elif input88 == 'Нет':
                                    input8 = input('Хотите что нибудь из бара? - ')
                                    if input8 == 'Да':
                                        bar = ['Margarita - 8000 tg', 'Old Fashioned - 8000 tg']
                                        input91 = input(f'{bar}: ')
                                        if input91 == 'Margarita':
                                            money100 = 8000
                                            pp4000 = money100 + pp2
                                            print(f"ваш чек {pp4000} tg")
                        elif dessert == 'Tiramisu':
                            money6 = 500
                            pp3 = money6 + money1
                            input4 = input('Хотите горячие напитки? - ')
                            if input4 == 'Да':
                                hotDrink = ['Chai Latte - 200 tg', 'Mexican Hot Chocolate - 200 tg']
                                input90 = input(f'{hotDrink}: ')
                                if input90 == 'Chai Latte':
                                    money7 = 200
                                    pp5 = money7 + pp3
                                    input99 = input('Хотите что нибудь из бара? - ')
                                    if input99 == 'Да':
                                        bar = ['Margarita - 8000 tg', 'Old Fashioned - 8000 tg']
                                        input91 = input(f'{bar}: ')
                                        if input91 == 'Margarita':
                                            money100 = 8000
                                            pp4100 = money100 + pp5
                                            print(f"ваш чек {pp4100}")
                elif input3 == 'Chicken Marsala':
                    money4 = 1000
                    pp2 = money4 + money1
            if input2 == 'Нет':
                dessert = ['Chocolate Lava Cake - 500 tg', 'Tiramisu - 500 tg']
                input90 = input(f'{dessert}: ')
                if input90 == 'Chocolate Lava Cake':
                    money5 = 500
                    pp2 = money1 + money5
                    input4 = input('Хотите горячие напитки? - ')
                    if input4 == 'Да':
                        hotDrink = ['Chai Latte - 200 tg', 'Mexican Hot Chocolate - 200 tg']
                        input88 = input(f"{hotDrink}: ")
                        if input88 == 'Chai Latte':
                            money7 = 200
                            pp4 = money7 + pp2
                elif dessert == 'Tiramisu':
                    money6 = 500
                    pp3 = money6 + money1
                    input4 = input('Хотите горячие напитки? - ')
                    if input4 == 'Да':
                        hotDrink = ['Chai Latte - 200 tg', 'Mexican Hot Chocolate - 200 tg']
                        input90 = input(f'{hotDrink}: ')
                        if input90 == 'Chai Latte':
                            money7 = 200
                            pp5 = money7 + pp3
                            input99 = input('Хотите что нибудь из бара? - ')
                            if input99 == 'Да':
                                bar = ['Margarita - 8000 tg', 'Old Fashioned - 8000 tg']
                                input91 = input(f'{bar}: ')
                                if input91 == 'Margarita':
                                    money100 = 8000
                                    pp4100 = money100 + pp5
                                    print(f"ваш чек {pp4100}")
                    if input4 == 'Нет':
                        input8 = input('Хотите что нибудь из бара? - ')
                        if input8 == 'Да':
                            bar = ['Margarita - 8000 tg', 'Old Fashioned - 8000 tg']
                            input91 = input(f'{bar}: ')
                            if input91 == 'Margarita':
                                money100 = 8000
                                pp4000 = money100 + pp3
                                print(f"ваш чек {pp4000}")
        elif input1 == 'Spinach and Artichoke Dip':
            money2 = 4000
            input1 = input(f"Выберайте - {first}")
            if input1 == 'Caprese Salad':
                money1 = 5000
                input2 = input('желаете второе?')
                if input2 == 'Да':
                    second = ['Grilled Salmon - 2000 tg', 'Chicken Marsala - 1000 tg']
                    input3 = input(f'Выберайте - {second}')
                    if input3 == 'Grilled Salmon':
                        money3 = 2000
                        pp = money3 + money1
                        input6 = input('Вы хотите десерт')
                        if input6 == 'Да':
                            dessert = ['Chocolate Lava Cake - 500 tg', 'Tiramisu - 500 tg']
                            input90 = input(f'{dessert}: ')
                            if input90 == 'Chocolate Lava Cake':
                                money5 = 500
                                pp2 = pp + money5
                                input4 = input('Хотите горячие напитки? - ')
                                if input4 == 'Да':
                                    hotDrink = ['Chai Latte - 200 tg', 'Mexican Hot Chocolate - 200 tg']
                                    input88 = input(f"{hotDrink}: ")
                                    if input88 == 'Chai Latte':
                                        money7 = 200
                                        pp4 = money7 + pp2
                                        input8 = input('Хотите что нибудь из бара? - ')
                                        if input8 == 'Да':
                                            bar = ['Margarita - 8000 tg', 'Old Fashioned - 8000 tg']
                                            input91 = input(f'{bar}: ')
                                            if input91 == 'Margarita':
                                                money100 = 8000
                                                pp4000 = money100 + pp4
                                                print(f"ваш чек {pp4000}")
                                    elif input88 == 'Нет':
                                        input8 = input('Хотите что нибудь из бара? - ')
                                        if input8 == 'Да':
                                            bar = ['Margarita - 8000 tg', 'Old Fashioned - 8000 tg']
                                            input91 = input(f'{bar}: ')
                                            if input91 == 'Margarita':
                                                money100 = 8000
                                                pp4000 = money100 + pp2
                                                print(f"ваш чек {pp4000} tg")
                            elif dessert == 'Tiramisu':
                                money6 = 500
                                pp3 = money6 + money1
                                input4 = input('Хотите горячие напитки? - ')
                                if input4 == 'Да':
                                    hotDrink = ['Chai Latte - 200 tg', 'Mexican Hot Chocolate - 200 tg']
                                    input90 = input(f'{hotDrink}: ')
                                    if input90 == 'Chai Latte':
                                        money7 = 200
                                        pp5 = money7 + pp3
                                        input99 = input('Хотите что нибудь из бара? - ')
                                        if input99 == 'Да':
                                            bar = ['Margarita - 8000 tg', 'Old Fashioned - 8000 tg']
                                            input91 = input(f'{bar}: ')
                                            if input91 == 'Margarita':
                                                money100 = 8000
                                                pp4100 = money100 + pp5
                                                print(f"ваш чек {pp4100}")
                    elif input3 == 'Chicken Marsala':
                        money4 = 1000
                        pp2 = money4 + money1
                if input2 == 'Нет':
                    dessert = ['Chocolate Lava Cake - 500 tg', 'Tiramisu - 500 tg']
                    input90 = input(f'{dessert}: ')
                    if input90 == 'Chocolate Lava Cake':
                        money5 = 500
                        pp2 = money1 + money5
                        input4 = input('Хотите горячие напитки? - ')
                        if input4 == 'Да':
                            hotDrink = ['Chai Latte - 200 tg', 'Mexican Hot Chocolate - 200 tg']
                            input88 = input(f"{hotDrink}: ")
                            if input88 == 'Chai Latte':
                                money7 = 200
                                pp4 = money7 + pp2
                    elif dessert == 'Tiramisu':
                        money6 = 500
                        pp3 = money6 + money1
                        input4 = input('Хотите горячие напитки? - ')
                        if input4 == 'Да':
                            hotDrink = ['Chai Latte - 200 tg', 'Mexican Hot Chocolate - 200 tg']
                            input90 = input(f'{hotDrink}: ')
                            if input90 == 'Chai Latte':
                                money7 = 200
                                pp5 = money7 + pp3
                                input99 = input('Хотите что нибудь из бара? - ')
                                if input99 == 'Да':
                                    bar = ['Margarita - 8000 tg', 'Old Fashioned - 8000 tg']
                                    input91 = input(f'{bar}: ')
                                    if input91 == 'Margarita':
                                        money100 = 8000
                                        pp4100 = money100 + pp5
                                        print(f"ваш чек {pp4100}")
                        if input4 == 'Нет':
                            input8 = input('Хотите что нибудь из бара? - ')
                            if input8 == 'Да':
                                bar = ['Margarita - 8000 tg', 'Old Fashioned - 8000 tg']
                                input91 = input(f'{bar}: ')
                                if input91 == 'Margarita':
                                    money100 = 8000
                                    pp4000 = money100 + pp3
                                    print(f"ваш чек {pp4000}")
        else:
            print('Error')

A = restaurant()
print(A)