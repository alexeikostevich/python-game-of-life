# Conway's Game of Life
[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) in Python 3.6.

```python
# Simulate 'The Game of Life' for a 10 x 10 grid
for world in Life.of_random_world(10, 10):
    print(world)
    input('Press Enter to continue...')
```

## Demo
```bash
# Requires a Posix-compatible terminal (Linux or OS X)
$ python3 main.py
```

## Technology Stack
|                      | Technology                                         |
| -------------------- |----------------------------------------------------|
| Language             | [Python 3.6](https://www.python.org/)              |
| Linter               | [Flake8 3.5](http://flake8.pycqa.org/en/latest/)   |

## Development
### Prerequisites
1. [Python 3.6](https://www.python.org/downloads/)

### Quickstart
1. [Creates and activates](https://docs.python.org/3/library/venv.html) a Python virtual environment

```bash
$ python3 -m venv .venv
$ . .venv/bin/activate
```

2. Install dependencies

```bash
$ pip install -r requirements.txt
```

### Styleguide
The project uses [PEP8](https://www.python.org/dev/peps/pep-0008/). [Flake8](http://flake8.pycqa.org/en/latest/) is setup to enforce the rules.

```bash
$ flake8
```
