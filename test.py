"""Implementation of the CNN classes"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = "0.1.0"
__author__ = "Abien Fred Agarap"

import argparse
from model.cnn_softmax import CNN
from model.cnn_svm import CNNSVM
import tensorflow as tf
import tensorflow_transform as tft

tf.summary.scalar('./')