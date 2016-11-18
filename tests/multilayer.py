#!/usr/bin/env python
# -*- coding: utf-8 -*-

from code import StackedAutoEncoder
from code import SummaryWriter
from code import OpenCVInputLayer
from code import log

log.info("recording summaries to " + SummaryWriter().directory)

model = StackedAutoEncoder(
        dims=[100, 100],
        activations=['linear', 'linear'], 
        noise='gaussian', 
        epoch=[100, 100],
        loss='rmse',
        lr=0.007,
        metadata=True,
        timeline=True
    )

# Initialize input layer, register callback and feed video
inputlayer = OpenCVInputLayer(output_size=(28,28), batch_size=5)

inputlayer.registerCallback([0,0,28,28], model.fit_transform)

def foo(ae, data):
    log.info(str(data.shape))

model.registerCallback(foo)

inputlayer.feedVideo("data/mnist.mp4", frames=20)

model.max_activation_summary()
model.save_parameters()