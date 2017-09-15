class insect (object):

	def estrutura (self , abdomem, antenas, pernas, tipos):
		self.abdomem = abdomem	
		self.antenas = antenas
		self.pernas = pernas
		self.tipos = ['filiforme', 'moniliforme','clavada', 'capitada', 'imbricada', 'fusiforme', 'serreada',
					 	'dentada', 'estiliforme', 'plumosa', 'flabeada', 'setacea', 'furcada', 'pectinada','lamelada',
					 	 'gelinulada', 'aristada','composta']
		self.aparelho_bucal = ['mastigador', 'dugador labial', 'sugador maxilar', 'lambedor', ]

	def valida(self):
		if self.abdomem == True and self.antenas == 2 and self.pernas ==3:
			print ('Esse animal é um inseto')
			ante = input('Digite o tipo de antena: ')
			if ante in self.tipos:
				print ('Esse é um tipo valido de antena')
			else:
				print ('Essa antena nao pertence a um padrão dos insetos')
			apar = input('Digite um aparelho bucal')
			if apar in self.aparelho_bucal:
				print ('Esse é um tipo de aparelho bucal valido')
			else:
				print ('Esse aparelho bucal nao é valido ')
		else:
			print('Esse animal não é um inseto')
		
	def diptera(self, aparelho_bucal,asas_posteriores):
		self.aparelho_bucal = 'sugador'
		print (self.aparelho_bucal)
		self.asas_posteriores = 'balancis'
		print (self.asas_posteriores)
			


print ('Digite as caracteristicas desse animal')
chos = input('Ele possui abdomem?: ')
if chos == 's':
	abd = True
else:
	abd = False
inseto = insect()
ant = int(input('Qual o numero de antenas?: '))
pern = int(input('Qual o numero de pernas?: '))
inseto.estrutura(abdomem =abd, antenas=ant, pernas=pern, tipos='' )
inseto.valida()


