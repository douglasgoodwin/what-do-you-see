from os import listdir,getcwd,makedirs,path,walk
from sys import argv
import datetime
import subprocess
import argparse
import imghdr

# we want to loop through all of the images in
# a directory and match those images with style
# or content.

DEBUG = False

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
    parser.add_argument('-gpu', '--gpu',
                        help='Does your video card have a GPU? 1 or -1')

    results, leftovers = parser.parse_known_args()

    if results.outdir is None:
        outdir = path.join(getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

    results = parser.parse_args(args)
    return (results.content_images,
			results.style_image,
			outdir,
			results.gpu
			)

def makemyscript(contentimg,styleimg,outimg,gpu):

    thescript = """th neural_style.lua \
        -content_image %s \
        -style_image %s \
        -output_image %s \
        -model_file /Users/dgoodwin/neural-style/models/VGG_ILSVRC_19_layers.caffemodel \
        -print_iter 4 \
        -backend cudnn -cudnn_autotune \
        -gpu %s
        -image_size 1000""" %(contentimg,styleimg,outimg,gpu)
    return str(thescript)

  # do you have a GPU handy?
  # nvidia-smi
  # if not, try -gpu -1

def getmyroot(afilewithpath):
    myroot = str( afilewithpath.split('/')[-1].split('.')[0] )
    return myroot

# loop through the content images
def makestyle(contentdir,styleimg,outdir,gpu):
    for n,img in enumerate(contentdir,start=1):
      outimg = "%s/%d_S%s_C%s.png" %( outdir,n,getmyroot(styleimg),getmyroot(img) )
      dscript = makemyscript(contentimg=img,styleimg=styleimg,outimg=outimg,gpu=gpu)
      print("---")
      print(dscript)
      print("---")
      if DEBUG:
          subprocess.call(['echo',dscript])
      else:
          subprocess.call([dscript])

def getimagefiles(adir):
    mycontentimgs = []
    for eachfile in listdir(adir):
        # only image files, please!
        fullpath = path.join(adir, eachfile)
        if imghdr.what(fullpath) is not None:
            mycontentimgs.append(fullpath)
    return mycontentimgs

if __name__ == '__main__':
    contentdir,styleimg,outdir,gpu = check_arg(argv[1:])
    curdir = getcwd()
    # get a list of image files
    mycontentimgs = getimagefiles(contentdir)
    if not DEBUG:
        makedirs(outdir)
        print("outdir %s is ready" %(outdir))
    makestyle(mycontentimgs,styleimg,outdir,gpu)

    if DEBUG:
        print 'contentdir =',contentdir
        print 'styleimg =',styleimg
        print 'outdir =',outdir
        print 'gpu =',gpu
