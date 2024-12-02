class vehiculos():
	"""docstring for ClassName"""
	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo 
		self.enmarcha=False

	def arrancar(self):
		self.enmarcha=True
	def estado(self):
		print("Marca: ", self.marca, "Modelo: ", self.modelo, "En marcha :", self.enmarcha)
class motos(vehiculos):
	pass
moto_0=motos("Honda", "CRV")

moto_0.estado()
		