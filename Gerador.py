import os
import argparse
import configparser
from tables import *
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

	## Disk Data
	Ho_disk = float(config.get("disk", "Ho_disk"))
	Z_disk = float(config.get("disk", "Z_disk"))
	M_disk = float(config.get("disk", "M_disk"))
	N_disk = int(config.get("disk", "N_disk"))

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

	disk = Cd.set_disk_position(Ho_disk, Z_disk, M_disk, N_disk)
	halo = Cd.set_halo_positions(cut_halo, M_halo, A_halo, gamma_halo, N_halo)
	bulge = Cd.set_bulge_positions(cut_bulge, M_bulge, A_bulge, gamma_bulge, N_bulge)
	print(disk)
	print(f"Halo: {halo}")
	print(f"Bulge: {bulge}")
		
	vet_x_disk, vet_y_disk, vet_z_disk = disk[:, [0]].flatten(), disk[:, [1]].flatten(), disk[:, [2]].flatten()
	vet_x_bulge, vet_y_bulge, vet_z_bulge = bulge[:, [0]].flatten(), bulge[:, [1]].flatten(), bulge[:, [2]].flatten()
	vet_x_halo, vet_y_halo, vet_z_halo = halo[:, [0]].flatten(), halo[:, [1]].flatten(), halo[:, [2]].flatten()

	vet_x = np.array([vet_x_disk, vet_x_bulge, vet_x_halo], dtype=np.ndarray)
	vet_y = np.array([vet_y_disk, vet_y_bulge, vet_y_halo], dtype=np.ndarray)
	vet_z = np.array([vet_z_disk, vet_z_bulge, vet_z_halo], dtype=np.ndarray)

	Cd.plot_coord(vet_x, vet_y, vet_z)

	if args.save:
		with open_file("Data/Coord_Data.hdf5", mode="w") as data:
			data.create_group('/', 'Header')
			data.root.Header._v_attrs.__delitem__("VERSION")
			data.root.Header._v_attrs.__delitem__("TITLE")
			data.root.Header._v_attrs.__delitem__("CLASS")
			for _ in range(4):
				data.create_group('/', f'PartType{_}')
			mass_per_part_disk = M_disk / N_disk
			mass_per_part_bulge = M_bulge / N_bulge
			mass_per_part_halo = M_halo / N_halo
			massTable_Disk = np.full((1,N_disk), mass_per_part_disk, float)
			massTable_Halo = np.full((1, N_halo), mass_per_part_halo, float)
			massTable_Bulge = np.full((1, N_bulge), mass_per_part_bulge, float)

			##To_Halo
			data.create_array(data.root.PartType1, "Coordinates", halo)
			data.create_array(data.root.PartType1, "Masses", massTable_Halo)

			##To_Disk
			data.create_array(data.root.PartType2, "Coordinates", disk)
			data.create_array(data.root.PartType2, "Masses", massTable_Disk)

			##To_Bulge
			data.create_array(data.root.PartType3, "Coordinates", bulge)
			data.create_array(data.root.PartType3, "Masses", massTable_Bulge)


			data.root.Header._v_attrs.MassTable = np.array([0., 0., 0., 0.])
			data.root.Header._v_attrs.NumPart_ThisFile = np.array([0, N_halo, N_disk, N_bulge], dtype=np.uint32)
			data.root.Header._v_attrs.NumPart_Total = np.array([0, N_halo, N_disk, N_bulge], dtype=np.uint64)

if __name__ == "__main__":
	main()
