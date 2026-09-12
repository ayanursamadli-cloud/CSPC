# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup

Create the environment for a given lab:

conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- A radioactive decay simulation (`decay.py`) with two versions: a pure-Python loop and a vectorised NumPy version, plus tests and a speed comparison script.

**Speed comparison (loop vs NumPy):**
- loop : 2.7914 s
- numpy : 0.0003 s
- speed-up: 10095.2x faster

**Tests:** all passing? yes

**Conclusion:**
- The NumPy version is dramatically faster because it replaces the per-atom Python loop with a single vectorised `rng.binomial` call handled in optimized C code, instead of looping through every atom in the Python interpreter. I learned how much overhead pure-Python loops add at scale, and why vectorisation