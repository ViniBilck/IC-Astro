import numpy as np

def radial_rand(h, z_0, m, n):
	'''
	Retorna um vetor de números aleatorios para raio da galaxia
	'''
	a_const = (-4*np.pi*h*z_0)/m
	num_r = -h*np.log(a_const * np.random.uniform(-1,0,n) + 1)
	ret =  num_r + min(num_r)*-1
	
	return ret

def high_rand(h, z_0, m, n):
	'''
	Retorna um vetor de números aleatorios para expessura da galaxia
	'''
	dominio = m/(4*np.pi*h**2)
	z = np.random.uniform(-dominio,dominio,n)
	a_const = (4*np.pi*h**2)/m
	## ret = z_0 * np.arctanh(a_const*z)
	t = z*a_const
	lo = np.log((1+t)/(1-t))

	retu = z_0 * (1/2) * lo

	return retu


def galaxia(h1, h2, z01, z02, m, n):
	
	z = high_rand(h1, z01, m, n)
	p = radial_rand(h2, z02, m, n)
	
	r = np.sqrt((z**2) + (p**2))
	th = 2*np.pi*np.random.random(n)
	x = r*np.sin(th)
	y = r*np.cos(th)

	data = []
	data_ana = []
	for _ in range(n):
		data.append([x[_], y[_], z[_]])
		data_ana.append([z[_], p[_]])
	return np.array(data, dtype=np.float32), np.array(data_ana, dtype=np.float32)

