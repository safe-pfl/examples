# SAFE-PFL distance calculator example

## What safe-pfl-distance does

`safe-pfl-distance` is a pip package that helps developers / researchers to measure these distances

- Coordinate-based distance (SAFE-PFL idea)
- Cosine distance
- Euclidean distance
- Jensen-Shannon distance
- Wasserstein distance

To submit any issues / pull requests please visit the [safe-pfl-distance](https://github.com/safe-pfl/distances) repository.

## Quick Start

To install `safe-pfl-distance` package, run

```sh
pip install safe-pfl-distance --user
```

Then clone this repository via

```sh
git clone https://github.com/safe-pfl/examples
```
  
go to the `distance` directory put the output models from the [safe-pfl](https://github.com/safe-pfl/safe-pfl) project in to respective folder in`models` directory which is a directory with bellow sub-directories at first

- alexnet
- cnn
- googlenet
- resnet
- vgg 

> [!IMPORTANT]
>
> - If you ran [safe-pfl example](https://github.com/safe-pfl/examples/safe-pfl) with for instance, ResNet model then you have to put the given models in `distance/models/resnet` path.
> - The models name must be exactly like `node_*.pth` which here * is a real number between 0 to 9 since we have 10 nodes in our Personalized Federated Learning environment.

Then run the [main.py](https://github.com/safe-pfl/distances/main.py) in the `distance` directory with the models you want to measure distances on as input parameters

```sh
cd distance # Go to the distance directory
python main.py --model resnet
```

the `--model` valid parameters are as above `alexnet`, `cnn`, `googlenet`, `resnet` and `vgg`.

the output of the `distance/main.py` will store in `distance/results` folder which have two sub-folders

- latex
- plot

Each of those folders have sub-folder respective to the parameters given as the script input.