def velocity_vector(data):
	r_coord = [np.sqrt(data[_][0]**2 + data[_][1]**2 + data[_][2]**2) for _ in range(len(data))]
	mass = [np.sum((r_coord < r_coord[_])) for _ in range(len(r_coord))]
	g_const = 1
	v_mod = [np.sqrt((g_const*mass[_])/r_coord[_]) for _ in range(len(r_coord))]
	
	return