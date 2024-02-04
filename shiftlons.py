def shiftlons(lon_in, data_in):

    """
    lon is one-dimensional, data_in has 3 dims., converts to -180 to 180
    """
    map = Basemap(projection='sinu',lat_0=0, lon_0=0)
    data_shifted = np.zeros(data_in.shape)
    if len(data_in.shape) == 3:
        for ii in range(data_in.shape[0]):
            lon_shifted, data_shifted[ii,:,:] = map.shiftdata(lon_in, datain = data_in[ii,:,:], lon_0=None)
    elif len(data_in.shape) == 2:
            lon_shifted, data_shifted = map.shiftdata(lon_in, datain = data_in, lon_0=None)
    else:
        raise Exception('check number of dimensions in <data_in> !!')
    del map
    return(lon_shifted,data_shifted)
