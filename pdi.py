import numpy as np
import cv2
import math
def transformação_gamma(imagem,gamma,c):
	altura = imagem.shape[0]
	largura = imagem.shape[1]
	for i in range(0, altura):
		for j in range (0,largura):
			(b, g, r) = imagem[i, j]
			b = 255*c*((b/255)**gamma)
			imagem[i,j] = (b ,b ,b)

def alargamento_de_contraste(imagem,r1,s1,r2,s2):
	altura = imagem.shape[0]
	largura = imagem.shape[1]
	if(r1!=0):
		alpha0 = s1/r1
	else:
		alpha0=0
	if(r1!=r2):
		alpha1 = (s2-s1)/(r2-r1)
	if(r2!=255):
		alpha2 = (255-s2)/(255-r2)
	else:
		alpha2=0
	for i in range(0, altura):
		for j in range (0,largura):
			(b, g, r) = imagem[i, j]
			if(b<=r1):
				b = alpha0*b
			elif(b>r1 and b<r2):
				b = alpha1*(b-r1) + s1
			elif(b>=r2):
				b = alpha2*(b-r2) + s2
			imagem[i,j] = (b,b,b)

def fatiamento_por_intensidade(imagem,inicio,fim,intensidade,modo):
	if(modo==0):
		for i in range(0,imagem.shape[0]):
			for j in range(0,imagem.shape[1]):
				(b,g,r) = imagem[i,j]
				if(b>=inicio and b<=fim):
					imagem[i,j]=(intensidade,intensidade,intensidade)
				else:
					imagem[i,j]=(0,0,0)
	else:
		for i in range(0,imagem.shape[0]):
			for j in range(0,imagem.shape[1]):
				(b,g,r) = imagem[i,j]
				if(b>=inicio and b<=fim):
					imagem[i,j]=(intensidade,intensidade,intensidade)

def fatiamento_plano_de_bits(imagem,planos):
	altura = imagem.shape[0]
	largura = imagem.shape[1]
	for plano in range (0,8):
		for i in range(0,altura):
			for j in range(0,largura):
				(b,g,r) = imagem[i,j]
				aux = 255*(b%2)
				planos[plano][i,j] = (aux,aux,aux)
				aux2=int(b/2)
				imagem[i,j] = (aux2,aux2,aux2)

def equalizacao_de_histograma(imagem):
	altura = imagem.shape[0]
	largura = imagem.shape[1]
	somatorio = [0] * 256
	for i in range (0,altura):
		for j in range (0,largura):
			(b,g,r) = imagem[i,j]
			somatorio[b] = somatorio[b] + 1
	for k in range (0,256):
		if(k!=255):
			somatorio[k+1] = somatorio[k+1] + somatorio[k]
		somatorio[k] = int((255*somatorio[k])/(altura*largura))
	for i in range (0,altura):
		for j in range (0,largura):
			(b,g,r) = imagem[i,j]
			imagem[i,j] = (somatorio[b],somatorio[b],somatorio[b])
def funcao3_25(x):
	if(x>=0 and x<=5):
		return x*7/5
	elif(x>5 and x<=20):
		return 7 - 6.3*(x-5)/15
	elif(x>20 and x<=181):
		return 0.7 - 0.7*(x-20)/161
	elif(x>181 and x<=202):
		return (x-181)*0.53/21
	elif(x>202 and x<=255):
		return 0.53 - (x-202)*0.53/63
	return 0
def especificacao_de_histograma(imagem):
	altura = imagem.shape[0]
	largura = imagem.shape[1]
	s = [0] * 256
	z = [0] * 256
	z_inversa = [0] * 256
	z_soma = 0
	for i in range (0,altura):
		for j in range (0,largura):
			(b,g,r) = imagem[i,j]
			s[b] = s[b] + 1
	for k in range (0,256):
		z[k] = funcao3_25(k)
		z_soma = z_soma + z[k]
	for k in range (0,256):
		if(k!=255):
			s[k+1] = s[k+1] + s[k]
			z[k+1] = z[k+1] + z[k]
		s[k] = int((255*s[k])/(altura*largura))
		z[k] = int((255*z[k])/(z_soma))
	z_inversa[255] = 255
	for k in range (254,-1,-1):
		for a in range (z[k],z[k+1]):
			z_inversa[a] = k
	for i in range (0,altura):
		for j in range (0,largura):
			(b,g,r) = imagem[i,j]
			imagem[i,j] = (z_inversa[s[b]],z_inversa[s[b]],z_inversa[s[b]])

def equalizacao_de_histograma_local(imagem,h,l):
	altura = imagem.shape[0]
	largura = imagem.shape[1]
	somatorio = [0] * 256
	for i in range (0,altura-h,h):
		for j in range (0,largura-l,l):
			somatorio = [0] * 256
			for x in range (i,i+h):
				for y in range (j,j+l):
					(b,g,r) = imagem[x,y]
					somatorio[b] = somatorio[b] + 1
			for k in range (0,256):
				if(k!=255):
					somatorio[k+1] = somatorio[k+1] + somatorio[k]
				somatorio[k] = int((255*somatorio[k])/(h*l))
			for x in range (i,i+h):
				for y in range (j,j+l):
					(b,g,r) = imagem[x,y]
					imagem[x,y] = (somatorio[b],somatorio[b],somatorio[b])
		#Último quadrante de uma linha
		if(largura%l!=0):
			somatorio = [0] * 256
			for x in range (i,i+h):
				for y in range (largura-largura%l,largura):
					(b,g,r) = imagem[x,y]
					somatorio[b] = somatorio[b] + 1
			for k in range (0,256):
				if(k!=255):
					somatorio[k+1] = somatorio[k+1] + somatorio[k]
				somatorio[k] = int((255*somatorio[k])/(h*(largura%l)))
			for x in range (i,i+h):
				for y in range (largura-largura%l,largura):
					(b,g,r) = imagem[x,y]
					imagem[x,y] = (somatorio[b],somatorio[b],somatorio[b])
	#Última linha
	if(altura%h!=0):
		for j in range (0,largura-l,l):
			somatorio = [0] * 256
			for x in range (altura-altura%h,altura):
				for y in range (j,j+l):
					(b,g,r) = imagem[x,y]
					somatorio[b] = somatorio[b] + 1
			for k in range (0,256):
				if(k!=255):
					somatorio[k+1] = somatorio[k+1] + somatorio[k]
				somatorio[k] = int((255*somatorio[k])/((altura%h)*l))
			for x in range (altura-altura%h,altura):
				for y in range (j,j+l):
					(b,g,r) = imagem[x,y]
					imagem[x,y] = (somatorio[b],somatorio[b],somatorio[b])
	#Último quadrante
	if(altura%h!=0 and largura%l!=0):
		somatorio = [0] * 256
		for x in range (altura-altura%h,altura):
			for y in range (largura-largura%l,largura):
				(b,g,r) = imagem[x,y]
				somatorio[b] = somatorio[b] + 1
		for k in range (0,256):
			if(k!=255):
				somatorio[k+1] = somatorio[k+1] + somatorio[k]
			somatorio[k] = int((255*somatorio[k])/((altura%h)*(largura%l)))
		for x in range (altura-altura%h,altura):
			for y in range (largura-largura%l,largura):
				(b,g,r) = imagem[x,y]
				imagem[x,y] = (somatorio[b],somatorio[b],somatorio[b])

def realce_estatistica_histograma(imagem,E,k0,k1,k2):
	altura = imagem.shape[0]
	largura = imagem.shape[1]
	novaImagem=[]
	media=0
	variancia=0
	for i in range (0,altura):
		for j in range (0,largura):
			(b,g,r) = imagem[i,j]
			media = media + b
	media = media/(altura*largura)
	for i in range (0,altura):
		for j in range (0,largura):
			(b,g,r) = imagem[i,j]
			variancia = variancia+((b-media)**2)
	variancia = variancia/(altura*largura)
	for i in range (0,altura):
		for j in range (0,largura):
			variancia_local=0
			media_local=0
			for x in range (i-1,i+2):
				for y in range (j-1,j+2):
					if(x>=0 and x<altura and y>=0 and y<largura):
						(b,g,r) = imagem[x,y]
						media_local=media_local+b
			media_local=media_local/9
			for x in range (i-1,i+2):
				for y in range (j-1,j+2):
					if(x>=0 and x<altura and y>=0 and y<largura):
						(b,g,r) = imagem[x,y]
						variancia_local=variancia_local+(b-media_local)**2
			variancia_local=variancia_local/9
			(b,g,r) = imagem[i,j]
			if(media_local<=k0*media and k1*variancia<=variancia_local and k2*variancia>=variancia_local):
				aux=E*b
				if(aux>255):
					aux=255
				novaImagem.append(aux)
			else:
				novaImagem.append(b)
	for i in range (0,altura):
		for j in range (0,largura):
			aux=novaImagem[i*largura+j]
			imagem[i,j]=(aux,aux,aux)

def filtro_de_media(imagem,n):
	altura = imagem.shape[0]
	largura = imagem.shape[1]
	novaImagem = []
	for i in range (0,altura):
		for j in range (0,largura):
			media = 0
			contador=0
			for x in range (i-int(n/2),i+int(n/2)+1):
				for y in range (j-int(n/2),j+int(n/2)+1):
					if(x<altura and y<largura and x>=0 and y>=0):
						(b,g,r) = imagem[x,y]
						media = media+b
						contador=contador+1
			media=media/contador
			novaImagem.append(media)
	for i in range (0,altura):
		for j in range (0,largura):
			imagem[i,j] = (novaImagem[i*largura+j],novaImagem[i*largura+j],novaImagem[i*largura+j])
def filtro_de_mediana(imagem,n):
	altura = imagem.shape[0]
	largura = imagem.shape[1]
	novaImagem = []
	vetorOrdenacao = []
	for i in range (0,altura):
		for j in range (0,largura):
			vetorOrdenacao.clear()
			for x in range (i-int(n/2),i+int(n/2)+1):
				for y in range (j-int(n/2),j+int(n/2)+1):
					if(x<altura and x>=0 and y>=0 and y<largura):
						(b,g,r) = imagem[x,y]
						if(len(vetorOrdenacao)==0 or vetorOrdenacao[len(vetorOrdenacao)-1]<=b):
							vetorOrdenacao.append(b)
						else:
							for k in range(0,len(vetorOrdenacao)):
								if(b<=vetorOrdenacao[k]):
									vetorOrdenacao.insert(k,b)
									b=256
			mediana=vetorOrdenacao[int(len(vetorOrdenacao)/2)]
			novaImagem.append(mediana)
	for i in range (0,altura):
		for j in range (0,largura):
			imagem[i,j] = (novaImagem[i*largura+j],novaImagem[i*largura+j],novaImagem[i*largura+j])

def filtro_laplaciano_sem_ajuste(imagem):
	altura = imagem.shape[0]
	largura = imagem.shape[1]
	novaImagem = []
	for i in range (0,altura):
		for j in range (0,largura):
			s=0
			if(i>0):
				(a1,a2,a3) = imagem[i-1,j]
				s=s+int(a1)
			if(i<altura-1):
				(b1,b2,b3) = imagem[i+1,j]
				s=s+int(b1)
			if(j>0):
				(c1,c2,c3) = imagem[i,j-1]
				s=s+int(c1)
			if(j<largura-1):
				(d1,d2,d3) = imagem[i,j+1]
				s=s+int(d1)
			(e1,e2,e3) = imagem[i,j]
			s = (s-4*int(e1))
			if(s>255):
				s=255
			elif(s<0):
				s=0
			novaImagem.append(s)
	for i in range (0,altura):
		for j in range (0,largura):
			aux=novaImagem[i*largura+j]
			imagem[i,j] = (aux,aux,aux)
def filtro_laplaciano_com_ajuste(imagem):
	altura = imagem.shape[0]
	largura = imagem.shape[1]
	novaImagem = []
	minimo = 255
	maximo = 0
	for i in range (0,altura):
		for j in range (0,largura):
			s=0
			if(i>0):
				(a1,a2,a3) = imagem[i-1,j]
				s=s+a1
			if(i<altura-1):
				(b1,b2,b3) = imagem[i+1,j]
				s=s+b1
			if(j>0):
				(c1,c2,c3) = imagem[i,j-1]
				s=s+c1
			if(j<largura-1):
				(d1,d2,d3) = imagem[i,j+1]
				s=s+d1
			(e1,e2,e3) = imagem[i,j]
			s = s-4*e1
			if(s<minimo):
				minimo=s
			if(s>maximo):
				maximo=s
			novaImagem.append(int(s))
	for i in range (0,altura):
		for j in range (0,largura):
			aux=int(255*((novaImagem[i*largura+j]-minimo)/(maximo-minimo)))
			imagem[i,j] = (aux,aux,aux)
def filtro_laplaciano_agucado(imagem):
	altura = imagem.shape[0]
	largura = imagem.shape[1]
	novaImagem = []
	minimo = 255
	maximo = 0
	for i in range (0,altura):
		for j in range (0,largura):
			s=0
			if(i>0):
				(a1,a2,a3) = imagem[i-1,j]
				s=s+a1
			if(i<altura-1):
				(b1,b2,b3) = imagem[i+1,j]
				s=s+b1
			if(j>0):
				(c1,c2,c3) = imagem[i,j-1]
				s=s+c1
			if(j<largura-1):
				(d1,d2,d3) = imagem[i,j+1]
				s=s+d1
			(e1,e2,e3) = imagem[i,j]
			s = s-4*e1
			if(s>255):
				s=255
			elif(s<0):
				s=0
			novaImagem.append(int(s))
	for i in range (0,altura):
		for j in range (0,largura):
			(b,g,r)=imagem[i,j]
			aux=b-novaImagem[i*largura+j]
			if(aux<0):
				aux=0
			imagem[i,j] = (aux,aux,aux)
def filtro_laplaciano_agucado_diagonal(imagem):
	altura = imagem.shape[0]
	largura = imagem.shape[1]
	indice = 0
	novaImagem = []
	for i in range (0,altura):
		for j in range (0,largura):
			s=0
			for x in range (i-1,i+2):
				for y in range (j-1,j+2):
					if(x>=0 and y>=0 and x<altura and y<largura):
						(b,g,r)=imagem[x,y]
						if(x==i and y==j):
							s=s-8*b
						else:
							s=s+b
			if(s<0):
				s=0
			if(s>255):
				s=255
			novaImagem.append(s)
	for i in range (0,altura):
		for j in range (0,largura):
				(b,g,r)=imagem[i,j]
				aux=b-novaImagem[i*largura+j]
				if(aux<0):
					aux=0
				imagem[i,j]=(aux,aux,aux)
def filtro_suavizacao_gaussiano(imagem,n,desvio):
	altura=imagem.shape[0]
	largura=imagem.shape[1]
	delta=int(n/2)
	coeficientes=[]
	k=0
	novaImagem=[]
	for x in range (-delta,delta+1):
		for y in range (-delta,delta+1):
			coeficientes.append(math.exp(-(((x**2)+(y**2))/(2*(desvio**2)))))
			k=k+math.exp(-(((x**2)+(y**2))/(2*(desvio**2))))
	for i in range (0,altura):
		for j in range (0,largura):
			s=0
			for x in range (i-delta,i+delta+1):
				for y in range (j-delta,j+delta+1):
					if(x>=0 and y>=0 and x<altura or y<largura):
						(b,g,r)=imagem[i,j]
						coeficiente=coeficientes[(2*delta+1)*(x-i+delta)+(y-j+delta)]
						s=s+b*coeficiente
			novaImagem.append(int(s/k))
	for i in range (0,altura):
		for j in range (0,largura):
			if(i>0 and j>0 and i<altura-1 and j<largura-1):
				a=novaImagem[i*largura+j]
				imagem[i,j] = (a,a,a)

def mascara_nitidez(imagem_original,imagem_borrada):
	altura=imagem_original.shape[0]
	largura=imagem_original.shape[1]
	for i in range (0,altura):
		for j in range (0,largura):
			(b1,g1,r1) = imagem_original[i,j]
			(b2,g2,r2) = imagem_borrada[i,j]
			aux=int(b1)-int(b2)
			if(aux<0):
				aux=0
			imagem_original[i,j]=(aux,aux,aux)

def filtragem_mascara_nitidez(imagem,mascara,k):
	altura=imagem.shape[0]
	largura=imagem.shape[1]
	for i in range (0,altura):
		for j in range (0,largura):
			(b1,g1,r1) = imagem[i,j]
			(b2,g2,r2) = mascara[i,j]
			aux=int(b1+k*b2)
			if(aux>255):
				aux=255
			imagem[i,j]=(aux,aux,aux)

def gradiente_sobel(imagem):
	altura=imagem.shape[0]
	largura=imagem.shape[1]
	wx=[[1,2,1],[0,0,0],[-1,-2,-1]]
	wy=[[-1,0,1],[-2,0,2],[-1,0,1]]
	novaImagem=[]
	for i in range (0,altura):
		for j in range (0,largura):
			gx=0
			gy=0
			for x in range (i-1,i+2):
				for y in range (j-1,j+2):
					if(x>=0 and y>=0 and y<largura and x<altura):
						(b,g,r) = imagem[x,y]
						gx=gx+b*wx[x-i+1][y-j+1]
						gy=gy+b*wy[x-i+1][y-j+1]
			modulo=abs(gx)+abs(gy)
			if(modulo>255):
				modulo=255
			elif(modulo<0):
				modulo=0
			novaImagem.append(modulo)
	for i in range (0,altura):
		for j in range (0,largura):
			aux=novaImagem[i*largura+j]
			imagem[i,j] = (aux,aux,aux)

