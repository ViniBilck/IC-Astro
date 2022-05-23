import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

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
    a_const = (-4 * np.pi * h * z_0) / m
    num_r = -h * np.log(a_const * np.random.uniform(-1, 0, n) + 1)
    ret = num_r + min(num_r) * -1

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
    dominio = m / (4 * np.pi * h ** 2)
    z = np.random.uniform(-dominio, dominio, n)
    a_const = (4 * np.pi * h ** 2) / m
    t = z * a_const
    lo = np.log((1 + t) / (1 - t))

    retu = z_0 * (1 / 2) * lo

    return retu


def set_disk_position(h1: float, z01: float, m: float, n: int):
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

    th = 2 * np.pi * np.random.random(n)
    x = p * np.sin(th)
    y = p * np.cos(th)
    coord = np.column_stack((x, y, z))

    return coord


def bulge_vet(M, a, n):
    x_r = np.random.uniform(0, 1, n)
    r_rand = a * np.sqrt(x_r / M) / (1 - np.sqrt(x_r / M))
    return r_rand


def coord_esf(R, n):
    data = []
    for _ in range(n):
        theta = np.arccos(1 - 2 * np.random.random())
        phi = np.random.random() * 2 * np.pi
        raio = R * np.sqrt(np.random.random())

        data.append([raio * np.cos(phi) * np.sin(theta), raio * np.sin(phi) * np.sin(theta), raio * np.cos(theta)])
    data2 = np.array(data, dtype=np.float32)
    return data2


def bulge_coord(M, a, n):
    r_coord = bulge_vet(M, a, n)
    data = []
    for _ in range(len(r_coord)):
        x = coord_esf(r_coord[_], 1).tolist()[0]
        data.append(x)

    return np.array(data, dtype=np.float32)

def dehnen_cumulative(r, M, a, gamma):
  return M * (r/(r+float(a)))**(3-gamma)


# Inverse cumulative mass function. Mc is a number between 0 and M.
def dehnen_inverse_cumulative(Mc, M, a, gamma):
  results = []
  for i in Mc:
    results.append(optimize.brentq(lambda r: dehnen_cumulative(r, M, a, gamma) - i, 0, 1.0e10))
  return np.array(results)

def set_halo_positions(halo_cut_r, M_halo, a_halo, gamma_halo, N_halo):
  global halo_cut_M
  halo_cut_M = dehnen_cumulative(halo_cut_r, M_halo, a_halo, gamma_halo)
  radii = dehnen_inverse_cumulative(np.random.sample(N_halo) * halo_cut_M,
                                    M_halo, a_halo, gamma_halo)
  thetas = np.arccos(np.random.sample(N_halo)*2 - 1)
  phis = 2 * np.pi * np.random.sample(N_halo)
  xs = radii * np.sin(thetas) * np.cos(phis)
  ys = radii * np.sin(thetas) * np.sin(phis)
  zs = radii * np.cos(thetas)
  coords = np.column_stack((xs, ys, zs))
  return coords


def set_bulge_positions(bulge_cut_r, M_bulge, a_bulge, gamma_bulge, N_bulge):
  global bulge_cut_M
  bulge_cut_M = dehnen_cumulative(bulge_cut_r, M_bulge, a_bulge, gamma_bulge)
  radii = dehnen_inverse_cumulative(np.random.sample(N_bulge) * bulge_cut_M,
    M_bulge, a_bulge, gamma_bulge)
  thetas = np.arccos(np.random.sample(N_bulge) * 2 - 1)
  phis = 2 * np.pi * np.random.sample(N_bulge)
  xs = radii * np.sin(thetas) * np.cos(phis)
  ys = radii * np.sin(thetas) * np.sin(phis)
  zs = radii * np.cos(thetas)
  coords = np.column_stack((xs, ys, zs))
  return coords

def plot_coord(vet_x, vet_y, vet_z):
    """
    Grafica os planos XY e YZ. Vetores precisam ter o mesmo comprimento
    Parametros
    ----------
    vet_x : ndarray
    	Lista com os valores do eixo X
    vet_y : ndarray
    	Lista com os valores do eixo Y
    vet_z : ndarray
    	Lista com os valores do eixo Z
	Returns
    -------
    return : PyPlot
        Plot de XY e YZ
    """
    f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
    ax1.plot(vet_x[0], vet_y[0], 'o', markersize=1, label="Disk")
    ax1.plot(vet_x[2], vet_y[2], 'o', markersize=1, label="Halo", alpha=0.8)
    ax1.plot(vet_x[1], vet_y[1], 'o', markersize=1, label="Bulge")
    ax1.set_title("XY View")
    ax1.set_xlabel("kpc/h")
    ax1.set_ylabel("kpc/h")
    ax1.set_xlim(-50, 50)
    ax1.set_ylim(-50, 50)
    ax1.grid()
    ax2.plot(vet_y[0], vet_z[0], 'o', markersize=1, label="Disk")
    ax2.plot(vet_y[2], vet_z[2], 'o', markersize=1, label="Halo", alpha=0.8)
    ax2.plot(vet_y[1], vet_z[1], 'o', markersize=1, label="Bulge")
    ax2.set_title("YZ View")
    ax2.set_xlabel("kpc/h")
    ax2.set_ylabel("kpc/h")
    ax2.set_xlim(-50, 50)
    ax2.set_ylim(-50, 50)
    ax2.grid()
    plt.legend()
    plt.show()
