"""
Відомості про автомобіль складаються з його марки, унікального
номера і прізвища власника. Дано словник, який містить відомості про
декілька автомобілей. Скласти процедури знаходження
a) прізвищ власниківі номерів автомобілей даної марки;
b) кількості автомобілей кожної марки.

"""

cars_dictionary = {'AA3321BE': ['Volvo', 'Solopov'], 'AR33921IO': ['Volvo', 'Korney'],
                   'AO3312LP': ['Porsche', 'Alehiienko'], 'KA3330II': ['Porsche', 'Dunar'],
                   'LS3345NP': ['BMW', 'Korney'], 'LM3241PO': ['Mercedes', 'Solopov'],
                   'LO2234IO': ['Volvo', 'Lopkin'], 'AK4657VS': ['Toyota', 'Volohina'],
                   'AM33893BI': ['Volga', 'Anroniana'], 'AL4532LO': ['Honda', 'Kanoval']}


# a) this function find last name and number car from input values call car
def find_by_brand():
    car_brands = str(input('Enter valid values about brand car: ').lower())
    found_car = [(key, value[1]) for key, value in cars_dictionary.items() if value[0].lower() == car_brands]

    if any(found_car):
        print("I'm finding:", sep='\n')
        return found_car
    else:
        return 'Have not found this brand'


print(find_by_brand(), sep=', ')
print()


# b) this function count how many cars each brand
def count_car():
    lst_brands = [cars_dictionary[i][0] for i in cars_dictionary]
    lst_all_brands = list(set([cars_dictionary[i][0] for i in cars_dictionary]))

    count = [(i, lst_brands.count(i)) for i in lst_all_brands]

    n = str(input('Enter "count" if do you want count all brand cars in the dictionary, or "no" if you do not:'))
    while n != 'count' or n != 'no':
        if 'count' == n.lower():
            return count
        elif 'no' == n.lower():
            return 'End'
        else:
            n = str(input('Enter correct answer please:'))


print(*count_car(), sep='\n')
