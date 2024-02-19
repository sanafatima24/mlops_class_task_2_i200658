# MLOps Class Task

This repository contains code for the MLOps class task. It includes a Python class `StudentsInMLOps` with methods for managing students in an MLOps class, along with test cases to ensure its correctness.

## Installation

To set up the project, follow these steps:

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd mlops_class_task
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can use the `StudentsInMLOps` class in your Python code by importing it from the `main` module. Here's an example:

```python
from main import StudentsInMLOps

# Create an instance of the class
ml_ops_class = StudentsInMLOps()

# Enroll students
ml_ops_class.enrollStudents(20)

# Drop students
ml_ops_class.dropStudents(5)

# Get total strength
total_strength = ml_ops_class.getTotalStrength()
print("Total strength:", total_strength)

# Get class name
class_name = ml_ops_class.getClassName()
print("Class name:", class_name)
