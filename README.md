# Triangle Area Calculator

## Overview

This project is a simple Python program that calculates the area of a triangle using **Heron's Formula**. The user enters the lengths of the three sides of the triangle, and the program computes and displays the area rounded to two decimal places.

## Features

* Accepts the lengths of all three sides as input.
* Uses Heron's Formula to calculate the area.
* Displays the result rounded to two decimal places.
* Simple and beginner-friendly implementation.

## Formula Used

The program uses **Heron's Formula**:

```text
s = (a + b + c) / 2

Area = √(s × (s − a) × (s − b) × (s − c))
```

where:

* `a`, `b`, and `c` are the lengths of the three sides.
* `s` is the semi-perimeter of the triangle.

## Requirements

* Python 3.x

## Project Structure

```text
Triangle_Area_Calculator/
│── triangle_area.py
└── README.md
```

Replace `triangle_area.py` with the actual filename if it is different.

## How to Run

Clone the repository:

```bash
git clone https://github.com/KotapatiDhananjay/Repository-Name.git
```

Navigate to the project directory:

```bash
cd Repository-Name
```

Run the program:

```bash
python triangle_area.py
```

## Sample Output

```text
length of first side : 3
length of second side : 4
length of third side : 5
The area of the triangle is 6.0
```

## Concepts Covered

* Variables
* User Input
* Arithmetic Operations
* Mathematical Formulas
* Heron's Formula
* Output Formatting
* `round()` Function

## Author

Kotapati Dhananjay

GitHub: https://github.com/KotapatiDhananjay
