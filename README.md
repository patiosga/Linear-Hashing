# Linear Hashing

This project implements a Linear Hashing algorithm in Python. Linear Hashing is a dynamic hashing technique that allows the hash table to grow and shrink gracefully as the number of elements changes.

## Features

- Dynamic resizing of the hash table
- Efficient insertion, deletion, and search operations

## Installation

To use this project, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/Linear-Hashing.git
cd Linear-Hashing
```

## Usage

You can use the Linear Hashing implementation by importing the `LinearHashing` class from the module:

```python
from linear_hashing import LinearHashing

# Create a new Linear Hashing instance
hash_table = LinearHashing()

# Insert elements
hash_table.insert(key)

# Search for an element
value = hash_table.search(key)

# Delete an element
hash_table.delete(key)
```

## Example

Here is a simple example demonstrating how to use the Linear Hashing implementation:

```python
from linear_hashing import LinearHashing

# Create a new Linear Hashing instance
hash_table = LinearHashing()

# Insert elements
hash_table.insert(1)
hash_table.insert(2)

# Search for an element
print(hash_table.element_exists(1))  # Output: True

# Delete an element
hash_table.delete(1)
print(hash_table.element_exists(1))  # Output: False
```


