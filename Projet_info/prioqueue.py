import heapq

class PrioQueue(object):
    def __init__(self, l):
        """Cree une file a priorite a partir d'une liste l :
        la liste l doit contenir les couples (priorite, element)"""
        self.queue = [[prio, i, elt] for (i, (prio, elt)) in enumerate(l)]
        heapq.heapify(self.queue)

    def __repr__(self):
        """Representation chaine de la file a priorite"""
        return '<PrioQueue: {0.queue}>'.format(self)

    def decrease_prio(self, elt, new_prio):
        """Met a jour la priorite de 'elt' dans la file
        en la remplacant par 'new_prio'"""
        for i, (_, _, e) in enumerate(self.queue):
            if e == elt:
                self.queue[i][0] = new_prio
                heapq._siftdown(self.queue, 0, i)
        return self.queue
        raise KeyError("decrease_prio")

    def pop(self):
        """Extrait de la file a priorite l'element de priorite minimale
        Renvoie le couple (priorite, element) correspondant"""
        prio, _, elt = heapq.heappop(self.queue)
        return (prio, elt)

    def is_empty(self):
        """Teste si la file a priorite est vide"""
        return len(self.queue) == 0
