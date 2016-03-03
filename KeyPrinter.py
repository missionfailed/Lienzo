from LienzoListener import LienzoListener

class KeyPrinter(LienzoListener):
	def exitProgram(self, ctx):
		print("Programa parseado con exito")
        