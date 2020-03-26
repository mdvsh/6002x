# reimplementation of lect1.py for better understanding.

class Food(object):
    def __init__(self, v, n, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def getCost(self):
        return self.calories
    def ratio(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ' : (' + str(self.value) + ', ' + str(self.calories) + ')'

def menuBuilder(names, values, calories):
    '''
    names, values ans weights are lists of same length
    :param name:
    :param values:
    :param weights:
    :return: list of foods
    '''
    menu = []
    for i in range(len(values)):
        menu.append(Food(values[i], names[i], calories[i]))
    return menu

def greedyAlgo(items, constraint, keyFunc):
    '''
    :param items: list to apply greedy algo to
    :param constraint: to abide by (>= 0)
    :param keyFunc: maps elements of items to nums
    :return: result, totalValue of items taken
    '''
    itemCopy = sorted(items, key=keyFunc, reverse=True)
    totalValue, totalCost = 0.0, 0.0
    result = []
    for i in range(len(itemCopy)):
        if (totalCost+itemCopy[i].getCost()) <= constraint:
            result.append(itemCopy[i])
            totalCost += itemCopy[i].getCost()
            totalValue += itemCopy[i].getValue()
    return (result, totalValue)

def test(items, constraint, keyFunc):
    took, val = greedyAlgo(items, constraint, keyFunc)
    print('Total value of items taken : ', val)
    for item in took:
        print('     ', item)

def tester(foods, maxUnits):
    '''
    collection of tester functions on different parameters of greedy.
    '''
    print('Use greedy by value to allocate', maxUnits, 'calories')
    test(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits, 'calories')
    test(foods, maxUnits, lambda x: 1/Food.getCost(x))
    print('\nUse greedy by ratio of value to cost to allocate', maxUnits, 'calories')
    test(foods, maxUnits, Food.ratio)

names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]

foods = menuBuilder(names, values, calories)
tester(foods, 500)
print()

# the below variables are for cross checking my answers to a finger exercise.
item = ['clock', 'picture', 'radio', 'vase', 'book', 'computer']
dollars = [175,90,20,50,10,200]
weights = [10,9,4,2,1,20]
burglar_item_list = menuBuilder(item, dollars, weights)
tester(burglar_item_list, 20)
