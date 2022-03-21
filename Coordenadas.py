import numpy as np
import matplotlib.pyplot as plt 



plt.style.use('seaborn-bright')
plt.style.use('dark_background')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['legend.fontsize'] = 14
plt.rcParams['figure.figsize'] = (16, 8)
plt.rcParams['lines.linewidth'] = 2
plt.rcParams["savefig.dpi"] = 400



def radial_rand(h: float, z_0: float, m: float, n: int):
	"""
    Gera um valor aleatorio para a parte radial da galaxia, seguindo o perfil de densidade do disco.
    Parametros
    ----------
    h : float
        Comprimento da escala exponencial do disco
    z_0 : float
        Espessura da escala vertical do disco
	m : float
        Massa total do disco
    n : int
        Número de particulas geradas
	Returns
    -------
    ret : Array
        Lista de números aleatorios que correspondem a trecho radial da galaxia.
    """
	a_const = (-4*np.pi*h*z_0)/m
	num_r = -h*np.log(a_const * np.random.uniform(-1,0,n) + 1)
	ret =  num_r + min(num_r)*-1
	
	return ret

def high_rand(h: float, z_0: float, m: float, n: int):
	"""
    Gera um valor aleatorio para a expessura da galaxia, seguindo o perfil de densidade do disco.
    Parametros
    ----------
    h : float
        Comprimento da escala exponencial do disco
    z_0 : float
        Espessura da escala vertical do disco
	m : float
        Massa total do disco
    n : int
        Número de particulas geradas
	Returns
    -------
    retu : Array
        Lista de números aleatorios que correspondem a expessura vertical da galaxia.
    """
	dominio = m/(4*np.pi*h**2)
	z = np.random.uniform(-dominio,dominio,n)
	a_const = (4*np.pi*h**2)/m
	t = z*a_const
	lo = np.log((1 + t)/(1 - t))

	retu = z_0*(1/2)*lo

	return retu


def galaxia(h1: float, z01: float, m: float, n: int):
	"""
    Gera coordenadas X, Y, Z aleatorias, seguindo o perfil de densidade do disco.
    Parametros
    ----------
    h1 : float
        Comprimento da escala exponencial do disco
    z01 : float
        Espessura da escala vertical do disco
	m : float
        Massa total do disco
    n : int
        Número de particulas geradas
	Returns
    -------
    return : np.array, np.array
        Duas matrizes que correspondem, coordenadas X, Y, Z da galaxia, 
		e os valores de Rho e Z, do perfil de densidade do disco.
    """	
	z = high_rand(h1, z01, m, n)
	p = radial_rand(h1, z01, m, n)

	th = 2*np.pi*np.random.random(n)
	x = p*np.sin(th)
	y = p*np.cos(th)

	data = []
	data_ana = []
	for _ in range(n):
		data.append([x[_], y[_], z[_]])
		data_ana.append([z[_], p[_]])
	return np.array(data, dtype=np.float32), np.array(data_ana, dtype=np.float32)



def bulge_vet(M, a, n):
	x_r = np.random.uniform(0,1,n)
	r_rand = a*np.sqrt(x_r/M)/(1 - np.sqrt(x_r/M))
	return r_rand



def bulge_coord():
	
	return


def plot_coord(vet_x: list, vet_y: list, vet_z: list):
	"""
    Grafica os planos XY e YZ. Vetores precisam ter o mesmo comprimento
    Parametros
    ----------
    vet_x : list
    	Lista com os valores do eixo X
    vet_y : list
    	Lista com os valores do eixo Y
    vet_z : list
    	Lista com os valores do eixo Z
	Returns
    -------
    return : PyPlot
        Plot de XY e YZ
    """
	f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
	ax1.plot(vet_x, vet_y, 'o', markersize = 1)
	ax1.set_title("XY View")
	ax1.set_xlabel("kpc/h")
	ax1.set_ylabel("kpc/h")
	ax1.set_xlim(-50, 50)
	ax1.set_ylim(-50, 50)
	ax1.grid()
	ax2.plot(vet_y, vet_z, 'o', markersize = 1)
	ax2.set_title("YZ View")
	ax2.set_xlabel("kpc/h")
	ax2.set_ylabel("kpc/h")
	ax2.set_xlim(-50, 50)
	ax2.set_ylim(-50, 50)
	ax2.grid()
	plt.show()

	