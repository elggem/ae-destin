# tensorflow_node

<hidden..[![Build Status](https://travis-ci.org/elggem/tensorflow_node.svg?branch=master)](https://travis-ci.org/elggem/tensorflow_node)>

This is a tensorflow based framework for evaluating deep learning algorithms and streaming internal believe states out via ROS. It aims to be a flexible implemention that can be modified and inspected during runtime on live stream data. Eventually it will be used in conjunction with the [OpenCog](https://github.com/opencog/opencog) framework for integrated Artificial General Intelligence.

  - *This code is under heavy development and used for research purposes, so handle with care!*

## Documentation

You can find documentation on the [wiki](https://github.com/elggem/tensorflow_node/wiki) tab. There are references for the network architecture and some high-level descriptions on how it works.

## Participate

I've put todos and remaining tasks in the projects tab on Github. Feel free to collaborate or contact me if you have any suggestions!

## I want to run it!

Clone the repo into your catkin workspace, make it and run

    roslaunch tensorflow_node mnist.launch

TF summaries are being written to `outputs/summaries`, if enabled in the config file, and they can be inspected via this command:

    rosrun tensorflow_node tensorboard


