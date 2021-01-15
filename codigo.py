import cv2
import numpy as np
import pdi
import matplotlib.pyplot as plt

#Inicio 3.9
def Questao1():
	imagemb = cv2.imread('entradas\Fig0309(a)(washed_out_aerial_image).tif')
	imagemc = cv2.imread('entradas\Fig0309(a)(washed_out_aerial_image).tif')
	imagemd = cv2.imread('entradas\Fig0309(a)(washed_out_aerial_image).tif')

	pdi.transformação_gamma(imagemb,3,1)
	pdi.transformação_gamma(imagemc,4,1)
	pdi.transformação_gamma(imagemd,5,1)

	cv2.imwrite("saidas\Fig0309(b)(washed_out_aerial_image).tif", imagemb)
	cv2.imwrite("saidas\Fig0309(c)(washed_out_aerial_image).tif", imagemc)
	cv2.imwrite("saidas\Fig0309(d)(washed_out_aerial_image).tif", imagemd)

#Fim 3.9

#Inicio 3.10
def Questao2():
	imagemc = cv2.imread('entradas\Fig0310(b)(washed_out_pollen_image).tif')
	imagemd = cv2.imread('entradas\Fig0310(b)(washed_out_pollen_image).tif')


	rminimo=255
	rmaximo=0
	soma=0
	for i in range(0,imagemc.shape[0]):
		for j in range(0,imagemc.shape[1]):
			(b,g,r) = imagemc[i,j]
			if(b<rminimo):
				rminimo=b
			if(b>rmaximo):
				rmaximo=b
			soma = soma+b
	medio = soma/(imagemc.shape[0]*imagemc.shape[1])
	pdi.alargamento_de_contraste(imagemc,rminimo,0,rmaximo,255)
	pdi.alargamento_de_contraste(imagemd,medio,0,medio,255)

	cv2.imwrite('saidas\Fig0310(c)(washed_out_pollen_image).tif',imagemc)
	cv2.imwrite('saidas\Fig0310(d)(washed_out_pollen_image).tif',imagemd)

#Fim 3.10

#Inicio 3.12
def Questao3():
	imagemb = cv2.imread('entradas\Fig0312(a)(kidney).tif')
	imagemc = cv2.imread('entradas\Fig0312(a)(kidney).tif')
	pdi.fatiamento_por_intensidade(imagemb,150,255,255,0)
	pdi.fatiamento_por_intensidade(imagemc,150,255,255,1)
	cv2.imwrite('saidas\Fig0312(b)(kidney).tif',imagemb)
	cv2.imwrite('saidas\Fig0312(c)(kidney).tif',imagemc)

#Fim 3.12

#Inicio 3.14

def Questao4():
	imagem = cv2.imread('entradas\Fig0314(a)(100-dollars).tif')
	planos=[]
	for i in range (0,8):
		planos.append(cv2.imread('entradas\Fig0314(a)(100-dollars).tif'))
	pdi.fatiamento_plano_de_bits(imagem,planos)
	cv2.imwrite('saidas\Fig0314(b)(100-dollars).tif',planos[0])
	cv2.imwrite('saidas\Fig0314(c)(100-dollars).tif',planos[1])
	cv2.imwrite('saidas\Fig0314(d)(100-dollars).tif',planos[2])
	cv2.imwrite('saidas\Fig0314(e)(100-dollars).tif',planos[3])
	cv2.imwrite('saidas\Fig0314(f)(100-dollars).tif',planos[4])
	cv2.imwrite('saidas\Fig0314(g)(100-dollars).tif',planos[5])
	cv2.imwrite('saidas\Fig0314(h)(100-dollars).tif',planos[6])
	cv2.imwrite('saidas\Fig0314(i)(100-dollars).tif',planos[7])

#Fim 3.14

#Inicio 3.20

def Questao5():
	imagem1 = cv2.imread('entradas\Fig0320(1)(top_left).tif')
	imagem2 = cv2.imread('entradas\Fig0320(2)(2nd_from_top).tif')
	imagem3 = cv2.imread('entradas\Fig0320(3)(third_from_top).tif')
	imagem4 = cv2.imread('entradas\Fig0320(4)(bottom_left).tif')
	pdi.equalizacao_de_histograma(imagem1)
	pdi.equalizacao_de_histograma(imagem2)
	pdi.equalizacao_de_histograma(imagem3)
	pdi.equalizacao_de_histograma(imagem4)
	cv2.imwrite('saidas\Fig0320(5)(top_middle).tif',imagem1)
	cv2.imwrite('saidas\Fig0320(6)(2nd_from_top).tif',imagem2)
	cv2.imwrite('saidas\Fig0320(7)(third_from_top).tif',imagem3)
	cv2.imwrite('saidas\Fig0320(8)(bottom_middle).tif',imagem4)

#Fim 3.20

#Inicio 3.24
def Questao6():
	imagem = cv2.imread('entradas\Fig0323(a)(mars_moon_phobos).tif')
	pdi.equalizacao_de_histograma(imagem)
	cv2.imwrite('saidas\Fig0324(b)(mars_moon_phobos).tif',imagem)
	
#Fim 3.24
	
#Inicio 3.25
def Questao7():
	imagem = cv2.imread('entradas\Fig0323(a)(mars_moon_phobos).tif')
	pdi.especificacao_de_histograma(imagem)
	cv2.imwrite('saidas\Fig0325(c)(mars_moon_phobos).tif',imagem)
#Fim 3.25 
	
#Inicio 3.26 
def Questao8():
	imagem1 = cv2.imread('entradas\Fig0326(a)(embedded_square_noisy_512).tif')
	imagem2 = cv2.imread('entradas\Fig0326(a)(embedded_square_noisy_512).tif')
	pdi.equalizacao_de_histograma(imagem1)
	pdi.equalizacao_de_histograma_local(imagem2,3,3)
	cv2.imwrite('saidas\Fig0326(b)(embedded_square_noisy_512).tif',imagem1)
	cv2.imwrite('saidas\Fig0326(c)(embedded_square_noisy_512).tif',imagem2)
#Fim 3.26
	
#Inicio 3.27
def Questao9():
	imagem1 = cv2.imread('entradas\Fig0327(a)(tungsten_original).tif')
	imagem2 = cv2.imread('entradas\Fig0327(a)(tungsten_original).tif')
	pdi.equalizacao_de_histograma(imagem1)
	cv2.imwrite('saidas\Fig0327(b)(tungsten_original).tif',imagem1)
	pdi.realce_estatistica_histograma(imagem2,4,0.4,0.02,0.4)
	cv2.imwrite('saidas\Fig0327(c)(tungsten_original).tif',imagem2)
#Fim 3.27
	
#Inicio 3.33
def Questao10():
	imagem1 = cv2.imread('entradas\Fig0333(a)(test_pattern_blurring_orig).tif')
	imagem2 = cv2.imread('entradas\Fig0333(a)(test_pattern_blurring_orig).tif')
	imagem3 = cv2.imread('entradas\Fig0333(a)(test_pattern_blurring_orig).tif')
	imagem4 = cv2.imread('entradas\Fig0333(a)(test_pattern_blurring_orig).tif')
	imagem5 = cv2.imread('entradas\Fig0333(a)(test_pattern_blurring_orig).tif')
	pdi.filtro_de_media(imagem1,3)
	pdi.filtro_de_media(imagem2,5)
	pdi.filtro_de_media(imagem3,9)
	pdi.filtro_de_media(imagem4,15)
	pdi.filtro_de_media(imagem5,35)
	cv2.imwrite('saidas\Fig0333(b)(test_pattern_blurring_orig).tif',imagem1)
	cv2.imwrite('saidas\Fig0333(c)(test_pattern_blurring_orig).tif',imagem2)
	cv2.imwrite('saidas\Fig0333(d)(test_pattern_blurring_orig).tif',imagem3)
	cv2.imwrite('saidas\Fig0333(e)(test_pattern_blurring_orig).tif',imagem4)
	cv2.imwrite('saidas\Fig0333(f)(test_pattern_blurring_orig).tif',imagem5)
#Fim 3.33
	
#Inicio 3.34
def Questao11():
	imagem1 = cv2.imread('entradas\Fig0334(a)(hubble-original).tif')
	pdi.filtro_de_media(imagem1,15)
	cv2.imwrite('saidas\Fig0334(b)(hubble-original).tif',imagem1)
	maximo=0
	for i in range(0,imagem1.shape[0]):
		for j in range(0,imagem1.shape[1]):
			(b,g,r) = imagem1[i,j]
			if(b>maximo):
				maximo=b
	pdi.alargamento_de_contraste(imagem1,maximo/4,0,maximo/4,255)
	cv2.imwrite('saidas\Fig0334(c)(hubble-original).tif',imagem1)
#Fim 3.34
	
#Inicio 3.35
def Questao12():
	imagem1 = cv2.imread('entradas\Fig0335(a)(ckt_board_saltpep_prob_pt05).tif')
	imagem2 = cv2.imread('entradas\Fig0335(a)(ckt_board_saltpep_prob_pt05).tif')
	pdi.filtro_de_media(imagem1,3)
	pdi.filtro_de_mediana(imagem2,3)
	cv2.imwrite('saidas\Fig0335(b)(ckt_board_saltpep_prob_pt05).tif',imagem1)
	cv2.imwrite('saidas\Fig0335(c)(ckt_board_saltpep_prob_pt05).tif',imagem2)
#Fim 3.35
	
#Inicio 3.38
def Questao13():
	imagem1 = cv2.imread('entradas\Fig0338(a)(blurry_moon).tif')
	imagem2 = cv2.imread('entradas\Fig0338(a)(blurry_moon).tif')
	imagem3 = cv2.imread('entradas\Fig0338(a)(blurry_moon).tif')
	imagem4 = cv2.imread('entradas\Fig0338(a)(blurry_moon).tif')
	pdi.filtro_laplaciano_sem_ajuste(imagem1)
	pdi.filtro_laplaciano_com_ajuste(imagem2)
	pdi.filtro_laplaciano_agucado(imagem3)
	pdi.filtro_laplaciano_agucado_diagonal(imagem4)
	cv2.imwrite('saidas\Fig0338(b)(blurry_moon).tif',imagem1)
	cv2.imwrite('saidas\Fig0338(c)(blurry_moon).tif',imagem2)
	cv2.imwrite('saidas\Fig0338(d)(blurry_moon).tif',imagem3)
	cv2.imwrite('saidas\Fig0338(e)(blurry_moon).tif',imagem4)

#Fim 3.38

#Inicio 3.40
def Questao14():
	filtro_gaussiano = cv2.imread('entradas\Fig0340(a)(dipxe_text).tif')
	mascara_nitidez = cv2.imread('entradas\Fig0340(a)(dipxe_text).tif')
	filtragem_mascara = cv2.imread('entradas\Fig0340(a)(dipxe_text).tif')
	filtragem_high_boost = cv2.imread('entradas\Fig0340(a)(dipxe_text).tif')
	

	pdi.filtro_suavizacao_gaussiano(filtro_gaussiano,5,3)
	cv2.imwrite('saidas\Fig0340(b)(dipxe_text).tif',filtro_gaussiano)

	pdi.mascara_nitidez(mascara_nitidez,filtro_gaussiano)
	cv2.imwrite('saidas\Fig0340(c)(dipxe_text).tif',mascara_nitidez)

	pdi.filtragem_mascara_nitidez(filtragem_mascara,mascara_nitidez,1)
	cv2.imwrite('saidas\Fig0340(d)(dipxe_text).tif',filtragem_mascara)

	pdi.filtragem_mascara_nitidez(filtragem_high_boost,mascara_nitidez,4.5)
	cv2.imwrite('saidas\Fig0340(e)(dipxe_text).tif',filtragem_high_boost)

	
#Fim 3.40

#Inicio 3.42
def Questao15():
	imagem = cv2.imread('entradas\Fig0342(a)(contact_lens_original).tif')
	pdi.gradiente_sobel(imagem)
	cv2.imwrite('saidas\Fig0342(b)(contact_lens_original).tif',imagem)
#Fim 3.42

#Inicio 3.43
def Questao16():
	#imagem1 = cv2.imread('entradas\Fig0343(a)(skeleton_orig).tif')
	#pdi.filtro_laplaciano_com_ajuste(imagem1)
	#cv2.imwrite('saidas\Fig0343(b)(skeleton_orig).tif',imagem1)

	#imagem2 = cv2.imread('entradas\Fig0343(a)(skeleton_orig).tif')
	#pdi.filtro_laplaciano_agucado(imagem2)
	#cv2.imwrite('saidas\Fig0343(c)(skeleton_orig).tif',imagem2)

	#imagem3= cv2.imread('saidas\Fig0343(c)(skeleton_orig).tif')
	#pdi.gradiente_sobel(imagem3)
	#cv2.imwrite('saidas\Fig0343(d)(skeleton_orig).tif',imagem3)

	imagem4 = cv2.imread('saidas\Fig0343(d)(skeleton_orig).tif')
	#pdi.filtro_de_media(imagem4,5)
	#cv2.imwrite('saidas\Fig0343(e)(skeleton_orig).tif',imagem4)

	imagem5 = cv2.imread('saidas\Fig0343(c)(skeleton_orig).tif')
	pdi.mascara_nitidez(imagem5,imagem4)
	cv2.imwrite('saidas\Fig0343(f)(skeleton_orig).tif',imagem5)

	imagem6 = cv2.imread('entradas\Fig0343(a)(skeleton_orig).tif')
	pdi.filtragem_mascara_nitidez(imagem6,imagem4,1)
	cv2.imwrite('saidas\Fig0343(g)(skeleton_orig).tif',imagem6)

	imagem7 = cv2.imread('saidas\Fig0343(g)(skeleton_orig).tif')
	pdi.transformação_gamma(imagem7,0.5,1)
	cv2.imwrite('saidas\Fig0343(h)(skeleton_orig).tif',imagem7)



#Fim 3.43;

Questao9()
