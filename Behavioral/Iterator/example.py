class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return "{}: $ {}".format(self.name, self.price)


class BaseIterator:
    def has_next(self):
        pass

    def next(self):
        pass

    def has_prev(self):
        pass

    def prev(self):
        pass


class MenuIterator(BaseIterator):
    def __init__(self, items):
        self.index = 0
        self.items = items

    def has_next(self):
        return False if self.index >= len(self.items) else True

    def has_prev(self):
        return True if self.index >= len(self.items) else False

    def next(self):
        menu_item = self.items[self.index]
        self.index += 1
        return menu_item

    def prev(self):
        menu_item = self.items[self.index - 2]
        self.index += -1
        return menu_item

    def remove(self):
        return self.items.pop()


class BaseMenu:
    def iterator(self):
        pass


class Menu(BaseMenu):
    def __init__(self):
        self.items = []

    def add(self, menu_item):
        self.items.append(menu_item)

    def iterator(self):
        return MenuIterator(self.items)


if __name__ == '__main__':
    i1 = Item("spaghetti", 7.50)
    i2 = Item("hamburger", 6.00)
    i3 = Item("chicken sandwich", 6.50)

    menu = Menu()
    menu.add(i1)
    menu.add(i2)
    menu.add(i3)

    print("Displaying Menu:")
    iterator = menu.iterator()

    while iterator.has_next():
        item = iterator.next()
        print(item)

    print("Removing last item returned")
    iterator.remove()

    print("Displaying Menu:")
    # iterator = menu.iterator()
    while iterator.has_prev():
        item = iterator.prev()
        print(item)
