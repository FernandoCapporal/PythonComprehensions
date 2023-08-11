import csv
import matplotlib.pyplot as plt

my_dict = {}

with open('data.csv','r') as file:
    my_file = csv.DictReader(file)

    for i in my_file:
        my_dict[dict(i)['Country']] = dict(i)

def plot_poblation(pais):

    aux = (list(my_dict[pais].keys()))
    x_aux=[]
    for i in aux:
        if (len(i.split()) == 2) and  (i.split()[1] == 'Population'):
            x_aux.append( [int(i.split()[0]),  int(my_dict[pais][i])]  )

    x_aux = sorted(x_aux, key=lambda x: x[0])
    print(x_aux)
    fig, ax = plt.subplots()

    x1 = [x[0] for x in x_aux]
    y1 = [y[1] for y in x_aux]

    ax.bar(x1, y1, color = 'r',  width= 2, align='center')
    ax.set_xlabel('decada')
    ax.set_ylabel('N° habitantes.')
    ax.set_ylim([0, max(y1)])
    ax.set_title(f"{pais} pupulation in last years")

    plt.show()

pais = input("Ingresa el país del cual quieres obtener información poblacional: ")

try:
    d = my_dict[pais]
    print(my_dict[pais])
    plot_poblation(pais)
except Exception:
    print("Vuelva a correr el programa e ingrese un valor válido")




