import numpy as np
from math import sqrt
from galopy import *

if __name__ == "__main__":
    # Initialize parameters
    min_probability = 1.0
    n_offsprings = 600
    n_elite = 200
    n_generations = 1000

    # Gate represented as a matrix
    matrix = np.array([[1. / sqrt(3.),          1. / sqrt(3.),          1. / sqrt(3.)],
                       [1. / sqrt(3.), -0.5 / sqrt(3.) + 0.5j, -0.5 / sqrt(3.) - 0.5j],
                       [1. / sqrt(3.), -0.5 / sqrt(3.) - 0.5j, -0.5 / sqrt(3.) + 0.5j]])
    # State modes:
    # (2)----------
    # (1)----------
    # (0)----------
    basic_states = np.array([[2],
                             [1],
                             [0]])
    # Create an instance of search
    search = CircuitSearch('cpu', matrix, input_basic_states=basic_states, depth=3,
                           n_ancilla_modes=0, n_ancilla_photons=0)
    # Launch the search!
    circuit = search.run(min_probability, n_generations, n_offsprings, n_elite)

    # Save result
    circuit.to_loqc_tech("result.json")
