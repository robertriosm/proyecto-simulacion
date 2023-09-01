import numpy as np
import random
import matplotlib.pyplot as plt



mapas = []

for x in range(3):

    map_types = {
    "control": ["Busan", "Nepal", "Ilios", "Oasis", "Lijian Tower", "Antartic Peninsula"],
    "push": ["Esperanca", "Colosseo", "New Queen Street"],
    "escort": ["Circuit Royale", "Dorado", "Route 66", "JunkerTown", "Rialto", "Havana", "Watchpoint Gibraltar", "Shambali Monastery"],
    "hybrid": ["Blizzard World", "Numbani", "Hollywood", "Eichenwalde", "Kings Row", "Midtown", "Paraiso"]
}
    
    map_order = ["control", "hybrid", "push", "escort", "control"]
    selected_maps = []

    # Elegir el primer mapa aleatoriamente
    first_map_type = "control"
    selected_maps.append(random.choice(map_types[first_map_type]))

    # Eliminar el mapa seleccionado del tipo para el último mapa
    map_types[first_map_type].remove(selected_maps[0])
    map_order.remove(map_order[0])

    # Calcular las probabilidades para la distribución multinomial
    probabilities = [len(map_types[map_type]) for map_type in map_order]

    # Generar una selección de mapas utilizando la distribución multinomial
    selected_indices = np.random.multinomial(1, probabilities / np.sum(probabilities), size=1)[0]

    # Seleccionar un mapa aleatorio del tipo seleccionado para cada índice
    for selected_index, map_type in zip(selected_indices, map_order):
        selected_map = map_types[map_type][selected_index]
        selected_maps.append(selected_map)

    mapas += selected_maps
    print(selected_maps)


# # Transpose the mapas array to get separate lists for each index
# transposed_mapas = np.array(mapas).T.tolist()

# # Plot grouped histograms
# for idx, maps_list in enumerate(transposed_mapas):
#     plt.hist(maps_list, bins=len(set(maps_list)), alpha=0.5, label=f'Element {idx}')
    
# plt.title('Grouped Histograms')
# plt.xlabel('Map')
# plt.ylabel('Frequency')
# plt.xticks(rotation=45)
# plt.legend()
# plt.show()

