# Introduction

Followed Richard Wells's Supermarket exercise to better understand unit testing in Python with pytest.
Tried to use pytest-html as well.
Course name: Unit Testing and Test Driven Development in Python.

## Requirements
1. pytest:
    pip install pytest
2. pytest-html:
    pip intall pytest-html

## Notes:
While trying pytest-html, it gave file not found error, found a way around it using:

1. open git and cd into the directory of your project
2. command: python -m pytest --html=./report.html