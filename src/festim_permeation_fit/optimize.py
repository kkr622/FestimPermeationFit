import numpy as np
from IPython.utils.capture import capture_output
from .piecewise import compress_piecewise 
import festim as F

def optimize_flux(Gi, G_fixed, i, experimental_flux, params):
    """
    params: dict { 'model': ..., 'dq': ..., 'Nt': ..., 'inc_amp': ..., 'dt': ..., 'ku': ..., 'kd': ... }
    """
    Gi = float(Gi)
    
    model = params['model']
    dq = params['dq']
    Nt = params['Nt']
    inc_amp = params['inc_amp']
    dt = params['dt']
    
    G_trial = np.array(G_fixed + [Gi] + [0] * (Nt - i - 1)) * inc_amp
    
    flux_expr = compress_piecewise(G_trial, F.t, dt)

    model.boundary_conditions = [
        F.FluxBC(surfaces=1, value=flux_expr, field="solute"),
        F.RecombinationFlux(surfaces=1, Kr_0=params['ku'], E_Kr=0, order=2),
        F.RecombinationFlux(surfaces=2, Kr_0=params['kd'], E_Kr=0, order=2),
    ]
    
    model.initialise()
    model.run()

    computed_flux = abs(np.array(dq.filter(surfaces=2).data))
    exp_flux = np.array(experimental_flux)[:i + 1]
    computed_flux = computed_flux[:i + 1]

    return np.sum(((computed_flux - exp_flux) / exp_flux) ** 2)

def optimize_flux_without_output(*args, **kwargs):
    with capture_output():
        return optimize_flux(*args, **kwargs)