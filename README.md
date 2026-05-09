# Inventory Tracker

A simple Python inventory management system that stores stock history, supports searching and sorting, and saves data to a CSV file.

---

# Features

- Add inventory items
- Update stock values
- View stock history
- Remove items
- Predict remaining stock lifespan
- Automatic CSV save/load
- Binary search for fast lookup
- Merge sort for alphabetical organization
- List comprehension using Pythonic idioms

---

# Requirements

- Python 3.10+

No external libraries are required.

---

# Run the Program

Save the file as:

```bash
inventory.py
```

Run with:

```bash
python inventory.py
```

---

# Menu Options

When the program starts, you will see:

```text
1. Add Item
2. Update Stock
3. View Stock
4. Remove Item
5. Predict Item
6. Show All
7. Save
8. Exit
```

Enter the number of the action you want to perform.

---

# How to Use

## Add Item

Adds a new inventory item.

Example:

```text
Item name: Apples
Initial value: 50
```

---

## Update Stock

Changes the current stock amount.

Example:

```text
Item name: Apples
Change amount: -10
```

- Negative numbers decrease stock
- Positive numbers increase stock
- Stock never goes below 0

---

## View Stock

Displays:

- Inventory history
- Current stock amount

Example output:

```text
Stock History for "Apples"

History : "[50, 40, 60]"

Current : "60"
```

---

## Remove Item

Deletes an item from inventory.

Example:

```text
Item name: Apples
```

Output:

```text
"Apples" removed
```

---

## Predict Item

Estimates how long the stock will last based on previous inventory changes.

Example:

```text
Item "Apples" has approximately 4.50 periods left
```

---

## Show All

Displays all inventory items and their histories.

Example:

```python
('Apples', [50, 40, 60])
('Bananas', [30, 20, 10])
```

---

## Save

Saves all inventory data to:

```text
inventory.csv
```

---

## Exit

Automatically saves inventory before closing the program.

---

# Inventory File Format

Data is stored in:

```text
inventory.csv
```

Example:

```csv
Name,Inventory History
Apples,"[50, 40, 60]"
Bananas,"[30, 20, 10]"
```

---

# Data Structure

Inventory is stored as:

```python
list[tuple[str, list[int]]]
```

Example:

```python
[
    ("Apples", [50, 40, 60]),
    ("Bananas", [30, 20, 10])
]
```

---

# Algorithms Used

## Binary Search

Used for:
- Fast item lookup
- Fast insertion into sorted inventory

## Merge Sort

Used to:
- Keep inventory alphabetically sorted

---

# Time Complexity

## Binary Search

Used in:
- `search()`
- insertion logic in `add()`

Time Complexity:

- Best Case: `O(1)`
- Average Case: `O(log n)`
- Worst Case: `O(log n)`

---

## Merge Sort

Used in:
- `merge_sort()`

Time Complexity:

- Best Case: `O(n log n)`
- Average Case: `O(n log n)`
- Worst Case: `O(n log n)`

Space Complexity:

- `O(n)`

---

## Updating Stock

Used in:
- `update_stock()`

Time Complexity:

- Search: `O(log n)`
- Append to history: `O(1)`

Total:

- `O(log n)`

---

## Adding Items

Used in:
- `add()`

Time Complexity:

- Binary search lookup: `O(log n)`
- List insertion: `O(n)`

Total Worst Case:

- `O(n)`

(The insertion itself shifts elements in the list.)

---

# Notes

- Searches are case-insensitive
- Inventory cannot become negative
- Data automatically loads on startup
- Data automatically saves on exit

---

# Author
apers1 and USeung1
## TLDR;
Python inventory tracker using object-oriented programming, abstract base classes, binary search, and merge sort.
