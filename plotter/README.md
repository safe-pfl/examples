# SAFE-PFL plotter example

## What safe-pfl-plotter does

`safe-pfl-plotter` is a pip package that helps developers / researchers to plot the [SAFE-PFL](https://github.com/safe-pfl/safe-pfl) log file.

To submit any issues / pull requests please visit the [safe-pfl-plotter](https://github.com/safe-pfl/plotter) repository.

## Quick Start

To install `safe-pfl-plotter` package, run

```sh
pip install safe-pfl-plotter --user
```

Then clone this repository via

```sh
git clone https://github.com/safe-pfl/examples
```
  
go to the `plotter` directory anf put the _*.log_ file from the [safe-pfl](https://github.com/safe-pfl/safe-pfl) project in it.

> [!IMPORTANT]
>
> - If you ran [safe-pfl example](https://github.com/safe-pfl/examples/safe-pfl) on different dates then the log file is different respective to the its running date.
> The code with find the number of clients with regex so please DO NOT change the log file and you DO NOT need to pass the number of contributing nodes / clients in Federated Learning environment.

Then run the [logs_plotter.py](./logs_plotter.py) in the `plotter` directory with the log file you want to plot each clients accuracies.

```sh
cd plotter # Go to the plotter directory
python ./logs_plotter.py --log_path *.log --plot_result_path ./results/plot # don't add .png extension
```

the output of the `plotter/logs_plotter.py` will store in `plotter/results/plot.png` path.

> [!NOTE]
>
> Other input parameters are `--all_test_accuracy_mean` which is a boolean, if set to `true` this wil show the mean of clients / nodes test accuracies. The `--all_test_accuracy_std` also show the standard deviations of clients / nodes test accuracies id set to `true`. the `--distinct_colors` will plot the chart with distinguishable colors if set to `true`.
