from sklearn.tree import export_graphviz
from training_dataset import *

import os

def export_tree(tree):
    train_labels = os.listdir(train_path)
    train_labels.sort()
    if not os.path.exists(test_path):
        os.makedirs(test_path)

    export_graphviz(tree, out_file='tree.dot', class_names=train_labels, rounded=True, filled=True)
    print("\n")
    print(f" To view the tree, copy all of the text in 'tree.dot'")
    print(f" and paste it to http://webgraphviz.com/")
    print("\n")
    return