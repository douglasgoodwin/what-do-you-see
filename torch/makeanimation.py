from os import listdir,getcwd,makedirs,path,walk,system
from sys import argv
import datetime
import subprocess
import argparse
import imghdr

# we want to loop through all of the images in
# a directory and match those images with style
# or content.

# you may need this:
# . ~/dgoodwin/torch/install/bin/torch-activate

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
    parser.add_argument('-g', '--gpu',
                        help='Does your video card have a GPU? 0 (yes) or -1 (no)')
    parser.add_argument('-b', '--backend',
                        help='Name your backend: nn, cudnn, cutorch, cunn')
    parser.add_argument('-w', '--width',
                        help='image width, pixels')

    results, leftovers = parser.parse_known_args()

    backend = 'nn'
    if results.backend == 'cudnn':
        backend = 'cudnn -cudnn_autotune'
    if results.backend == 'cutorch':
        backend = 'cutorch'
    if results.backend == 'cunn':
        backend = 'cunn'

    if results.outdir is None:
        outdir = path.join(getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

    results = parser.parse_args(args)
    return (results.content_images,
			results.style_image,
			outdir,
			results.gpu,
            backend,
            results.width,
			)

def makemyscript(contentimg,styleimg,outimg,gpu,backend,width):
    thescript = """th neural_style.lua \
        -content_image %s \
        -style_image %s \
        -output_image %s \
        -model_file ./models/VGG_ILSVRC_19_layers.caffemodel \
        -print_iter 4 \
        -backend %s \
        -gpu %s \
        -image_size %d""" %(contentimg,styleimg,outimg,backend,gpu,int(width))
    return str(thescript)

    # do you have a GPU handy? Set -gpu 0 . Have two? -gpu 0,1
    # nvidia-smi
    # if not, try -gpu -1

def getmyroot(afilewithpath):
    myroot = str( afilewithpath.split('/')[-1].split('.')[0] )
    return myroot

# loop through the content images
def makestyle(contentdir,styleimg,outdir,gpu,backend,width):
    for n,img in enumerate(contentdir,start=1):
      outimg = "%s/%d_S%s_C%s.png" %( outdir,n,getmyroot(styleimg),getmyroot(img) )
      dscript = makemyscript(contentimg=img,styleimg=styleimg,outimg=outimg,gpu=gpu,backend=backend,width=width)
      print("---")
      print(dscript)
      print("---")
      if DEBUG:
          subprocess.call(['echo',dscript])
      else:
          system(dscript)

def getimagefiles(adir):
    mycontentimgs = []
    for eachfile in listdir(adir):
        # only image files, please!
        fullpath = path.join(adir, eachfile)
        if imghdr.what(fullpath) is not None:
            mycontentimgs.append(fullpath)
    mycontentimgs.sort()
    return mycontentimgs

if __name__ == '__main__':
    contentdir,styleimg,outdir,gpu,backend,width = check_arg(argv[1:])
    curdir = getcwd()
    # get a list of image files
    mycontentimgs = getimagefiles(contentdir)
    if not DEBUG:
        makedirs(outdir)
        print("outdir %s is ready" %(outdir))
    makestyle(mycontentimgs,styleimg,outdir,gpu,backend,width)

    if DEBUG:
        print 'contentdir =',contentdir
        print 'styleimg =',styleimg
        print 'outdir =',outdir
        print 'gpu =',gpu
        print 'backend =',backend
        print 'width =',width
