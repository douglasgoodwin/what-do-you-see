# we want to loop through all of the images in
# a directory and match those images with style
# or content.

myscript = """th neural_style.lua \
  -content_image %s \
  -style_image %s \
  -output_image %s \
  -model_file models/VGG_ILSVRC_19_layers.caffemodel \
  -print_iter 4 \
  -backend cudnn -cudnn_autotune \
  -image_size 1000""" (content,style,output)

from os import listdir
from optparse import OptionParser

parser = OptionParser()
curdir = '/Users/dgoodwin/what-do-you-see'
imgdir = '%s/handmovie' %(curdir)
mycontentimgs = listdir(imgdir)
mystyleimg = '%s/imgs/sources/_smoke-32.jpg' %(curdir)

def myscript(content,style,outimg):
  thescript = """th neural_style.lua \
    -content_image %s \
    -style_image %s \
    -output_image %s \
    -model_file models/VGG_ILSVRC_19_layers.caffemodel \
    -print_iter 4 \
    -backend cudnn -cudnn_autotune \
    -image_size 1000""" %(content,style,outimg)
  return str(thescript)

# loop through the content images
for n,img in enumerate(mycontentimgs,start=1):
  outimg = "out/%d_S%s_C%s.jpg" %(n,mystyleimg,img)
  dscript = myscript(content=img,style=mystyleimg,outimg=outimg)
  print(dscript)
