# 0x00-pascal_triangle

Welcome to the "0x00-pascal_triangle" directory!

## Description

This directory contains Python code to generate Pascal's triangle. Pascal's triangle is a triangular array of binomial coefficients, named after the French mathematician Blaise Pascal. Each number in the triangle is the sum of the two numbers directly above it in the previous row.

## Files

* `0-pascal_triangle.py`: This Python script contains a function to generate Pascal's triangle given the number of rows as input. The function returns Pascal's triangle as a list of lists.

## Usage

To generate Pascal's triangle, you can use the provided Python script `0-pascal_triangle.py`. Import the `pascal_triangle` function and call it with the desired number of rows. Example usage:

```python
from 0-pascal_triangle import pascal_triangle

num_rows = 5
triangle = pascal_triangle(num_rows)
print(triangle)
