import heapq

class PrioQueue(object):
    def __init__(self, list : list):
        """
        Créer une file à priorité à partir d'une liste list :
        la liste list doit contenir les couples (priorité, element)
        """
        self.queue = [[prio, i, elt] for (i, (prio, elt)) in enumerate(list)]
        heapq.heapify(self.queue)


    def __repr__(self):
        """
        Représentation chaine de la file a priorite
        """
        return '<PrioQueue: {0.queue}>'.format(self)


    def decrease_prio(self, elt, new_prio):
        """
        Met à jour la priorite de 'elt' dans la file
        en la remplaçant par 'new_prio'
        """
        for i, (_, _, e) in enumerate(self.queue):
            if e == elt:
                self.queue[i][0] = new_prio
                heapq._siftdown(self.queue, 0, i)
        return self.queue
        


    def pop(self):
        """
        Extrait de la file à priorité l'élement de priorité minimale
        Renvoie le couple (priorité, élement) correspondant
        """
        prio, _, elt = heapq.heappop(self.queue)
        return (prio, elt)


    def is_empty(self):
        """
        Teste si la file à priorité est vide
        """
        return len(self.queue) == 0