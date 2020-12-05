"""
Заданий вектор розмірності n, компонентами якого є записи, що
містять відоммості про вершини гір. У відомостях про кожну вершину
вказуються назва гори і її висота. Скласти програму пошуку найвищої
вершини.
"""

#----------------------First case---------------------------

mountain_and_peak = tuple((('Alps', 4810), ('Kazbek', 5152), ('Elbrus', 5642), ('Dykhtau', 5204)))
max_peak = max(i[1] for i in mountain_and_peak)
for i in range(len(mountain_and_peak)):
    if mountain_and_peak[i][1] == max_peak:
        print(mountain_and_peak[i])     # output ('Elbrus', 5642)


#-----------------------Second case---------------------------

mountain_and_peak = tuple((('Alps', 4810), ('Kazbek', 5152), ('Elbrus', 5642), ('Dykhtau', 5204)))
print(*[mountain_and_peak[i] for i in range(len(mountain_and_peak)) if mountain_and_peak[i][1] == max(i[1] for i in mountain_and_peak)])    # output ('Elbrus', 5642)










