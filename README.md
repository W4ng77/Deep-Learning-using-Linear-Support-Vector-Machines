# Deep-Learning-using-Linear-Support-Vector-Machines
In this project, we selected a CNN+SVM paper: Deep Learning using Linear Support Vector Machines. We tried to 4 reproduce the result obtained by following the exact method mentioned in this paper. We used online open-sourced 5 implementation of the CNN+softmax model and CNN+SVM model and plugged the hyper-parameters given in the 6 paper into the models. Finally, we found that SVM as the top layer of deep learning performs better than softmax as the 7 top layer.
data preview is in datapreview.ipynb

This project should be run in python 3.7

package needed:
	tensorflow v1.15.4, time
use 'pip install tensorflow==1.15.4'

hyper parameters are already coded in the file.



run 'python3 main.py --model 2  --dataset MNIST_data --penalty_parameter 1 --checkpoint_path ./checkpoint --log_path logs' in terminal for svm model.

run 'python3 main.py --model 1  --dataset MNIST_data --penalty_parameter 1 --checkpoint_path ./checkpoint --log_path logs' in terminal for softmax model.
