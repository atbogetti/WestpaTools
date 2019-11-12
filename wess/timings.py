import h5py
import numpy

def walltime(h5file):
    """
    This function calculates the wallclock time of a WESTPA simulation.
    
    Parameters
    ----------
    h5file: dictionary
        The user's HDF5 file loaded with open_h5.
    
    Returns
    -------
    Nothing
        The wallclock time will be printed to the terminal in seconds.
    
    Examples
    --------
    >>> h5file = open_h5("west.h5")
    >>> walltime(h5file)
    2000000 seconds
    """
    wallclocktime = h5file['summary']['walltime']
    print(numpy.sum(wallclocktime),"seconds")

def aggtime(h5file, tau):
    """
    This function calculates the aggregate time of a WESTPA simulation.
    
    Parameters
    ----------
    h5file: dictionary
        The user's HDF5 file loaded with open_h5.
    tau: float
        The WESTPA simulation's tau value in picoseconds.
    
    Returns
    -------
    Nothing
        The aggregate time will be printed to the terminal in picoseconds.
    
    Examples
    --------
    >>> h5file = open_h5("west.h5")
    >>> aggtime(h5file)
    2000 picoseconds
    """
    aggregatetime = h5file['summary']['n_particles']
    print(numpy.sum(aggregatetime)*tau,"picoseconds")
