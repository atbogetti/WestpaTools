import h5py
import numpy

def loadh5(file_location = "./west.h5"):
    """
    A function that opens an h5 file.
    
    Parameters
    ----------
    file_location: a string
    The path to the user's h5 file. Default: west.h5 in the current directory.
    
    Returns
    -------
    h5_file: dictionary
    The user's specified h5 file.
    
    Examples
    --------
    >>> file_location = "../myh5file.h5"
    >>> h5 = loadh5(file_location)
    >>> h5
    <HDF5 file "myh5file.h5" (mode r)>
    """
    h5_file = h5py.File(file_location, 'r')
    return h5_file
