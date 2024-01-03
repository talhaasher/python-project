import sys ,os ,random,math ,pygame


speed=0.5
ap_size,sn_size=9
sepration=12
src_res_hieght=600
src_res_width=800
Fps=60
key_inputs={'UP':1,'DOWN':2,'LEFT':3,'RIGHT':4,'UP':'W','DOWN':'S','LEFT':'A','RIGHT':'D'}


pygame.init()
pygame.display.set_caption('snake')
pygame.font.init()
random.speed()

src=pygame.display.set_mode((src_res_hieght,src_res_width),pygame.HWSURFACE)

#resource
sc_font=pygame.font.Font(None,38)
sc_num_font=
