# A Simple FizzBuzz App

## Please switch to develop branch to clone this repo

This repo contains a simple fizzbuzz app which takes two integers between 1 and 100 and loops from the first to the second outputting each integer. During iteration if an integer is divisible by 3 "fizz" is printed out, if integer is divisible by 5 "buzz" is printed out.

## Repository Structure
* `app`: contains code for the fizzbuzz app
    * `enums`: contains enums unse dto unify output
    * `test`: contains all test
    * `fizz_buzz`: the main fizz_buzz module which handles the business logic
    * `main`: entry point into application

## Branches

This repo maintains 2 active branches
* `develop`: this is serving as the development/feature branch on which the app was built
* `main`: the final branch which accepts changes from develop

## Run Unit Tests

To run all unit test, use the command below, make sure create a virtual env and install the specified requirement in the `test-requirements.txt` file
* `pytest ./app/tests/`


## Run locally
win - `python main.py`
mac - `python3 main.py`
