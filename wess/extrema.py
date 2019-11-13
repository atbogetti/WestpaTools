import numpy
import h5py

def findmax(h5file, pcoord_dim, fi, li):
    """
    A function that locates the segment with the maximum pcoord value.

    Parameters
    ----------
    h5file: dictionary
        The user's HDF5 file loaded with loadh5.
    pcoord_dim: integer
        The progress coordinate dimension you want to know the max for.
    fi: integer
        The starting iteration for consideration.
    li: integer
        The ending iteration for consideration.

    Returns
    -------
    Nothing
        The maximum value and its corresponding iter and seg numbers are printed to the terminal.

    Examples
    --------
    >>> h5file = loadh5("west.h5")
    >>> findmax(h5file, 1, 1, 10)
    Maximum pcoord value for dimension 1 is: 22.9468
    It is segment: 78 of iteration: 10          
    """
    max_values = []
    for i in range(fi,li+1):
      i = str(i)
      iteration = "iter_" + str(numpy.char.zfill(i,8))
      pc = h5file['iterations'][iteration]['pcoord']
      maxv = numpy.max(pc[:,-1,pcoord_dim-1])
      max_values.append(maxv)
    maxmax = numpy.max(max_values)
    nw = numpy.where(max_values>(maxmax-maxmax*0.0001))
    iter_num = str((nw[0]+1)[0])
    
    wheretolook = "iter_" + str(numpy.char.zfill(iter_num,8))
    max_iter = h5file['iterations'][wheretolook]['pcoord'][:,-1,pcoord_dim-1]
    segmax = numpy.max(max_iter)
    nw2 = numpy.where(max_iter>(segmax-segmax*0.0001))
    seg_num = (nw2[0]+1)[0]
    print ("Maximum pcoord value for dimension",pcoord_dim,"is:",segmax) 
    print ("It is segment:",seg_num,"of iteration:",iter_num)

def findmin(h5file, pcoord_dim, fi, li):
    """
    A function that locates the segment with the minimum pcoord value.

    Parameters
    ----------
    h5file: dictionary
        The user's HDF5 file loaded with loadh5.
    pcoord_dim: integer
        The progress coordinate dimension you want to know the min for.
    fi: integer
        The starting iteration for consideration.
    li: integer
        The ending iteration for consideration.

    Returns
    -------
    Nothing
        The minimum value and its corresponding iter and seg numbers are printed to the terminal.

    Examples
    --------
    >>> h5file = loadh5("west.h5")
    >>> findmin(h5file, 1, 1, 10)
    Minimum pcoord value for dimension 1 is: 2.4968
    It is segment: 1 of iteration: 9          
    """
    min_values = []
    for i in range(fi,li+1):
      i = str(i)
      iteration = "iter_" + str(numpy.char.zfill(i,8))
      pc = h5file['iterations'][iteration]['pcoord']
      minv = numpy.min(pc[:,-1,pcoord_dim-1])
      min_values.append(minv)
    minmin = numpy.min(min_values)
    print(min_values)
    print(minmin)
    nw = numpy.where(min_values<(minmin+minmin*0.0001))
    print(nw)
    iter_num = str((nw[0]+1)[0])
    
    wheretolook = "iter_" + str(numpy.char.zfill(iter_num,8))
    min_iter = h5file['iterations'][wheretolook]['pcoord'][:,-1,pcoord_dim-1]
    segmin = numpy.min(min_iter)
    nw2 = numpy.where(min_iter<(segmin+segmin*0.0001))
    seg_num = (nw2[0]+1)[0]
    print ("Minimum pcoord value for dimension",pcoord_dim,"is:",segmin) 
    print ("It is segment:",seg_num,"of iteration:",iter_num)
