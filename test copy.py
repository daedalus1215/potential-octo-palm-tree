from typing import Dict, MutableMapping

def populate_ranks(votes: Dict[str, int], ranks: Dict[str, int]) -> None:
    """ this provides the best mix of static type safety and runtime performance """
    names = list(votes.keys())
    names.sort(key=votes.__getitem__, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i

def get_winner_4(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))

class SortedDict(MutableMapping):
    """Testing"""
    def __init__(self) -> None:
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __iter__(self):
        print(f'keys are = {self.data.keys()}')
        keys = list(self.data.keys())
        print(f'list of keys are {keys}')
        keys.sort()
        for key in keys:
            yield key

    def __delitem__(self, key):
        del self.data[key]
        
    def __len__(self):
        return len(self.data)

votes = {
    'otter': 1281,
    'polar bear': 589,
    'fox': 863
}

sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner_4(sorted_ranks)
print(winner)