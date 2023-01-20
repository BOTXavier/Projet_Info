import matplotlib.pyplot as plt 
DONNEES_DIJ = 'C:\ENAC\\1A\python\labyrinthe\Projet_Info-1\Projet_Info-1\Projet_info\donnees_dij.txt' 


def recup_donnees(file, t, nbr_case_visite, nbr_cycles, n):
    f1 = open(file, 'a')
    f1.write(str(t) + ' ' + str(nbr_case_visite)+ ' ' + str(nbr_cycles) + ' ' + str(n)+ '\n')
    f1.close()


def read_file(file):
    t, nbr_case_visite, nbr_cycle, n = [], [], [], []
    with open(file) as f:
        for line in f:
            l = line.split()
            t.append(float(l[0]))
            nbr_case_visite.append(int(l[1]))
            nbr_cycle.append(int(l[2]))
            n.append(int(l[3]))
    return t, nbr_case_visite, nbr_cycle, n


def plot_comparaison(file):
    t, nbr_case_visite, nbr_cycle, n = read_file(file)
    plt.subplot(121)
    plt.plot(n, t)
    plt.title('Temps d\'éxécution en fonction de la taille du laby')
    plt.ylabel('Temps d\'éxécution en s')
    plt.xlabel('taille du laby')

    plt.subplot(122)
    plt.plot(n, nbr_case_visite)
    plt.title('Nombre de cases visitées en fonction de la taille du laby')
    plt.ylabel('Nombre de cases visitées')
    plt.xlabel('taille du laby')
    


t, nbr_case_visite, nbr_cycle, n = read_file(DONNEES_DIJ)
plot_comparaison(DONNEES_DIJ)
plt.show()