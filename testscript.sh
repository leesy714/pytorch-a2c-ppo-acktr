#!/bin/bash
seed=4
for i in {Pong,Seaquest}; do
    echo python main.py --env-name "${i}NoFrameskip-v4" --save-dir ./trained_models/${seed};
    python main.py --env-name "${i}NoFrameskip-v4" --save-dir ./trained_models/${seed};
done
