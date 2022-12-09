from sklearn.tree import DecisionTreeClassifier
from create_dataset import *
from formatting_output import *
from training_dataset import *

tree = DecisionTreeClassifier(random_state=seed)

if __name__ == "__main__":
    print("==================================================================")
    print("         BATIK PATTERN CLASSIFICATION USING DECISION TREE         ")
    print("==================================================================")
    print("                 List of Command: ")
    print(" 1. CREATE   : to create dataset")
    print(" 2. TRAIN    : to train the model in 'dataset/train/' folder")
    print(" 3. TEST     : to test the model in 'dataset/test/' folder")
    print(" 4. EXPORT   : to export 'tree.dot' file")
    print(" 5. QUIT     : to exit the program")
    print()

    while True:
        try:
            command = input(">>> ")

            if command == "CREATE":
                prepare_data()
            elif command == "TRAIN":
                tree  = DecisionTreeClassifier(random_state=seed)
                train_model(tree)
            elif command == "TEST":
                test_model(tree)
            elif command == "EXPORT":
                export_tree(tree)
            elif command == "QUIT":
                break
            else:
                print("INVALID COMMAND")
                
        except:
            print("ERROR : PLEASE TRY ANOTHER COMMAND")