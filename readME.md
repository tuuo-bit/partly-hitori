# Partly Hitori

**Brute Force Algorithm that Solves (almost) your Hitori Puzzle**

Having decided to hard code an algorithm that would solve the [Hitori](https://en.wikipedia.org/wiki/Hitori) puzzle, I came to realize that it is a NP-Complete problem just to shatter any hope I had to complete this project.

With the help of this [site](https://www.conceptispuzzles.com/index.aspx?uri=puzzle/hitori/techniques), I managed to put together few basic solving stratergies to code in the form of functions as *markUnique*, *markTriple*, *markBetweenPair* and *pairInduction*.

## Get Started

[Demo](https://youtu.be/grAUYCnaC3k)

Left Entry widget takes space separated perfect square number of values arranged to represent the Hitori grid.

The run ">" button will produce the solution output of size that of the input array with "X" for blacked out numbers and "O" for safe numbers.

A completely solved output would have only "X"s and "O"s. Numbers that show up in the output require stratergies that are not included in this algorithm.

## Libraries and Modules

* Python 3.12.3
* numpy 1.26.4
* math
* tkinter
