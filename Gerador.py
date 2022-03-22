import os
import numpy as np
import matplotlib.pyplot as plt 
import argparse
import configparser
import tables
import Velocidade as vd
import Coordenadas as cd

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-ho", help="Comprimento da escala exponencial do disco", type = float )
	parser.add_argument("-z", help="Espessura da escala vertical do disco", type = float )
	parser.add_argument("-m", help="Massa total do disco", type = float )
	parser.add_argument("-n", help="Número de particulas geradas", type = int )
	parser.add_argument("-G", "--Galaxia", help="Gerador de galaxia", action = "store_true")
	parser.add_argument("-CG", "--Config_Galaxia", help="Gerador de galaxia com arquivo config.ini", action = "store_true")
	parser.add_argument("-b", "--bulge", help="Gerador de bojo", action = "store_true")
	parser.add_argument("-s", "--save", help="Salva as coordenadas em HDF5", action = "store_true")
	parser.add_argument ("-c", "--config", help ="", dest='config_file', default='config.ini', type=str)
	
	args = parser.parse_args()
	here = os.path.realpath('.')
	config_file = args.config_file
	config = configparser.ConfigParser(defaults = {'here': here})
	config.read(args.config_file)
	
	if args.Galaxia:
		gal, p_z =  cd.galaxia(args.ho, args.z, args.m, args.n)
		print(gal)
		
		vet_x, vet_y, vet_z = gal[:,[0]].flatten(), gal[:,[1]].flatten(), gal[:,[2]].flatten()
		
		cd.plot_coord(vet_x, vet_y, vet_z)
		
		if args.save:
			data = tables.open_file("Data/Coord_Data.hdf5", mode = "w")
			atom = tables.Atom.from_dtype(gal.dtype)
			d = data.create_carray(data.root, "Coordinates", atom, gal.shape)
			d[:] = gal
			data.close()		

	if args.Config_Galaxia:
		ho = float(config.get("param", "ho"))
		z = float(config.get("param", "z"))
		m = float(config.get("param", "m"))
		n = int(config.get("param", "n"))

		gal, p_z =  cd.galaxia(ho, z, m, n)
		print(gal)
		
		vet_x, vet_y, vet_z = gal[:,[0]].flatten(), gal[:,[1]].flatten(), gal[:,[2]].flatten()
		
		cd.plot_coord(vet_x, vet_y, vet_z)

		if args.save:
			data = tables.open_file("Data/Coord_Data.hdf5", mode = "w")
			atom = tables.Atom.from_dtype(gal.dtype)
			d = data.create_carray(data.root, "Coordinates", atom, gal.shape)
			d[:] = gal
			data.close()
	
	if args.bulge:
		a = float(config.get("bulge", "a"))
		m = float(config.get("bulge", "m"))
		n = int(config.get("bulge", "n"))

		bulge = cd.bulge_coord(m, a, n)
		vet_x, vet_y, vet_z = bulge[:,[0]].flatten(), bulge[:,[1]].flatten(), bulge[:,[2]].flatten()
		
		cd.plot_coord(vet_x, vet_y, vet_z)


if __name__ == "__main__":
	main()
	

