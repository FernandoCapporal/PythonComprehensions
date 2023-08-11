import csv
import matplotlib.pyplot as plt


continente = input("Ingresa el continente que quieres gráficar: ")

countries = []
percentages = []
with open("data.csv", 'r') as file:
    data = csv.DictReader(file)
    for line in data:
        if line['Continent'] == continente:
            countries.append(line['Country'])
            percentages.append(line['World Population Percentage'])

if len(countries) != 0:

    fig, ax = plt.subplots()

    ax.pie(percentages, labels=countries)
    ax.set_title(f"world population percentage countries in {continente}")

    plt.show()

else:
    print("Vuelva a correr el programa con un continente válido")
