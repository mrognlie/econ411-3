# Econ 411-3: Macroeconomics with Heterogeneity
This repository has course materials for Econ 411-3, the third and final part of the first-year macro sequence and Northwestern, as taught in spring 2024. The full repository [can be downloaded as a ZIP here](https://github.com/mrognlie/econ411-3/archive/refs/heads/main.zip). Note that some browsers may have trouble previewing these PDFs if you click on the files above; if so, you can click on the links for each lecture in the outline below, or just download the repository. You can also [visit my general teaching page here](https://sites.northwestern.edu/rognlie/teaching/).

The course covers a variety of topics but focuses on household-side heterogeneity and its consequences. It starts with the "standard incomplete markets" core, shows how that can be embedded in general equilibrium in different ways (e.g. Aiyagari vs. Bewley), discusses inequality and life-cycle forces, and then moves on to aggregate dynamics and HANK models. For the latter, it uses sequence-space Jacobians, which are useful in many ways: for obtaining solutions, understanding the propagation mechanism, and also implementing departures from full information and rational expectations.

### Organization

The lectures themselves are located in the main folder of the repository, and take several forms: lectures 3 and 7 are Jupyter notebooks, the rest of lectures 1 through 9 are regular slides, and and lecture 10 through 12 are written notes. The `notebooks` subfolder contains additional Jupyter notebooks, including notebooks that generate all figures used in lectures (briefer and less pedagogical than the other notebooks), and also supplements for lectures 3 and 7. The `psets_and_review` subfolder contains three problem sets, along with review questions and solutions for the midterm and final.

The main folder also includes core Python modules that are called by notebooks:
- [`sim_steady_state.py`](https://github.com/mrognlie/econ411-3/blob/main/sim_steady_state.py) (basic standard incomplete markets steady state code, developed in the Lecture 3 notebook)
- [`sim_steady_state_fast.py`](https://github.com/mrognlie/econ411-3/blob/main/sim_steady_state_fast.py) (a somewhat faster addition to `sim_steady_state.py`, developed in the Lecture 3 supplementary notebook in `notebooks`)
- [`life_cycle.py`](https://github.com/mrognlie/econ411-3/blob/main/life_cycle.py) (very basic life-cycle model code, used in Lecture 6)
- [`sim_fake_news.py`](https://github.com/mrognlie/econ411-3/blob/main/sim_fake_news.py) (basic code for implementing the fake news algorithm for sequence-space Jacobians in the SIM model, using algorithm described in Lecture 7)

The topics of each lecture are:

- [Lecture 1:](https://mrognlie.github.io/econ411-3/econ411_3_lecture1.pdf) Course overview
- [Lecture 2:](https://mrognlie.github.io/econ411-3/econ411_3_lecture2.pdf) The standard incomplete markets (SIM) model \[most figures from lecture 3, [notebook w/extra figures](https://github.com/mrognlie/econ411-3/blob/main/notebooks/econ411_3_lecture2_extrafigures.ipynb)\]
- [Lecture 3:](https://github.com/mrognlie/econ411-3/blob/main/econ411_3_lecture3.ipynb) Computing the steady state of the SIM model \[[supplementary notebook on speeding up code](https://github.com/mrognlie/econ411-3/blob/main/notebooks/econ411_3_lecture3_supplement_speed.ipynb)\]
- [Lecture 4:](https://mrognlie.github.io/econ411-3/econ411_3_lecture4.pdf) General equilibrium in the SIM model \[[notebook w/figures](https://github.com/mrognlie/econ411-3/blob/main/notebooks/econ411_3_lecture4_figures.ipynb)\]
- [Lecture 5:](https://mrognlie.github.io/econ411-3/econ411_3_lecture5.pdf) The Pareto distribution and fat tails for income and wealth \[[notebook w/figures](https://github.com/mrognlie/econ411-3/blob/main/notebooks/econ411_3_lecture5_figures.ipynb)\]
- [Lecture 6:](https://mrognlie.github.io/econ411-3/econ411_3_lecture6.pdf) Life-cycle / OLG models \[[notebook w/figures](https://github.com/mrognlie/econ411-3/blob/main/notebooks/econ411_3_lecture6_figures.ipynb)\]
- [Lecture 7:](https://github.com/mrognlie/econ411-3/blob/main/econ411_3_lecture7.ipynb) Dynamics and sequence-space Jacobians in the SIM model \[[supplementary notebook on expectation functions](https://github.com/mrognlie/econ411-3/blob/main/notebooks/econ411_3_lecture7_supplement_expfunctions.ipynb)\] \[[supplement on fake news algorithm](https://mrognlie.github.io/econ411-3/econ411_3_lecture7_supplement.pdf)\]
- [Lecture 8:](https://mrognlie.github.io/econ411-3/econ411_3_lecture8.pdf) Introduction to HANK and fiscal policy \[[notebook w/figures](https://github.com/mrognlie/econ411-3/blob/main/notebooks/econ411_3_lecture8_figures.ipynb)\]
- [Lecture 9:](https://mrognlie.github.io/econ411-3/econ411_3_lecture9.pdf) Introduction to monetary policy in HANK \[[notebook w/figures](https://github.com/mrognlie/econ411-3/blob/main/notebooks/econ411_3_lecture9_figures.ipynb)\]
- [Lecture 10:](https://mrognlie.github.io/econ411-3/econ411_3_lecture10.pdf) Departing from full information and rational expectations (“FIRE”) \[[notebook w/figures](https://github.com/mrognlie/econ411-3/blob/main/notebooks/econ411_3_lecture10_computations.ipynb)\]
- [Lecture 11:](https://mrognlie.github.io/econ411-3/econ411_3_lecture11.pdf) Models of pricing and inflation \[[notebook w/figures](https://github.com/mrognlie/econ411-3/blob/main/notebooks/econ411_3_lecture11_computations.ipynb)\]
- [Lecture 12:](https://mrognlie.github.io/econ411-3/econ411_3_lecture12.pdf) Multiple sectors in an input-output network

Problem sets and review materials:

- [Problem set 1](https://mrognlie.github.io/econ411-3/psets_and_review/econ411_3_ps1.pdf), [Problem set 2](https://mrognlie.github.io/econ411-3/psets_and_review/econ411_3_ps2.pdf), [Problem set 3](https://mrognlie.github.io/econ411-3/psets_and_review/econ411_3_ps3.pdf)
- [Midterm review questions](https://mrognlie.github.io/econ411-3/psets_and_review/econ411_3_midterm_review_questions.pdf) and [solutions](https://mrognlie.github.io/econ411-3/psets_and_review/econ411_3_midterm_review_solutions.pdf)
- [Final review questions](https://mrognlie.github.io/econ411-3/psets_and_review/econ411_3_final_review_questions.pdf) and [solutions](https://mrognlie.github.io/econ411-3/psets_and_review/econ411_3_final_review_solutions.pdf)

### Technical requirements and other materials
The Jupyter notebooks and modules require Python and the `numpy`, `scipy`, `matplotlib`, and `numba` libraries.

For closely related materials, please take a look at our [2023 NBER workshop page](https://github.com/shade-econ/nber-workshop-2023/tree/main), which includes recordings where I cover the computational material in Lecture 3 (and expectation functions in the supplement to Lecture 7).
