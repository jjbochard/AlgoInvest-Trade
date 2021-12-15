# AlgoInvest-Trade
## Table of contents
- [Table of content](#table-of-content)
- [Foreword](#foreword)
- [Installation](#installation)
- [How to use](#how-to-use)
- [Possible improvements](#possible-improvements)

## Foreword

The aim of these programs is write algorithms in order to maximise profit for a list of actions and with a limit of investment

First, I had to a program which tests all the possibilities.

Secondly, I had to find a solution to decrease the time of execution of the the first algorithm.
I could choose different approximate solution but I choose to solve the problem using dynamic programmation

The problem I have to solve is knapsack problem. For more information, check [here](https://en.wikipedia.org/wiki/Knapsack_problem)
## Installation
### Clone the code source (using ssh)

    mkdir foo
    git clone git@github.com:jjbochard/P07_AlgoInvest-Trade.git foo
    cd foo

### Create your virtual environnement

First, install [Python 3.6+](https://www.python.org/downloads/).

Then, create your virtual environnement :

    python3 -m venv <your_venv_name>

Activate it :

- with bash command prompt

        source <your_venv_name>/bin/activate

- or with Windows PowerShell

        .\venv\Scripts\activate

Finally, install required modules

    pip3 install -r requirements.txt

To deactivate your venv :

    deactivate

### Optionnal : configure your git repository with pre-commit (if you want to fork this project)

You can install the configured pre commit hook with

    pre-commit install

## How to use

+ Run the programs

To run bruteforce solution, use :

    make bruteforce

To run optimized solution, use :

    make optimized

To run sienna1 solution, use :

    make sienna1

To run sienna2 solution, use :

    make sienna2

To run both sienna solution, use :

    make all_sienna


## Possible improvements

* I can save more seconds of execution using a matrice with only 2 rows (or even 1) but I think it's not worth it here

* I can prove than P = NP in order to add 1 000 000 dollars to my bank account
