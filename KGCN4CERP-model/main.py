import argparse
import numpy as np
from time import time
from data_loader import load_data
from train import train

np.random.seed(555)


parser = argparse.ArgumentParser()


# movie
# parser.add_argument('--dataset', type=str, default='movie', help='which dataset to use')
# parser.add_argument('--aggregator', type=str, default='sum', help='which aggregator to use')
# parser.add_argument('--n_epochs', type=int, default=10, help='the number of epochs')
# parser.add_argument('--neighbor_sample_size', type=int, default=4, help='the number of neighbors to be sampled')
# parser.add_argument('--dim', type=int, default=16, help='dimension of user and entity embeddings')
# parser.add_argument('--n_iter', type=int, default=3, help='number of iterations when computing entity representation')
# parser.add_argument('--batch_size', type=int, default=256, help='batch size')
# parser.add_argument('--l2_weight', type=float, default=2e-5, help='weight of l2 regularization')
# parser.add_argument('--lr', type=float, default=2e-4, help='learning rate')
# parser.add_argument('--ratio', type=float, default=1, help='size of training dataset')


# book
# parser.add_argument('--dataset', type=str, default='book', help='which dataset to use')
# parser.add_argument('--aggregator', type=str, default='sum', help='which aggregator to use')
# parser.add_argument('--n_epochs', type=int, default=10, help='the number of epochs')
# parser.add_argument('--neighbor_sample_size', type=int, default=8, help='the number of neighbors to be sampled')
# parser.add_argument('--dim', type=int, default=64, help='dimension of user and entity embeddings')
# parser.add_argument('--n_iter', type=int, default=3, help='number of iterations when computing entity representation')
# parser.add_argument('--batch_size', type=int, default=256, help='batch size')
# parser.add_argument('--l2_weight', type=float, default=2e-5, help='weight of l2 regularization')
# parser.add_argument('--lr', type=float, default=2e-4, help='learning rate')
# parser.add_argument('--ratio', type=float, default=1, help='size of training dataset')


# music
parser.add_argument('--dataset', type=str, default='music', help='which dataset to use')
parser.add_argument('--aggregator', type=str, default='concat', help='which aggregator to use sum')
parser.add_argument('--n_epochs', type=int, default=20, help='the number of epochs')
parser.add_argument('--neighbor_sample_size', type=int, default=16, help='the number of neighbors to be sampled 8')
parser.add_argument('--dim', type=int, default=4, help='dimension of user and entity embeddings 16')
parser.add_argument('--n_iter', type=int, default=2, help='number of iterations when computing entity representation 1')
parser.add_argument('--batch_size', type=int, default=32, help='batch size 128')
parser.add_argument('--l2_weight', type=float, default=1e-5, help='weight of l2 regularization 1e-4')
parser.add_argument('--lr', type=float, default=1e-3, help='learning rate 5e-4')
parser.add_argument('--ratio', type=float, default=1, help='size of training dataset')




show_loss = False
show_time = False
show_topk = False


t = time()

args = parser.parse_args()
data = load_data(args)
train(args, data, show_loss, show_topk)

if show_time:
    print('time used: %d s' % (time() - t))
