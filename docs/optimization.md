# Optimization

## Overview

The calculation is performed by fitting FESTIM simulation results to experimental data using SciPy's optimization.

## Method

The optimal incident flux was determined by minimizing the \(\chi^2\) value, defined by the following equation, through iterative calculations. This calculation is defined in `src/optimize.py`.

\[
\chi^2 = \left( \frac{\Gamma_{calc} - \Gamma_{exp}}{\Gamma_{exp}} \right)^2
\]

### Parameter Definitions:
- **\(\Gamma_{exp}\)**: Experimental value
- **\(\Gamma_{calc}\)**: Calculated value
