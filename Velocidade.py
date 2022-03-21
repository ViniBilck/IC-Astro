import numpy as np


def velocity_module(data):
	r_coord_mod = [np.sqrt(data[_][0]**2 + data[_][1]**2 + data[_][2]**2) for _ in range(len(data))]
	mass = [np.sum((r_coord_mod < r_coord_mod[_])) for _ in range(len(r_coord_mod))]
	g_const = 1
	v_mod = [np.sqrt((g_const*mass[_])/r_coord_mod[_]) for _ in range(len(r_coord_mod))]
	
	return v_mod

def velocity_vector(data, v_module):
    v_normais_plan = []
    for _ in range(len(data)):
        modulo = np.linalg.norm(data[_])
        t = np.rad2deg(np.arctan2(data[_][1], data[_][0]) + np.pi / 2)
        p = np.array([np.cos(t), np.sin(t), 0]) * modulo
        x = np.cross(data[_], p)
        x /= np.linalg.norm(x)
        v_un = np.cross(x, data[_])
        v_un /= np.linalg.norm(v_un)
        v_normais_plan.append(v_un)

    v_velo = [np.cross(v_normais_plan[_], data[_]/np.linalg.norm(data[_])) for _ in range(len(data))]
    ret = []
    for _ in range(len(v_velo)):
        ret.append([v_module[_]*v_velo[_][0], v_module[_]*v_velo[_][1], v_module[_]*v_velo[_][2]])
    return np.array(ret, dtype=np.float32)