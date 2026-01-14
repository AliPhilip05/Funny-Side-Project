import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
class frechDeck:
    ranks = [n for n in range(2,11) + list('JKQA')]
    suits = 'spade heart club diamond'.split()

def __initiaize(self):
    self.cards = [Card(rank,suit)]