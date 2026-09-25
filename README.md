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

**Reproducibility check:**
- My partner cloned my CSPC repository, created the environment from my
  environment.yml, activated it, and ran `pytest -v` on their machine with
  no changes — everything worked correctly (all tests passed).

**Conclusion:**
- The NumPy version is dramatically faster because it replaces the per-atom Python loop with a single vectorised `rng.binomial` call handled in optimized C code, instead of looping through every atom in the Python interpreter. I learned how much overhead pure-Python loops add at scale, and why vectorisation


## PW1 --- Lab B

Obsevred decay data was compared against the analytical law N0*exp(-lambda * t) with lambda = 0.3. The observed points closely follow the analytical curve, confirming exponential decay behaviour. The Snakemake pipeline runs plot.py to regenerete figure.png 
from decay_observed.csv, rebuilding it only when the CSV or script has changed.

## PW2 --- Lab A

Measured mean acceleration: -8.58 m/s^2 (std dev: 28.72 m/s^2)
The acceleration is far noisier than the position because differentiation amplifies noise: it compares nearby points, and small measurement errors become large relative changes once divided by the small time step. Since acceleration required two successive differentiations of the position data, the noise was amplified twice, which is why its standard deviation (~28.7) is so large even though the position itself looked smooth. Integrating the noisy acceleration back up to velocity and then position recovered the original trajectory to within 0.78 m — showing that integration (a running sum) partially cancels out random noise, the opposite effect of differentiation.