# Week 7 Lab Summary – Introduction to Programming

## Overview
This lab introduced two important Python collection data types: **Sets** and **Dictionaries**. The session focused on understanding their structure, properties, methods, and common use cases, along with comprehensions and comparison operations.

## Sets
Sets are unordered collections that store **unique, immutable values**. They are mutable as a collection but do not allow duplicate elements. Sets are highly efficient for membership testing and mathematical operations.

Key topics covered included:
- Creating sets using `{}` and the `set()` constructor
- Understanding unordered storage and automatic duplicate removal
- Membership testing using `in` and `not in`
- Creating empty sets using `set()`

## Set Comprehensions
Set comprehensions were introduced as a concise way to generate sets programmatically. They work similarly to list comprehensions but use curly braces `{}`.
- Generating unique values from sequences
- Filtering elements using `if` conditions
- Removing duplicates automatically

## Set Operations and Methods
The lab explored mathematical set operations using both **operators** and **methods**, including:
- Union (`|`, `union()`)
- Intersection (`&`, `intersection()`)
- Difference (`-`, `difference()`)
- Symmetric Difference (`^`, `symmetric_difference()`)

Both accessor operations (returning new sets) and mutator operations (modifying sets in-place using methods like `update()` and `difference_update()`) were practiced.

## Set Comparisons
Set comparison operations were used to test relationships between sets:
- Subset and proper subset (`<`, `<=`)
- Superset and proper superset (`>`, `>=`)
- Equivalent methods such as `issubset()` and `issuperset()`

## Immutable Sets (frozenset)
The concept of immutable sets was introduced using the `frozenset()` constructor. Unlike regular sets, frozensets cannot be modified after creation, but they still support accessor operations and comparisons.

## Dictionaries
Dictionaries store data as **key:value pairs**, allowing fast access to values using unique keys. Dictionaries are ordered and mutable.

Topics included:
- Creating dictionaries using `{}` and the `dict()` constructor
- Adding, updating, and accessing key:value pairs
- Membership testing using dictionary keys
- Understanding keys as unique identifiers

## Dictionary Comprehensions
Dictionary comprehensions were used to generate dictionaries efficiently by mapping keys to values programmatically, such as mapping numbers to their square roots.

## Dictionary Methods
Common dictionary methods were explored, including:
- `get()`, `copy()`, `clear()`
- `pop()`, `popitem()`
- `update()`

These methods were used to safely access, modify, and manage dictionary contents.

## Iterating Over Dictionaries
Different ways to iterate over dictionaries were practiced:
- Iterating over keys
- Iterating over values using `values()`
- Iterating over key:value pairs using `items()` and sequence unpacking

## Key Terminology
This lab reinforced understanding of the following concepts:
- **Set**
- **Set Operations**
- **Set Comprehension**
- **Dictionary**
- **Key:Value Pair**

## Conclusion
Overall, this lab improved understanding of Python’s collection types and their practical applications. Sets and dictionaries provide efficient ways to manage unique data and structured key-based data, which are essential skills for effective Python programming.