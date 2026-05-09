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

# Notes

- Searches are case-insensitive
- Inventory cannot become negative
- Data automatically loads on startup
- Data automatically saves on exit

---

# Example Session

```text
1. Add Item
Enter choice: 1

Item name: Apples
Initial value: 50

"Apples" added
```

```text
2. Update Stock
Enter choice: 2

Item name: Apples
Change amount: -15

"Apples" updated: 50 -> 35 (-15)
```

```text
3. View Stock
Enter choice: 3

Stock History for "Apples"

History : "[50, 35]"

Current : "35"
```

---

# Author

Python inventory tracker using object-oriented programming, abstract base classes, binary search, and merge sort.
