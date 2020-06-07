print('Calculadora de Operações\n')

while True:
	#op = int(input('Qual operação gostaria de fazer?\n 1. Cálculo da distância entre dois pontos. \n 2. Ponto Médio. \n 3. Teorema de Pitágoras.\n 4. Perímetro da Circunferência. \n 5. Área da Circunferência.\n 6. Perímetro de um quadrilátero.\n 7. Área de um quadrilátero. \n 8. Coeficiente angular da reta. \n 9. Sair da Calculadora\n '))
	
	try:
			op = int(input('Qual operação gostaria de fazer?\n 1. Cálculo da distância entre dois pontos. \n 2. Ponto Médio. \n 3. Teorema de Pitágoras.\n 4. Perímetro da Circunferência. \n 5. Área da Circunferência.\n 6. Perímetro de um quadrilátero.\n 7. Área de um quadrilátero. \n 8. Coeficiente angular da reta. \n 9. Sair da Calculadora\n '))
			
			if op == 9:
				break
			if op == 1:
				import math
				print('\n Cálculo da distância entre dois pontos.\n')
				p1 = str(input('Quais as coordenadas do primeiro ponto? Separe-as por vírgula. \n'))
				p2 = str(input('Quais as coordenadas do segundo ponto? Separe-as por vírgula. \n'))
				p1 = p1.split(',')
				p2 = p2.split(',')
				print('\nx1 =',p1[0],'y1 =',p1[1],'\n','\nx2 =',p2[0],'y2 =',p2[1],'\n')
				t1 = float(p2[0]) - float(p1[0])
				t2 = float(p2[1]) - float(p1[1])
				q1 = t1**2
				q2 = t2**2
				s = q1 + q2
				d = math.sqrt(s)
				print('A distância entre os dois pontos é dada por: d = %.2f'%d,'\n')

			elif op == 2:
				import math
				print('\n Ponto médio.\n')
				p1 = str(input('Quais as coordenadas do primeiro ponto? Separe-as por vírgula. \n'))
				p2 = str(input('Quais as coordenadas do segundo ponto? Separe-as por vírgula. \n'))
				p1 = p1.split(',')
				p2 = p2.split(',')
				print('\nx1 =',p1[0],'y1 =',p1[1],'\n','\nx2 =',p2[0],'y2 =',p2[1],'\n')
				t1 = float(p2[0]) + float(p1[0])
				t2 = float(p2[1]) + float(p1[1])
				m1 = t1/2
				m2 = t2/2
				print('As coordenadas do ponto médio da reta dada são: (','%.2f'%m1,',','%.2f'%m2,')\n')

			elif op == 3:
				import math
				print('\n Teorema de Pitágoras. \n')
				inc = int(input('\nQual a incógnita que deseja descobrir? \n 1. Hipotenusa. \n 2. Cateto.\n'))
				if inc == 1:
					c1 = float(input('\nQual o valor do primeiro cateto?\n'))
					c2 = float(input('\nQual o valor do segundo cateto?\n'))
					h = (c1**2) + (c2**2)
					h1 = math.sqrt(h)
					print('A hipotenusa é: %.2f'%h1)
				elif inc == 2:
					c1 = float(input('\nQual o valor do cateto dado?\n'))
					c2 = float(input('\nQual o valor da hipotenusa?\n'))
					c = (c2**2) - (c1**2)
					h = math.sqrt(c)
					print('\nO valor do cateto-incógnita é:%.2f'%h,'\n')

			elif op == 4:
				import math
				print('\n Perímetro da Circunferência.\n')
				r = float(input('\nQual o raio da circunferência?\n'))
				p = 2 * math.pi *r
				print('\n O perímetro da circunferência é de: %.2f'% p,'\n')

			elif op == 5:
				import math
				print('\nÁrea da Circunferência.\n')
				r = float(input('\nQual o raio da circunferência?\n'))
				p = math.pi * (r**2)
				print('\n A área da circunferência é de: %.2f'% p,'\n')

			elif op == 6:
				print('\nPerímetro de um quadrilátero.\n')
				lado = str(input('\nQuais as medidas de cada lado da sua figura? Separe-as por vírgula\n'))
				lado = lado.split(',')
				l1 = float(lado[0])
				l2 = float(lado[1])
				l3 = float(lado[2])
				l4 = float(lado[3])
				if l1 < 0:
					l1 = l1*-1
				elif l2 < 0:
					l2 = l2 *-1
				elif l3 < 0:
					l3 = l3 * -1
				elif l4 < 0:
					l4 = l4 * -1
				per = l1+l2+l3+l4
				print('\n O perímetro de seu quadrilátero é de: ', per,'\n')

			elif op == 7:
				print('\nÁrea de um quadrilátero.\n')
				tipo = int(input('\n Qual quadrilátero deseja calcular o perímetro?\n 1. Quadrado.\n 2. Retângulo. \n 3. Losango. \n 4. Paralelogramo. \n 5. Trapézio. \n 6. Quadrilátero qualquer. \n'))
				if tipo == 1:
					print('\n Área do Quadrado\n')
					lado = str(input('\nQual a base e altura do seu quadrado? Separe-as por vírgula\n'))
					lado = lado.split(',')
					l1 = float(lado[0])
					l2 = float(lado[1])
					area = l1*l2
					print('\n A área do eu quadrado é de: %.2f'%area,'\n')
				elif tipo == 2:
					print('\n Área do Retângulo\n')
					lado = str(input('\nQual a base e altura do seu retângulo? Separe-as por vírgula\n'))
					lado = lado.split(',')
					l1 = float(lado[0])
					l2 = float(lado[1])
					area = l1*l2
					print('\n A área do seu retângulo é de: %.2f'%area,'\n')
				elif tipo == 3:
					print('\n Área do Losango\n')
					lado = str(input('\nQuais as diagonais do seu losango? Separe-as por vírgula\n'))
					lado = lado.split(',')
					l1 = float(lado[0])
					l2 = float(lado[1])
					area = (l1*l2)/2
					print('\n A área do seu losango é de: %.2f'%area,'\n')
				elif tipo == 4:
					print('\n Área do Paralelogramo\n')
					lado = str(input('\nQual a base e altura do seu losango? Separe-as por vírgula\n'))
					lado = lado.split(',')
					l1 = float(lado[0])
					l2 = float(lado[1])
					area = l1*l2
					print('\n A área do seu paralelogramo é de: %.2f'%area,'\n')
				elif tipo == 5:
					print('\n Área do Trapézio\n')
					lado = str(input('\nQual a base menor, base maior e altura do seu trapézio? Separe-as por vírgula na respectiva ordem\n'))
					lado = lado.split(',')
					b1 = float(lado[0])
					b2 = float(lado[1])
					h = float(lado[3])
					bm = (b1+b2)/2
					area = bm * h
					print('\n A área do seu trapézio é de: %.2f'%area,'\n')
				elif tipo == 6:
					print('\n Área de um quadrilátero qualquer.\n')
					print('\n Para calcularmos a área de um quadrilátero qualquer, precisaremos que você o divida em dois triângulos e nos retorne suas respectivas bases e alturas.\n')
					lado = str(input('\nQual a base e altura dos triângulos formados? Separe-as por vírgula\n'))
					lado = lado.split(',')
					l1 = float(lado[0])
					h1 = float(lado[1])
					l2 = float(lado[2])
					h2 = float(lado[3])
					area1 = (l1*h1)/2
					area2 = (l2*h2)/2
					area = area1+area2
					print('\n A área do seu quadrilátero é de: %.2f'%area,'\n')
			elif op == 8:
				print('\n Coeficiente angular da reta.\n')
				import math
				tg = float(input('\n Qual o ângulo formado pela reta junto as abscissas do seu plano cartesiano?\n'))
				coef = math.tan(tg)
				print('\n O coeficiente angular da equação da sua reta será: %.2f' % coef,'\n')


				raise ValueError("Opção inválida")
			
	except ValueError as e:
			print("Opção inválida", e)
	else:
			continue
