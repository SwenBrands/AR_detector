def get_wind_sector(direction,indlat,indlon):

    if (direction > 22.5) & (direction <= 67.5): #to the NE
       indlat_1 = indlat+1; indlat_2 = indlat+1; indlat_3 = indlat
       indlon_1 = indlon; indlon_2 = indlon+1; indlon_3 = indlon+1
    elif (direction > 67.5) & (direction <= 112.5): #to the E
       indlat_1 = indlat+1; indlat_2 = indlat; indlat_3 = indlat-1
       indlon_1 = indlon+1; indlon_2 = indlon+1; indlon_3 = indlon+1
    elif (direction > 112.5) & (direction <= 157.5): #to the SE            
       indlat_1 = indlat; indlat_2 = indlat-1; indlat_3 = indlat-1
       indlon_1 = indlon+1; indlon_2 = indlon+1; indlon_3 = indlon
    elif (direction > 157.5) & (direction <= 202.5): #to the S            
       indlat_1 = indlat-1; indlat_2 = indlat-1; indlat_3 = indlat-1
       indlon_1 = indlon+1; indlon_2 = indlon; indlon_3 = indlon-1
    elif (direction > 202.5) & (direction <= 247.5): #to the SW            
       indlat_1 = indlat-1; indlat_2 = indlat-1; indlat_3 = indlat
       indlon_1 = indlon; indlon_2 = indlon-1; indlon_3 = indlon-1
    elif (direction > 247.5) & (direction <= 292.5): #to the W            
       indlat_1 = indlat-1; indlat_2 = indlat; indlat_3 = indlat+1
       indlon_1 = indlon-1; indlon_2 = indlon-1; indlon_3 = indlon-1
    elif (direction > 292.5) & (direction <= 337.5): #to the NW
       indlat_1 = indlat; indlat_2 = indlat+1; indlat_3 = indlat+1
       indlon_1 = indlon-1; indlon_2 = indlon-1; indlon_3 = indlon
    elif (direction > 337.5) | (direction <= 22.5): #to the N
       indlat_1 = indlat+1; indlat_2 = indlat+1; indlat_3 = indlat+1
       indlon_1 = indlon-1; indlon_2 = indlon; indlon_3 = indlon+1
    else:
       raise Exception('entry for <dircection> is not valid')
       
    ind_nn_lon = [indlon_1[0],indlon_2[0],indlon_3[0]]
    ind_nn_lat = [indlat_1[0],indlat_2[0],indlat_3[0]]

    return(ind_nn_lon,ind_nn_lat)
        
