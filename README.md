# Noisy Trade

## How To Run

Create a python virtual environment and install the requirements from `requirements.txt`.

After you have cloned the repository, run the following commands in the root directory of the project.

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

To run the project, run the following command in the root directory of the project.

```bash
python3 src/main.py
```

## Project Structure

The project is structured as follows:

```
.
├── data                       # Data directory
│   ├── ^NSEI.csv
├── results                    # Results directory
├── src                        # Source code directory
│   ├── main.py                # Main file
│   ├── lib                    # Library directory
│   │   ├── __init__.py
│   │   ├── indicators         # Indicators directory
│   │   │   ├── __init__.py
│   │   │   ├── Average.py     # Average indicator
│   │   ├── strategies         # Strategies directory
│   │   │   ├── __init__.py
│   │   │   ├── MovingAverageCrossover.py # Moving Average Crossover strategy
│   │   ├── utils.py           # Utils
├── README.md
├── requirements.txt
└── .gitignore
```