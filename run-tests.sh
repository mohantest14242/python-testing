#!/bin/bash

# Set PYTHONPATH to include the directory of main.py
export PYTHONPATH=$PYTHONPATH:$(pwd)/../actions/src

# Navigate to pytest directory and run tests
cd tests
echo "Running pytest tests..."
pytest || { echo "Pytest tests failed"; exit 1; }
cd ..

# Navigate to unittest directory and run tests
cd unittest
echo "Running unittest tests..."
python -m unittest discover || { echo "Unittest tests failed"; exit 1; }
cd ..

echo "All tests executed."
