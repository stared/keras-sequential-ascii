# Sequential model in Keras -> ASCII

by [Piotr Migdał](http://p.migdal.pl/) from [deepsense.io](http://deepsense.io/)

See: https://github.com/fchollet/keras/issues/3873

## Install

```
pip install git+git://github.com/stared/keras-sequential-ascii.git
```

## Usage

```
from keras_sequential_ascii import sequential_model_to_ascii_printout
sequential_model_to_ascii_printout(model)
```

## Rationale

Both `model.summary()` and graph export were not enough - I wanted dimensions, numbers of parameters and activation functions in one place.
I use it for didactic purpose.

## Examples

### Proof of principle

```
      OPERATION           DATA DIMENSIONS   WEIGHTS(N)   WEIGHTS(%)

          Input   #####   (1, 28, 28)
  Convolution2D    \|/  -------------------       100     0.6%
           relu   #####   (10, 26, 26)
   MaxPooling2D   YYYYY -------------------         0     0.0%
                  #####   (10, 13, 13)
        Flatten   ||||| -------------------         0     0.0%
                  #####   (1690,)
          Dense   XXXXX -------------------     16910    98.8%
                  #####   (10,)
        Dropout    | || -------------------         0     0.0%
           relu   #####   (10,)
          Dense   XXXXX -------------------       110     0.6%
        softmax   #####   (10,)
```

### VGG16

```
      OPERATION           DATA DIMENSIONS   WEIGHTS(N)   WEIGHTS(%)

          Input   #####   (3, 224, 224)
  Convolution2D    \|/  -------------------      1792     0.0%
           relu   #####   (64, 224, 224)
  Convolution2D    \|/  -------------------     36928     0.0%
           relu   #####   (64, 224, 224)
   MaxPooling2D   YYYYY -------------------         0     0.0%
                  #####   (64, 112, 112)
  Convolution2D    \|/  -------------------     73856     0.1%
           relu   #####   (128, 112, 112)
  Convolution2D    \|/  -------------------    147584     0.1%
           relu   #####   (128, 112, 112)
   MaxPooling2D   YYYYY -------------------         0     0.0%
                  #####   (128, 56, 56)
  Convolution2D    \|/  -------------------    295168     0.2%
           relu   #####   (256, 56, 56)
  Convolution2D    \|/  -------------------    590080     0.4%
           relu   #####   (256, 56, 56)
  Convolution2D    \|/  -------------------    590080     0.4%
           relu   #####   (256, 56, 56)
   MaxPooling2D   YYYYY -------------------         0     0.0%
                  #####   (256, 28, 28)
  Convolution2D    \|/  -------------------   1180160     0.9%
           relu   #####   (512, 28, 28)
  Convolution2D    \|/  -------------------   2359808     1.7%
           relu   #####   (512, 28, 28)
  Convolution2D    \|/  -------------------   2359808     1.7%
           relu   #####   (512, 28, 28)
   MaxPooling2D   YYYYY -------------------         0     0.0%
                  #####   (512, 14, 14)
  Convolution2D    \|/  -------------------   2359808     1.7%
           relu   #####   (512, 14, 14)
  Convolution2D    \|/  -------------------   2359808     1.7%
           relu   #####   (512, 14, 14)
  Convolution2D    \|/  -------------------   2359808     1.7%
           relu   #####   (512, 14, 14)
   MaxPooling2D   YYYYY -------------------         0     0.0%
                  #####   (512, 7, 7)
        Flatten   ||||| -------------------         0     0.0%
                  #####   (25088,)
          Dense   XXXXX ------------------- 102764544    74.3%
           relu   #####   (4096,)
        Dropout    | || -------------------         0     0.0%
                  #####   (4096,)
          Dense   XXXXX -------------------  16781312    12.1%
           relu   #####   (4096,)
        Dropout    | || -------------------         0     0.0%
                  #####   (4096,)
          Dense   XXXXX -------------------   4097000     3.0%
                  #####   (1000,)
                  ||||| -------------------         0     0.0%
        softmax   #####   (1000,)
```
