from Image import *
from math import *
import sys
def split_pic_size(im,mask):
	w,h = im.size
	tw,th = mask.size
	tp = 1.0*tw/th
	if w > tp*h:
		box = (int((w-tp*h)/2),0,int((w+tp*h)/2),h)
	else:
		box = (0,int((h-w/tp)/2),w,int((h+w/tp)/2))
	new_im = im.crop(box)
	new_im = new_im.resize((tw,th),ANTIALIAS)
	return new_im
def hexagon_show(im1,mask1):
	im = im1.convert('RGBA')
	mask = mask1.convert('RGBA')
	h,w = im.size
	mask_list = [[0 for x in range(w)] for y in range(h)]
	im_list = [[0 for x in range(w)] for y in range(h)]
	for i in range(h):
		for j in range(w):
			mask_list[i][j] = mask.getpixel((i,j))
	for i in range(h):
		for j in range(w):
			im_list[i][j] = im.getpixel((i,j))
	for i in range(h):
		for j in range(w):
			if mask.getpixel((i,j)) == (0,0,0,0):
				im.putpixel([i,j],(0,0,0,0))
				im_list[i][j] = (0,0,0,0)
			else:
				pass
	im.show()
	return im
def judge_img(width):
	shi = width/10%10
	bai = width/100
	if shi <= 5:
		File_Name ='pic/'+str(bai)+'50px.png'
	elif bai == 9:
		File_Name = 'pic/'+'1000px.png'
	else:
		File_Name ='pic/'+str(bai+1)+'00px.png'
	return open(File_Name)
def main():
	imm = sys.argv[1]
	savepic = sys.argv[2]
	im = open(imm)
	im_width = im.size[0]
	mask = judge_img(im_width)
	splited_pic= split_pic_size(im,mask)
	newim = hexagon_show(splited_pic,mask)
	newim.save(savepic)
if __name__ == '__main__':
	main()
