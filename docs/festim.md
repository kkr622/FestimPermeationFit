# FESTIM

## Overview

This project is based on [FESTIM-workshop
](https://github.com/festim-dev/FESTIM-workshop). For instructions on how to use FESTIM, please refer to the following sites:

- [FESTIM docs](https://festim.readthedocs.io/en/latest/)

- [FESTIM tutorial](https://festim-workshop.readthedocs.io/en/latest/intro.html)

## Temporal Variation of Incident Flux

The `Piecewise` function is used to vary the incident flux over time in FESTIM. Please note that this implementation differs from the conventional method of providing time and data as simple lists.

\[
\Gamma(t) = 
\begin{cases} 
\Gamma_{1} & \text{if } 0 \le t \le dt \\
\Gamma_{2} & \text{if } dt < t \le 2dt \\
\vdots \\
\Gamma_{n} & \text{if } (n-1)dt < t \le n \cdot dt
\end{cases}
\]

The code for generating `Piecewise` expressions according to the specified time step (`dt`) in the optimization calculation can be found in `src/piecewise.py`.