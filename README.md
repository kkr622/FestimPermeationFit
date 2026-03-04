# festim-permeation-fit

This project utilizes FESTIM to calculate the incident flux for permeation probes.

The calculation is performed by fitting FESTIM simulation results to experimental data using SciPy's optimization.

This project is based on [FESTIM-workshop
](https://github.com/festim-dev/FESTIM-workshop). For instructions on how to use FESTIM, please refer to the following sites:

- [FESTIM docs](https://festim.readthedocs.io/en/latest/)

- [FESTIM tutorial](https://festim-workshop.readthedocs.io/en/latest/intro.html)

## Local install

1. Clone this repo

```
git clone https://github.com/kkr622/FestimPermeationFit.git
```
2. Create Conda environment (requires conda)

```
conda env create -f environment.yml
```
```
conda activate festim-permeation-fit
```

4. Using pip

```
pip install -e .
```

5. You should then be able to execute the notebooks with the ``festim-permeation-fit`` environment
