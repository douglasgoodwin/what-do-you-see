th neural_style.lua \
  -content_image _smoke-32.jpg \
  -style_image _weston-nude-partial.jpg \
  -output_image Csmoke_Snude-partial_cudnn_1000x.jpg \
  -model_file models/VGG_ILSVRC_19_layers.caffemodel \
  -print_iter 4 \
  -backend cudnn -cudnn_autotune \
  -image_size 1000
