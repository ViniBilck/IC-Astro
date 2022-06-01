import numpy as np

def velocity_module(data):
    r_coord_mod = [np.linalg.norm(data[_]) for _ in range(len(data))]
    mass = [np.sum((r_coord_mod < r_coord_mod[_])) for _ in range(len(r_coord_mod))]
    g_const = 1
    v_mod = [np.sqrt((g_const*mass[_])/r_coord_mod[_]) for _ in range(len(r_coord_mod))]
    return v_mod

def velocity_vector(data, v_module):
    ret = []
    ## import pdb; pdb.set_trace()
    for _ in range(len(data)):
        modulo = np.linalg.norm(data[_])
        t = np.arctan2(data[_][1], data[_][0]) + np.pi / 2
        p = np.array([np.cos(t), np.sin(t), 0]) * modulo
        x = np.cross(data[_], p)
        v_un = np.cross(data[_], x)
        v_un /= np.linalg.norm(v_un)
        ret.append([v_module[_]*v_un[0],v_module[_]*v_un[1],v_module[_]*v_un[2]])
    
    return np.array(ret, dtype=np.float32)
    

