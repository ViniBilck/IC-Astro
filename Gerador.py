import os
import argparse
import configparser
import tables
import numpy as np
import Coordenadas as Cd


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("-G", "--Galaxia", help="Gerador de galaxia", action="store_true")
	parser.add_argument("-CG", "--Config_Galaxia", help="Gerador de galaxia com arquivo config.ini", action="store_true")
	parser.add_argument("-b", "--bulge", help="Gerador de bojo", action="store_true")
	parser.add_argument("-s", "--save", help="Salva as coordenadas em HDF5", action="store_true")
	parser.add_argument("-c", "--config", help="", dest='config_file', default='config.ini', type=str)

	args = parser.parse_args()
	here = os.path.realpath('.')
	config = configparser.ConfigParser(defaults={'here': here})
	config.read(args.config_file)

	if args.Config_Galaxia:
		## Disk Data
		ho = float(config.get("disk", "Ho_disk"))
		z = float(config.get("disk", "Z_disk"))
		m = float(config.get("disk", "M_disk"))
		n = int(config.get("disk", "N_disk"))

		## Halo Data
		cut_halo = float(config.get("halo", "r_cut_halo"))
		M_halo = float(config.get("halo", "M_halo"))
		N_halo = int(config.get("halo", "N_halo"))
		A_halo = float(config.get("halo", "A_halo"))
		gamma_halo = float(config.get("halo", "gamma_halo"))

		## Bulge Data
		cut_bulge = float(config.get("bulge", "r_cut_bulge"))
		M_bulge = float(config.get("bulge", "M_bulge"))
		N_bulge = int(config.get("bulge", "N_bulge"))
		A_bulge = float(config.get("bulge", "A_bulge"))
		gamma_bulge = float(config.get("bulge", "gamma_bulge"))

		disk = Cd.set_disk_position(ho, z, m, n)
		halo = Cd.set_halo_positions(cut_halo, M_halo, A_halo, gamma_halo, N_halo)
		bulge = Cd.set_bulge_positions(cut_bulge, M_bulge, A_bulge, gamma_bulge, N_bulge)
		print(disk)
		print(f"Halo: {halo}")
		print(f"Bulge: {bulge}")
		
		vet_x_disk, vet_y_disk, vet_z_disk = disk[:, [0]].flatten(), disk[:, [1]].flatten(), disk[:, [2]].flatten()
		vet_x_bulge, vet_y_bulge, vet_z_bulge = bulge[:, [0]].flatten(), bulge[:, [1]].flatten(), bulge[:, [2]].flatten()
		vet_x_halo, vet_y_halo, vet_z_halo = halo[:, [0]].flatten(), halo[:, [1]].flatten(), halo[:, [2]].flatten()

		vet_x = np.array([vet_x_disk, vet_x_bulge, vet_x_halo])
		vet_y = np.array([vet_y_disk, vet_y_bulge, vet_y_halo])
		vet_z = np.array([vet_z_disk, vet_z_bulge, vet_z_halo])

		Cd.plot_coord(vet_x, vet_y, vet_z)

		if args.save:
			data = tables.open_file("Data/Coord_Data.hdf5", mode="w")
			atom = tables.Atom.from_dtype(disk.dtype)
			d = data.create_carray(data.root, "Coordinates", atom, disk.shape)
			d[:] = disk
			data.close()
	
	if args.bulge:
		a = float(config.get("bulge", "a"))
		m = float(config.get("bulge", "m"))
		n = int(config.get("bulge", "n"))

		bulge = Cd.bulge_coord(m, a, n)
		vet_x, vet_y, vet_z = bulge[:, [0]].flatten(), bulge[:, [1]].flatten(), bulge[:, [2]].flatten()
		
		Cd.plot_coord(vet_x, vet_y, vet_z)


if __name__ == "__main__":
	main()
