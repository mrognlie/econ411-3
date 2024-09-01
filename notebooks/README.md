# Jupyter notebooks for lectures
This folder contains Jupyter notebooks that supplement the lecture materials. These notebooks fall into three categories:

- "Figures" notebooks for lectures 2, 4, 5, 6, 8, and 9 obtain the actual figures that included in the lecture slides for each. These are not as detailed or pedagogical as the other notebooks, but are included to make the lectures fully transparent. 
    * (Note that lecture 2 takes many figures from the lecture 3 Jupyter notebook in the main folder. The notebook here generates all other figures for lecture 2.)

- "Computations" notebooks for lectures 10 and 11 have code that implements the methods discussed in lectures 10 and 11, generating figures not included in the lecture notes themselves. These are a bit more pedagogical than the above.

- "Supplement" notebooks for lectures 3 and 7 are full-fledged mini-lectures in their own right. The lecture 3 supplement discusses how to profile and improve the speed of code, and underlies the `sim_steady_state_fast.py` module that we use for most of our work. The lecture 7 supplement covers "expectation functions", which are both useful in their own right and a key input to the "fake news algorithm" for rapidly computing sequence-space Jacobians.

**Note**: to run these notebooks, it is necessary to have the supporting modules from the main folder (`sim_steady_state.py`, `sim_steady_state_fast.py`, `life_cycle.py`, and `sim_fake_news.py`) in your Python search path. An easy way to do this is to copy the modules to the same directory as the notebooks.
