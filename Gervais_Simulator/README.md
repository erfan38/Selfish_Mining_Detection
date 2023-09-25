
# This is a usage of ns-3-allinone to capture data from a bitcoin network

The usage to use basic ns-3 (netanim and ns-3-dev) is to type:

./download.py

./build.py

The usage to use ns-3 under a bitcoin network is to type:

./waf

./waf --run "bitcoin-test --noBlocks=8 --nodes=16"

with the above command, you determine a bitcoin network with 16 nodes and 8 blocks to be mined. and you are supposed to run bitcoin-test.cc
If you want to get a dataset for an attacked network:

./waf --run scratch/selfish-miner-test

# Plan:

 1- capturing several features related to nodes and network that are important in launching Selfish Mining attacks on a bitcoin network

 2- Storing captured data as a dataset for both Attacked and Benign networks


 3- Homogenizing headers of two CSV files consisting of captured data from benign and attacked network:
There are two types of information we can capture from the network, those information related to each node, and the information related to the whole netwrok. We can have a single CSV file but for better comparison between attacked network and benign network, we consider one csv file consisting of information related to each node and the information related to the network during each iteration.
  The dataset consists of 1600 rows for 100 iterations if the number of miners is 16.

Now we need to homogenize the headers; It means that we need to capture the same features from both networks to have a better comparison and a better process in Deep Learning part of this project.

# 2- Normalizing the dataset
I plan to clean datasets using converting data to numeric values. Then, Min-Max scaling for normalization, and StandardScaler for standardization will be utilized.

# 3- Select our ML model and start training
First, we aim to use Random Forest Classification (RFC), aiming to gain a better understanding of whether we have obtained valuable datasets or not.


# ITERATIONS branch is getting results for iterations=100.

I got results for both benign and selfish network with 16 nodes and 100 times iterations.

I moved for loop for iterations = 100 to the main function, as we want to run bitcoin blockchain in every iteration to avoid similar results.

o I homogenized headers for both dataset.

I homogenized the functions for both selfish and benign network.

Here, we have two types of features, related to each node and the whole network caputred by calling the functions named: printForEachNode, printTotalNodes

For benign network:

The result for iterations are the same. We need to fix this problem. The problem is related to the place of for loop. I believe that we need to create the bitcoin network from the step 1 and run it and get our desire results.

For Selfish network:

The results we got are rational and we can move on to next step, normalizing the dataset.

benign_eachnode8.csv : has 1600 rows but we remove the for loop inside the functions/ or the for loop above calling the function and put it at the first lines of main function. The result, benign_eachnode9.csv wasn't good as it is saved only 15 rows. so we need to work on this part to fix the issue.

in benign_totalnode8.csv, 100 rows are saved but they are the same. so we desided to change the loop (the above solution) but in benign_totalnode9.csv only one row is saved. Fix this tomorrow maybe it is overwritten.

===========================================================================================================
TO SUM UP:

I fixed the problem and got datasets from benign network (iterations = 100, number of miners = 16). You can find datasets for benign network in RESULTS_B and for selfish network in RESULTS_S. Both datasets generated from benign and attached network consisting of 100 iterations for 16 miners.
NEXT STEP: we should normalize and standardize datasets in order to have a valuable dataset for ML techniques we are going to use.
