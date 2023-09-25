This project is named "Efficient Detection of Selfish Mining Attacks in Blockchain Systems Using Machine Learning".

We used PCA and RFC to detect selfish minig attack in a bitcoin network. First, we applied our approach on an existing dataset. Then, we generated our dataset within a simulated bitcoin network. Finally, we compare our results with the existing work.

Dataset 0 contains 32 features of the bitcoin network gathered from a simulated environment. All of the features are important in case of selfish mining attacks, but most of them are dependent on simulator's parameter as they might be independent in a real-time bitcoin network. We analyzed all of them and figured out only 6 of them are independent from the simulator's network and are useful for this attack Detection:

Dataset 1 is the existing dataset generated from ForkDec paper.
Dataset 2 is the simulated dataset that we gathered by modifying a bitcoin simulator presented by Aurthor Gervais. We modified this simulator by adding some features to capture from the bitcoin network.
Dataset 3 contains only one feature that is important in Selfish mining attack detection.

PCA_final.py is the code for PCA used for D1 ( we applied PCA on both training and testing dataset with the same PCA model)

pca_1.py is the code for PCA used for D2

preprocessing_D2_D3.py is the code for preprocessing and Random forest classification on Dataset 2 and Dataset 3

RFC.py random forest classificaiton code

D1_PCA_norm_RFC is the code for dataset 1

FC_NN.py is the code for fully connected neural network used for dataset 2 and dataset 3

shuffle_6f.csv is Dataset 2
reduced_dims_6f.csv is the output of PCA on Dataset 2
shuffle_data1_receivedTime.csv is Dataset 3
reduced_dims_1f.csv is the output of PCA on Dataet 3
testing.csv and training.csv are Dataset 1 ( ForkDec dataset)
reduced_dims_training.csv the output of PCA on Dataset 1
reduced_dims_testing.csv the output of PCA on Dataset 1
