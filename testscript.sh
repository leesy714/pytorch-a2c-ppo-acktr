#!/bin/bash
seed=2018
frames=10000000
#for i in {Frostbite,Seaquest,Pong,SpaceInvaders,BeamRider}; do
#for i in {Frostbite,Seaquest,Pong,SpaceInvaders,BeamRider,Breakout,Enduro}; do

for i in {Frostbite,Seaquest,Pong,SpaceInvaders,BeamRider,Breakout,Enduro,Gravitar,Kangaroo,Venture,Zaxxon,Skiing,Amidar}; do
    echo python main.py --algo a2c --env-name "${i}NoFrameskip-v4" --save-dir ./trained_models/frames${frames}_seed${seed} --num-frames ${frames} --save-interval 1000;
    python main.py --algo a2c --env-name "${i}NoFrameskip-v4" --save-dir ./trained_models/frames${frames}_seed${seed} --num-frames ${frames} --save-interval 1000;
done
