# LAB - Class 42

## Project: Pythonisms

### Project Description

Includes examples demonstrating `pythonic` language features, such as:

- iterators/generators on a custom collection
- decorator that adds behavior to a given function
- dunder methods

Custom iterators can be very powerful for generating sequences or iterating over data in ways that are not easily achievable with built-in Python functions or loops. They provide a clear, concise way to encapsulate iteration logic within a class that can then be reused across projects.

In Python, a generator is a special type of iterator, a function that returns an iterator object. Generators simplify the creation of iterators by automatically implementing the `__iter__()` and `__next__()` methods with a simpler syntax. The key feature that distinguishes a generator from a regular function is the presence of one or more `yield` statements instead of a `return` statement. When a generator function calls `yield`, it produces a value to the caller and suspends its own execution, maintaining its state for when it's called again.

Decorators in Python are a very powerful and useful tool, allowing you to modify the behavior of a function or method without permanently modifying the function itself.

### Author: Rhett Chase

### Links and Resources

<!-- - [back-end server url](https://capital-finder-rhett-chase.vercel.app/api) -->
<!-- - [front-end application](http://xyz.com/) (when applicable) -->
- chatGPT
- [Dunder Methods](https://dbader.org/blog/python-dunder-methods)
- [Iterators](https://dbader.org/blog/python-iterators)
- [Generators](https://dbader.org/blog/python-generators)
- [Decorators](https://realpython.com/primer-on-python-decorators/)

### Setup

- `pip install -r requirements.txt`

#### `.env` requirements (where applicable)

<!-- i.e.
- `PORT` - Port Number
- `DATABASE_URL` - URL to the running Postgres instance/db -->
- N/A

#### How to initialize/run your application (where applicable)

- Clone repo
- Install dependencies (see above)
- Initiate virtual environment
- Run tests using the commands below
- For decorators, run the python interactive shell and use the functions

#### How to use your library (where applicable)

- N/A

#### Tests

- `pytest tests/test_repeater.py`
- `pytest tests/test_linked_list_iterator.py`
