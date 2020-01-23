import h5py
import numpy
import matplotlib.pyplot as plt

def plotflux(h5file, state=1):
    """
    A function that plots the dataset target_flux_evolution from a direct.h5 file.

    Parameters
    ----------
    h5file: dictionary
        The user's HDF5 file loaded with loadh5.
    state: integer
        The target state; the state for which you want to know the entering flux for.

    Returns
    -------
    Nothing
        The plot of the flux evolution will be shown in a separate window.

    Examples
    --------
    >>> h5file = loadh5("direct.h5")
    >>> plotflux(h5file, 1)
    --------
    |  __/ |
    | /    |
    --------  
    """
    fluxes = h5file['target_flux_evolution']['expected',:,state-1]
    iterations = numpy.arange(1,len(fluxes)+1,1)
    fig, ax = plt.subplots()
    ax.plot(iterations,fluxes, linewidth=3)
    ax.set_xlabel('WE Iteration', fontsize=24)
    ax.set_ylabel('Mean Flux', fontsize=24)
    ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    ax.tick_params(labelsize=22)
    fig.tight_layout()
    plt.show()
