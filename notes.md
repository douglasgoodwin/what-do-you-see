# what do you see?
generate imagery for a short video by one of three approaches.

1. generate sequences of synthetic clouds (by conditional adversarial networks?) and submit them to an AI that determines if the images are SFW. Collect the images that will not pass for safe.
2. start a database of cloud images. search through frames of pornography for areas that may be classified as cloud. Replace the source images with clouds.
3. find the "skies" in databases of pornography. use a computer to determine if the image contains sky.

## why do this?

> Famous artists are typically renowned for a particular artistic style, which takes years to develop. Even once perfected, a single piece of art can take days or even months to create. This motivates us to explore efficient computational strategies for creating artistic images.

## things to try
gather images of clouds, add to local machine learning database.

all the images in the frame are made synthetically or generatively. for example, you might make the decor out of images of the bestselling armchairs. Or the people. Like a synthetic Komar and Melamid's [Most Wanted and Least Wanted paintings](http://www.diaart.org/program/exhibitions-projects/komar-melamid-the-most-wanted-paintings-web-project). But it's also how House of Cards was structured. People like Kevin Spacey, political intrigue, murder mysteries.

destory the personality / diversity of local coffeeshops. West Elm and AirBnB culture. Everything will be comfortable and look familiar.

shadows interacting with composited environments where the images are made from synethesis.

But start with just the clouds. Let them develop into imagery that's NSFW.

everything is produced by morphing and averaging.

Could AI create narratives? What kind of narrative would they create?

What happens when  algorithms start changing taste or aesthetics? The ice cream is made for the Instagram photo. The look of the Instagram changes the appearance and context of the ice cream. It’s designed to be an image consumed on social media. This becomes what a good ice\ cream looks like — and tastes like.

When does the world of the web start coming off the screen. When does it change the way that the coffeeshop is designed?

How does pornography set up expectations about what sexual experiences will be.


## useful software

1. [Image-to-Image Translation with Conditional Adversarial Nets](https://phillipi.github.io/pix2pix/)
2. [Tensorflow](https://www.tensorflow.org)
2. [TensorFlow CNN for fast style transfer](https://github.com/lengstrom/fast-style-transfer)
3. [Neural style in TensorFlow](https://github.com/anishathalye/neural-style)
3. American Fuzzy Lop: [Pulling JPEGs out of thin air](https://lcamtuf.blogspot.com/2014/11/pulling-jpegs-out-of-thin-air.html?m=1)
4. Google research: [Teaching Machines to draw](https://research.googleblog.com/2017/04/teaching-machines-to-draw.html?m=1), [Inceptionism](https://research.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html)
5. [Nudity detection in Python](https://github.com/hhatto/nude.py)
6. [AI Turned Bob Ross into a Terrifying Psychedelic Nightmare](https://creators.vice.com/en_us/article/bob-ross-alexander-reben-neural-network-nightmare)
7. [Pikazo App Lets You Paint Neural Network Art Masterpieces](https://creators.vice.com/en_us/article/pikazo-neural-network-art-app)
9. [Magenta: Music and Art Generation with Machine Intelligence](https://github.com/tensorflow/magenta)
10. [Genetic Programming: Mona Lisa FAQ](https://rogerjohansson.blog/2008/12/09/genetic-programming-mona-lisa-faq/)
11. [plat (v): plan out or make a map of](https://github.com/dribnet/plat)

## research, articles, courses

1. [A note on the evaluation of generative models](http://www.perceptron.net/media/publications/1511.01844v3.pdf), Lucas Theis, Aäron van den Oord, Matthias Bethge
2. [Art in the Age of Machine Intelligence](https://medium.com/artists-and-machine-intelligence/what-is-ami-ccd936394a83), Blaise Aguera y Arcas
3. [Creative Applications of Deep Learning w/ Tensorflow](https://github.com/pkmital/CADL), Parag K Mital
4. [awesome General Adversarial Networks](https://github.com/nightrome/really-awesome-gan)
5. [Sampling Generative Networks](https://arxiv.org/abs/1609.04468), Tom White
6. [Conditional generative adversarial nets for convolutional face generation](http://www.foldl.me/uploads/papers/tr-cgans.pdf), Jon Gauthier
7. [Machine Learning is Fun!](https://medium.com/@ageitgey/machine-learning-is-fun-part-3-deep-learning-and-convolutional-neural-networks-f40359318721), Adam Geitgey
8. [Convolutional neural networks for artistic style transfer](https://harishnarayanan.org/writing/artistic-style-transfer/), Harish Narayanan
9. [CS231n: Convolutional Neural Networks for Visual Recognition](http://cs231n.stanford.edu), Stanford U.
10. Publications by [Leon Gatys](http://bethgelab.org/publications/leon+gatys/)
11. [Image Style Transfer Using Convolutional Neural Networks](http://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf), Leon A. Gatys et alia

## techniques

1. [How to implement the Style Transfer algorithm in TensorFlow for combining the style and content of two images](https://www.youtube.com/watch?v=LoePx3QC5Js)

![fur-lined teacup](https://www.evernote.com/l/ADPBe2yIHIRPfZOTr11mwTlIfKeDnJKh91oB/image.png)

## institutions

1. [Google arts & culture](https://www.google.com/culturalinstitute/beta/)

## artists working in this area

### Mario Klingemann [[tumblr]](http://mario-klingemann.tumblr.com) [[twitter]](https://twitter.com/quasimondo), code artist

look at this video and document his approach. How does he "tune" his database?
[youtube: Machine learning & art - Google I/O 2016](https://youtu.be/egk683bKJYU?t=20m5s)


> 20:05 It's called fine tuning. And what it does is, you can take an already trained network, for example, the Google Net. And all you have to do is to cut off the bottom layer. And then you can retrain it with new material. And what happens is, all the top layers are pretty much the same, no matter what you train it with, because they look for abstract elements like edges, curvature, or things like that. So that doesn't need to be retrained. So doing that, you can take a trained network. You feed in new images. Instead of taking four weeks, you can train a network overnight. And the way I do it-- well, I tried it with I called it [MNIST](https://www.tensorflow.org/versions/r0.10/tutorials/mnist/beginners/) with a twist.

Mario is doing other work with morphing and averaging.

### [Cyril Diagne](https://twitter.com/kikko_fr), digital interaction artist

What can you do with 7 million digital artifacts?

![](https://icdn2.digitaltrends.com/image/sin-wave-machine-learning-720x480-c.png)


### [Oliver Husain](http://www.husain.de).
Look at the edges, see the fragility of construction.


### [Kurtis Hough](http://khstudios.com)
[Vimeo, Painted Hills](https://vimeo.com/161425126)
A sculptural and painterly look at the geometry of geology.

## who might be interested in this work?
- Jen Mergel
- Alex Galloway


## questions
1. would greyscale images provide more NSFWness?
2. where would we find a useful cloud library? See below.
3. what about [pareidolia](http://www.bbc.com/news/magazine-22686500)?


## links
 - [Facial Recognition Software Makes Art from Random Noise](http://www.smithsonianmag.com/smart-news/facial-recognition-software-makes-art-from-random-noise-15280755/)
 - [Genetic Programming: Evolution of Mona Lisa](https://rogerjohansson.blog/2008/12/07/genetic-programming-evolution-of-mona-lisa/)
 - [Deep learning datasets](http://deeplearning.net/datasets/)
 - [Cloud Atlas: world meteorological Organization](https://www.wmocloudatlas.org/)
 - [Imagenet](http://image-net.org/search?q=cloud)


## example images

these came up with a search for NSFW clouds, landscapes

![1.](https://www.evernote.com/l/ADOve536ZJpEMKuy_dTWZcGUOCqylbUlBXQB/image.png)

![sexy iceberg](http://i.imgur.com/iftQkfQ.jpg)

![sexy tree](https://s-media-cache-ak0.pinimg.com/564x/0f/c6/af/0fc6af791ae7e2dd483ebc271efa4a05.jpg)
