import matplotlib.pyplot as plt
fig = plt.figure()  # utile pour le fonctionnement dans replit

#### Fonction
def caluler_vitesse(x, y, dt, i):
    """Calcule la vitesse instantané du G à l'instant ti"""
    vx = (x[i + 1] - x[i - 1]) / (2 * dt)
    vy = (y[i + 1] - y[i - 1]) / (2 * dt)
    return (vx, vy)


def tracer_vecteur(x, y, vx, vy, echelle=0.07):
    plt.quiver(x, y,
               vx * echelle, vy * echelle,
               color="red",
               scale=1, scale_units='xy')


def afficher_graphe():
    # Configuration de la représentation graphique"""
    plt.plot(x, y, 'o', markersize=5)
    plt.xlabel("x (en m)")
    plt.ylabel("y (en m)")
    plt.title("Étude de la vitesse instantanée lors d'une chute")

    # Affichage
    #plt.show()   Si utilisation hors replit
    plt.savefig("Chute.png")
    

#### Programme principal
# Valeurs experimentales
y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = [0, 0, 0, 0, 0, 0, 0, 0, 0]
dt = 0.1

# points limites
second_point = 1
avant_dernier_point = len(y) - 1

for point in range(second_point, avant_dernier_point):
    (vx, vy) = caluler_vitesse(x, y, dt, point)
    tracer_vecteur(x[point], y[point], vx, vy)
afficher_graphe()
