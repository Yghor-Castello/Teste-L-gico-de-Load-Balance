def logica_para_adicionar_usuarios(l: list, umax: int) -> list:
	if(l[-1] == umax):
		l.append(1)
	else:
		l[-1] += 1
	return l

def logica_para_retirar_usuarios(l: list) -> list:
	if(l[0] > 0):
		l[0] -= 1
	else:
		l[1] -= 1
	if(l[0] == 0):
		del l[0]
	return l

def main():
	l = [0] #lista que representa quantidade de usuarios por servidores
	tisk = 1
	list_qtd_users = []
	custo_total = 0
	try:
		ttask = int(input())
		umax = int(input())
		while True:
			qtd_users = int(input())
			list_qtd_users.append(qtd_users)
			for i in range(qtd_users):
				l = logica_para_adicionar_usuarios(l, umax)
			if(tisk > ttask):
				for i in range(list_qtd_users.pop(0)):
					l = logica_para_retirar_usuarios(l)
			print(",".join(map(str,l)))
			custo_total += len(l)
			tisk += 1
	except EOFError:
		while(len(list_qtd_users)):
			qtd_de_usuarios_que_vao_sair = list_qtd_users.pop(0)
			for i in range(qtd_de_usuarios_que_vao_sair):
				l = logica_para_retirar_usuarios(l)
			print(",".join(map(str,l))) if len(l) else print(0)
			custo_total += len(l)
		print(custo_total)
		return 
#só roda pelo terminal
if __name__ == "__main__":
	main()