import argparse
from safe_pfl_plotter import __version__
from safe_pfl_plotter.logs_plotter import LogsPlotter


def main(args):
    print(f"Running SAFE-PFL v{__version__} plotter example")

    LogsPlotter(
        args.log_path,
        args.plot_result_path,
        args.all_test_accuracy_mean,
        args.all_test_accuracy_std,
        args.distinct_colors,
    ).read_log_file().plot()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate model distances.")

    parser.add_argument(
        "--log_path",
        type=str,
        help="Type of the path of the log file containing test accuracy data start with date.",
    )
    parser.add_argument(
        "--plot_result_path",
        type=str,
        default="./results/plot",
        help="Path to store plot result.",
    )
    parser.add_argument(
        "--all_test_accuracy_mean",
        type=bool,
        default=True,
        help="Show clients tests accuracy mean.",
    )
    parser.add_argument(
        "--all_test_accuracy_std",
        type=bool,
        default=True,
        help="Show clients tests accuracy standard deviation.",
    )
    parser.add_argument(
        "--distinct_colors",
        type=bool,
        default=True,
        help="Show plot lines with distinguishable colors.",
    )

    args = parser.parse_args()

    # Run example
    main(args)
