# Sequential model in Keras -> ASCII

by [Piotr Migdał](http://p.migdal.pl/)

A library for [Keras](https://keras.io/) for investigating architectures and parameters of sequential models.

Both `model.summary()` and graph export were not enough - I wanted array dimensions, numbers of parameters and activation functions in one place.
I use it for didactic purpose.

* TODO
  * Add ASCII art for more layers.
  * Go beyond simple sequential models (e.g. to allow *merge* layers); any ideas how?
  * Consider PRing to the main Keras repo, see [#3873](https://github.com/fchollet/keras/issues/3873).

See this library in the wild, for example:

* [Cifar-10 Classification using Keras Tutorial](https://blog.plon.io/tutorials/cifar-10-classification-using-keras-tutorial/) at Plon.io

## Installation

```
pip install git+git://github.com/stared/keras-sequential-ascii.git
```

## Usage

```
from keras_sequential_ascii import sequential_model_to_ascii_printout
sequential_model_to_ascii_printout(model)
```

## Examples

### Proof of principle

```
           OPERATION           DATA DIMENSIONS   WEIGHTS(N)   WEIGHTS(%)

               Input   #####      3   32   32
  BatchNormalization    μ|σ  -------------------        64     0.1%
                       #####      3   32   32
       Convolution2D    \|/  -------------------       448     0.8%
                relu   #####     16   30   30
       Convolution2D    \|/  -------------------      2320     4.3%
                relu   #####     16   28   28
        MaxPooling2D   Y max -------------------         0     0.0%
                       #####     16   14   14
       Convolution2D    \|/  -------------------       272     0.5%
                tanh   #####     16   14   14
             Flatten   ||||| -------------------         0     0.0%
                       #####        3136
               Dense   XXXXX -------------------     50192    94.1%
                       #####          16
             Dropout    | || -------------------         0     0.0%
                       #####          16
               Dense   XXXXX -------------------        51     0.1%
             softmax   #####           3
```

### VGG16

```
           OPERATION           DATA DIMENSIONS   WEIGHTS(N)   WEIGHTS(%)

              Input   #####      3  224  224
         InputLayer     |   -------------------         0     0.0%
                      #####      3  224  224
      Convolution2D    \|/  -------------------      1792     0.0%
               relu   #####     64  224  224
      Convolution2D    \|/  -------------------     36928     0.0%
               relu   #####     64  224  224
       MaxPooling2D   Y max -------------------         0     0.0%
                      #####     64  112  112
      Convolution2D    \|/  -------------------     73856     0.1%
               relu   #####    128  112  112
      Convolution2D    \|/  -------------------    147584     0.1%
               relu   #####    128  112  112
       MaxPooling2D   Y max -------------------         0     0.0%
                      #####    128   56   56
      Convolution2D    \|/  -------------------    295168     0.2%
               relu   #####    256   56   56
      Convolution2D    \|/  -------------------    590080     0.4%
               relu   #####    256   56   56
      Convolution2D    \|/  -------------------    590080     0.4%
               relu   #####    256   56   56
       MaxPooling2D   Y max -------------------         0     0.0%
                      #####    256   28   28
      Convolution2D    \|/  -------------------   1180160     0.9%
               relu   #####    512   28   28
      Convolution2D    \|/  -------------------   2359808     1.7%
               relu   #####    512   28   28
      Convolution2D    \|/  -------------------   2359808     1.7%
               relu   #####    512   28   28
       MaxPooling2D   Y max -------------------         0     0.0%
                      #####    512   14   14
      Convolution2D    \|/  -------------------   2359808     1.7%
               relu   #####    512   14   14
      Convolution2D    \|/  -------------------   2359808     1.7%
               relu   #####    512   14   14
      Convolution2D    \|/  -------------------   2359808     1.7%
               relu   #####    512   14   14
       MaxPooling2D   Y max -------------------         0     0.0%
                      #####    512    7    7
            Flatten   ||||| -------------------         0     0.0%
                      #####       25088
              Dense   XXXXX ------------------- 102764544    74.3%
               relu   #####        4096
              Dense   XXXXX -------------------  16781312    12.1%
               relu   #####        4096
              Dense   XXXXX -------------------   4097000     3.0%
            softmax   #####        1000
```
