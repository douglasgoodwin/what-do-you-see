from os import listdir,getcwd,makedirs
import datetime
import subprocess
from optparse import OptionParser

# we want to loop through all of the images in
# a directory and match those images with style
# or content.

DEBUG = True
parser = OptionParser()
curdir = '/Users/dgoodwin/what-do-you-see'
imgdir = '%s/handmovie' %(curdir)
mycontentimgs = listdir(imgdir)
mystyleimg = '%s/imgs/sources/_smoke-32.jpg' %(curdir)

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Transfer style from one image to multiple content images')
    parser.add_argument('-c', '--content_images',
                        help='a folder containing multiple content images',
                        required='True')
    parser.add_argument('-s', '--style_image',
                        help='a single image with style to transfer',
                        required='True')
    parser.add_argument('-o', '--outdir',
                        help='an output directory. it defaults to a timestamp.')

    results, leftovers = parser.parse_known_args()

    if results.outdir is None:
        outdir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H%M'))
        # you want this somewhere else
        # makedirs(mydir)

    results = parser.parse_args(args)
    return (results.url,
            results.infile,
            results.outfile)


# myscript = """th neural_style.lua \
#   -content_image %s \
#   -style_image %s \
#   -output_image %s \
#   -model_file models/VGG_ILSVRC_19_layers.caffemodel \
#   -print_iter 4 \
#   -backend cudnn -cudnn_autotune \
#   -image_size 1000""" (content,style,output)

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
  outimg = "%s/out/%d_S%s_C%s.jpg" %(curdir,n,mystyleimg,img)
  65_S/Users/dgoodwin/what-do-you-see/imgs/sources/_smoke-32.jpg_Cimage-0154.jpeg.jpg
  dscript = myscript(content=img,style=mystyleimg,outimg=outimg)
  if DEBUG:
      subprocess.call(['echo',dscript])
  else:
      system('echo %s' %(dscript))
