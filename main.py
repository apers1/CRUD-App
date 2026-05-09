from abc import ABC, abstractmethod
import csv
import ast
import os


class InventoryOperations(ABC):

    # primary structure: list of tuples name of item + inventory over time(str, list[int])

    @property
    @abstractmethod
    def data(self) -> list[tuple[str, list[int]]]:
        # subclass you make gives the list
        pass

    def load_inventory(self, filename="inventory.csv"):

        if not os.path.exists(filename):
            return

        with open(filename, "r", newline="") as f:

            reader = csv.reader(f)

            next(reader, None)

            for row in reader:

                if len(row) < 2:
                    continue

                name = row[0]

                try:
                    history = ast.literal_eval(row[1])
                    if not isinstance(history, list):
                        history = [int(history)]
                except:
                    try:
                        history = [int(row[1])]
                    except:
                        history = []

                self.items.append((name, history))

        self.items = self.merge_sort(self.items)

    # porter required
    def add(self, name: str, value: int):
        # do not add and then do merge sort. instead, use the binary search method to find if there is a match for name. if not, find the optimal index to put it in using a modified binary search

        match = self.search(name)

        if match is not None:
            self.data[match][1].append(value)

        else:
            # no match, find insertion point using binary search
            start = 0
            end = len(self.data)

            while start < end:
                # do not let it equal
                mid = (start + end) // 2

                if self.data[mid][0].lower() < name.lower():
                    start = mid + 1
                else:
                    end = mid

            # inserts the value at proper index based on the fact that the binary search found the name before it
            self.data.insert(start, (name, [value]))

    def search(self, item: str) -> int | None:
        start = 0
        end = len(self.data) - 1

        while start <= end:
            # while we arent too far
            mid = (start + end) // 2

            # grab mid value
            curr_name = self.data[mid][0]

            # if mid value is equal to what look for return
            if curr_name.lower() == item.lower():
                return mid

            # if abcd value is less then look in right side
            elif curr_name.lower() < item.lower():
                start = mid + 1

            # abcd value greater look left
            else:
                end = mid - 1

        # not found
        return None

    def calculate_prediction(self, name: str):

        # first - last over period
        item = self.search(name)

        if item is None:
            return f'Item "{name}" not found'

        item_hist = self.data[item][1]

        if len(item_hist) < 2:
            return f'Item "{name}" not enough data'

        loss = item_hist[0] - item_hist[-1]
        period = len(item_hist) - 1
        burn_rate = loss / period

        # return before trying to divide by zero
        if burn_rate <= 0:
            return f'Item "{name}" has predicted infinite time left (no use)'

        time_remaining = item_hist[-1] / burn_rate

        return f'Item "{name}" has approximately {time_remaining:.2f} periods left'

    # Existing item functions other necessary
    def remove_item(self, name: str):

        # use search to find index of item
        idx = self.search(name)

        if idx is None:
            print(f'"{name}" not found.')
            return

        # remove tuple at that index
        self.data.pop(idx)

        # print that it was removed "{name} removed\n"
        print(f'"{name}" removed')

    def merge_sort(
            self,
            lst: list[tuple[str, list[int]]]
    ) -> list[tuple[str, list[int]]]:

        if len(lst) <= 1:
            return lst

        mid = len(lst) // 2

        L = self.merge_sort(lst[:mid])
        R = self.merge_sort(lst[mid:])

        return self.merge(L, R)

    def merge(
            self,
            left: list[tuple[str, list[int]]],
            right: list[tuple[str, list[int]]]
    ) -> list[tuple[str, list[int]]]:

        result = []

        i = 0
        j = 0

        while i < len(left) and j < len(right):

            if left[i][0].lower() <= right[j][0].lower():
                result.append(left[i])
                i += 1

            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def see_current_stock(self, name: str):

        # binary search and print item price history
        ind = self.search(name)

        if ind is None:
            print(f'"{name}" not found.')
            return

        item_name, history = self.data[ind]

        curr = history[-1] if history else 0

        print(f'\n Stock History for "{item_name}"')
        print(f'\n History : "{history}"')
        print(f'\n Current : "{curr}"')

    def update_stock(self, name: str, change: int):

        # use search to find item index
        ind = self.search(name)

        if ind is None:
            print(f'"{name}" not found.')
            return

        # update integer value
        item_name, history = self.data[ind]

        current = history[-1] if history else 0

        # stock can't go below 0
        new_value = max(0, current + change)

        history.append(new_value)

        direction = "+" if change >= 0 else ""

        print(f'"{name}" updated: {current} -> {new_value} ({direction}{change})')

    def get_inventory(self):

        # for item in list:
        # write to csv "{item[0]}, {item[1]}"

        with open("inventory.csv", "w", newline="") as f:
            writer = csv.writer(f)

            writer.writerow(["Name", "Inventory History"])

            writer.writerows([[name, history] for name, history in self.data])


class Stock(InventoryOperations):
    def __init__(self):
        self.items = []

        self.load_inventory()

    @property
    def data(self) -> list[tuple[str, list[int]]]:
        return self.items


try:
    new_stock = Stock()

    while True:

        print("\n1. Add Item")
        print("2. Update Stock")
        print("3. View Stock")
        print("4. Remove Item")
        print("5. Predict Item")
        print("6. Show All")
        print("7. Save")
        print("8. Exit")
        choice = input("\nEnter choice: ")

        if choice == "1":
            name = input("Item name: ")
            value = int(input("Initial value: "))
            new_stock.add(name, value)
            print(f'"{name}" added')

        elif choice == "2":
            name = input("Item name: ")
            change = int(input("Change amount: "))
            new_stock.update_stock(name, change)

        elif choice == "3":
            name = input("Item name: ")
            new_stock.see_current_stock(name)

        elif choice == "4":
            name = input("Item name: ")
            new_stock.remove_item(name)

        elif choice == "5":
            name = input("Item name: ")
            print(new_stock.calculate_prediction(name))

        elif choice == "6":
            [print(item) for item in new_stock.items]

        elif choice == "7":
            new_stock.get_inventory()
            print("inventory saved")

        elif choice == "8":
            new_stock.get_inventory()
            print("inventory saved before exit")

            break
        else:
            print("invalid option")

except Exception as e:
    print("something failed i guess " + str(e))