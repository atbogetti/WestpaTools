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

def plotrc(assignfile, directfile, fi, li, istate, fstate, tauinps, concentrationinM=1):
    """
    A function that plots the rate constant evolution from a direct.h5 file.

    Parameters
    ----------
    assignfile: string
        Path to the user's w_ipa-generated assign.h5 file loaded with loadh5.
    directfile: string
        Path to the user's w_ipa-generated direct.h5 file loaded with loadh5.
    fi: integer
        Iteration to start evaluation of the rate constant.
    li: integer
        Iteration to end evaluation of the rate constant.
    istate: integer
        State from which trajectories are initialized.
    fstate: integer
        State from which trajectories are terminated.
    tauinps: integer
        Value of tau in picoseconds.
    concentration: float
        Value of the concentration in Molar; only required if the process is bimolecular.

    Returns
    -------
    Nothing
        The plot of the rate constant evolution will be shown in a separate window.

    Examples
    --------
    >>> assignfile = loadh5("assign.h5")
    >>> directfile = loadh5("direct.h5")
    >>> plotrc(assignfile, directfile, 1, 1000, 0, 1, 0.5, 0.03)
    --------
    |  __/ |
    | /    |
    --------  
    """
    cflist = []
    cf = directfile['conditional_fluxes']
    iter_start = directfile.attrs['iter_start']
    iter_stop = directfile.attrs['iter_stop']
    fidx = fi-iter_start
    lidx = fidx + (li-fi)
    cflist.append(cf[fidx:lidx,istate, fstate])
    flux_arr = numpy.vstack(cflist)

    poplist = []
    pops = assignfile['labeled_populations'][fi-1:li-1, istate].sum(axis=1)
    poplist.append(pops)
    pop_arr =  numpy.vstack(poplist)

    pop_list = []
    for simpop in pop_arr:
        N_arr = numpy.arange(1, simpop.shape[0]+1)
        cumsum = numpy.cumsum(simpop, axis=0)
        for i in xrange(cumsum.shape[0]):
            cumsum[i] = cumsum[i]/N_arr[i]
        pop_list.append(cumsum)
    pop_arr = numpy.array(pop_list)
                                                                       
    flux_list = [] 
    for simflux in flux_arr:
        N_arr = numpy.arange(1, simflux.shape[0]+1)
        cumsum = numpy.cumsum(simflux, axis=0)
        for i in xrange(cumsum.shape[0]):
            cumsum[i] = cumsum[i]/N_arr[i]
        flux_list.append(cumsum)
    flux_arr = numpy.array(flux_list)

    rates = flux_arr/pop_arr 

    rate_mean = rates.mean(axis=0)     
    rate_se = rates.std(axis=0, ddof=1)/numpy.sqrt(rates.shape[0])
    tauinps = tauinps*1E-12
    rate_mean = rate_mean/(tauinps*concentrationinM)
    rate_se = rate_se/(tauinps*concentrationinM)

    iterations = numpy.arange(1,len(rate_mean)+1,1)
    fig, ax = plt.subplots()
    ax.semilogy(iterations,rate_mean, linewidth=3)
    ax.set_xlabel('WE Iteration', fontsize=24)
    ax.set_ylabel('Rate Constant', fontsize=24)
    ax.tick_params(labelsize=22)
    fig.tight_layout()
    plt.show()
