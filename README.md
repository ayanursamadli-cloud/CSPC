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

Bonus: the 2D trajectory forms a figure-eight path; speed (sqrt(vx^2 + vy^2)) was computed via np.gradient on x and y separately.

## PW2 --- Lab B

In part 2 we use 3 different methods(gradient descent, Newton, SLSQP) to get the minimum, which we nailed it in easier landscape, f(x) = (x−3)²+1 all three reach approximately x = 3.
However in 2B g(x) = x⁴ − 3x² + x + 5 we see that at x0 = 0  newton method gives us a different result than others. Because newton method is not calculating the local minimum, it only calculates dg / dt = 0, which it can happen both local minimum and maximum, thats why in harder landscape we show the d(dg/dt)/dt and check if it is negative or positive. Choosing numbers for steps and l is a matter because from x0 = 2, gradient descent with l = 0.1 overshoots the nearby valley and ends at x ≈ −1.30, while l = 0.01 (with steps = 5000, since small steps need many iterations) converges to x ≈ 1.13. SLSQP also ended at x ≈ −1.30 from x0 = 2, so the result depends on the algorithm as well as the starting point.

In part 3, I have read the kinetics.csv file, set the t and C array and intialize and equilize C0 Tto the first value of C. and with total_error function I have calculated
the errors between guessed value and actual value and choose k which has the smalles error between actual value(the result k = 0.2618)
Note : at first I have mistyped exp(-k, t) so the value was high than I expected(approximately 1.6). after retyping it got 0.2618, which is the value we desired.

## Part 5 – Titration equivalence point

I read titration.csv, computed the slope dpH/dV with np.gradient, and  found the volume of maximum slope with, np.argmax. The equivalence point is  at about ... mL, where the pH curve jumps and its slope peaks (see titration.png).

## PW3 Dataset 1, Session 1

I loaded heart_disease_cleveland_new.csv with pandas (303 patients, 14 columns) and selected four continuous columns: age, chol, trestbps and thalach.  distributions.png shows 
a histogram of each of the four variables (20 bins each). age is approximatley bell shaped, chol is also appriximately bell shaped but left skewed, thalach is right skewed, and trasbps is left skewed.
For normality check I used two methods. First, I drew a Q-Q plot for each variable (qq.png), where points close to the straight line indicate normality. Second, I ran the Shapiro-Wilk test, where p < 0.05 means the variable is not normally distributed.
age	0.0061	not normal
chol	< 0.0001	not normal
trestbps	< 0.0001	not normal
thalach	0.0001	not normal
Conclusion. All four variables have p < 0.05, so none of them can be treated as normally distributed. In the Q-Q plot of chol, the points at the upper end rise above the line, which indicates a long right tail, so the variable is not normal. Because of this, in Session 2 I will use non-parametric methods (Mann-Whitney U and Spearman correlation) instead of the t-test and Pearson correlation.

## Session 2
Heart rate. Mann-Whitney U test (two-sided), chosen because `thalach` is not normal: U = 5806.5, p = 1.9e-13. Mean thalach: disease 139.3 ± 1.9 (SEM),
healthy 158.4 ± 1.5 (`means.png`). The error bars do not overlap, which agrees with the test: patients with heart disease reach a lower maximum heart rate.

Age vs thalach. Spearman rho = -0.39 (p = 1.5e-12): older patients tend to reach a lower maximum heart rate (moderate negative relationship,`age_thalach.png`).

Chemicals. Naively, cadmium (r = 0.88 with malignancy) looks far guiltier than benzene (r = 0.38). But pollution index correlates 0.98 with cadmium and
0.05 with benzene, so it may be a confounder. Restricting to similar pollution (40 < index < 60, n = 199):

Chemical  All data  Pollution held constant 
benzene   0.38      0.70 
cadmium   0.88      0.32 

Conclusion: benzene is the real cause. Cadmium only looked guilty because it
tracks pollution; its association collapses when pollution is controlled, while
benzene's survives.

Bonus: `target` proportions are 54.1% / 45.9%, Shannon entropy = 0.995 bits (max 1): almost perfectly balanced, so hard to guess.