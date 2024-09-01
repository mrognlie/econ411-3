# Econ 411-3: Macroeconomics with Heterogeneity
This repository has course materials for Econ 411-3, the third and final part of the first-year macro sequence and Northwestern, as taught in spring 2024.

The course covers a variety of topics but focuses on household-side heterogeneity and its consequences. It starts with the "standard incomplete markets" core, shows how that can be embedded in general equilibrium in different ways (e.g. Aiyagari vs. Bewley), discusses inequality and life-cycle forces, and then moves on to aggregate dynamics and HANK models. For the latter, it uses sequence-space Jacobians, which are useful in many ways: for obtaining solutions, understanding the propagation mechanism, and also implementing departures from full information and rational expectations.

The lectures themselves are located in the main folder of the repository, and take several forms: lectures 3 and 7 are Jupyter notebooks, the rest of lectures 1 through 9 are regular slides, and and lecture 10 through 12 are written notes. The `notebooks` subfolder contains additional Jupyter notebooks, including notebooks that generate all figures used in lectures, and also supplements for lectures 3 and 7. The `psets_and_review` subfolder contains three problem sets, along with review questions and solutions for the midterm and final.

The main folder also includes core Python modules that are called by notebooks:
- `sim_steady_state.py` (basic standard incomplete markets steady state code, developed in the Lecture 3 notebook)
- `sim_steady_state_fast.py` (a somewhat faster addition to `sim_steady_state.py`, developed in the Lecture 3 supplementary notebook in `notebooks`)
- `life_cycle.py` (very basic life-cycle model code, used in Lecture 6)
- `sim_fake_news.py` (basic code for implementing the fake news algorithm for sequence-space Jacobians in the SIM model, using algorithm described in Lecture 7)
