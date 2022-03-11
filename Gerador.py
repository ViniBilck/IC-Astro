import numpy as np
import matplotlib.pyplot as plt 
import argparse
import configparser

plt.style.use('seaborn-bright')
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
	'''
	Retorna um vetor de números aleatorios para raio da galaxia
	'''
	a_const = (-4*np.pi*h*z_0)/m
	num_r = -h*np.log(a_const * np.random.uniform(-1,0,n) + 1)
	ret =  num_r + min(num_r)*-1
	
	return ret

def high_rand(h: float, z_0: float, m: float, n: int):
	'''
	Retorna um vetor de números aleatorios para expessura da galaxia
	'''
	dominio = m/(4*np.pi*h**2)
	z = np.random.uniform(-dominio,dominio,n)
	a_const = (4*np.pi*h**2)/m
	t = z*a_const
	lo = np.log((1 + t)/(1 - t))

	retu = z_0*(1/2)*lo

	return retu


def galaxia(h1: float, h2: float, z01: float, z02: float, m: float, n: int):
	
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

def plot_coord(vet_x: list, vet_y: list, vet_z: list):
	f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
		
	## 1
	ax1.plot(vet_x, vet_y, 'o', markersize = 1, c = '#f72585')
	ax1.set_title("XY View")
	ax1.set_xlabel("kpc/h")
	ax1.set_ylabel("kpc/h")
	ax1.set_xlim(-50, 50)
	ax1.set_ylim(-50, 50)
	ax1.grid()

	## 2
	ax2.plot(vet_y, vet_z, 'o', markersize = 1, c = '#3a0ca3')
	ax2.set_title("YZ View")
	ax2.set_xlabel("kpc/h")
	ax2.set_ylabel("kpc/h")
	ax2.set_xlim(-50, 50)
	ax2.set_ylim(-50, 50)
	ax2.grid()
	plt.show()


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-h_D", help="comprimento da escala exponencial do disco", type = float )
	parser.add_argument("-z_D", help="espessura da escala vertical do disco", type = float )
	parser.add_argument("-m_D", help="Massa total do disco", type = float )
	parser.add_argument("-n_D", help="Número de particulas geradas", type = int )
	parser.add_argument("-G", "--Galaxia", help="Gerador de galaxia", action = "store_true")
	args = parser.parse_args()
	if args.Galaxia:
		gal, p_z =  galaxia(args.h_D, args.h_D, args.z_D, args.z_D, args.m_D, args.n_D)
		print(gal)
		
		vet_x, vet_y, vet_z = gal[:,[0]].flatten(), gal[:,[1]].flatten(), gal[:,[2]].flatten()
		
		plot_coord(vet_x, vet_y, vet_z)


if __name__ == "__main__":
	main()

