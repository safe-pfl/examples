import argparse
from safe_pfl_distance import __version__
from safe_pfl_distance.distance import ModelDistancesCalculator

from safe_pfl_distance.nets.cnn_net import Net
from safe_pfl_distance.nets.res_net import Net
from safe_pfl_distance.nets.google_net import Net
from safe_pfl_distance.nets.alex_net import Net
from safe_pfl_distance.nets.alex_net import Net


def main(args):
    print(f"Running SAFE-PFL v{__version__} distance example")

    calculator = ModelDistancesCalculator(
        args.model_type,
        args.sensitivity_parameter,
        args.model_path_prefix,
        args.precision,
    )

    calculator.extract_model_weights()

    calculator.compute_distance_matrices()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate model distances.")

    parser.add_argument(
        "--model_type",
        type=str,
        choices=["cnn", "resnet", "google", "alexnet", "vgg"],
        default="cnn",
        help="Type of the model 'cnn', 'resnet', 'google', 'alexnet', or 'vgg'.",
    )
    parser.add_argument(
        "--sensitivity_parameter",
        type=float,
        default=0.1,
        help="Sensitivity parameter for distance calculation.",
    )
    parser.add_argument(
        "--model_path_prefix",
        type=str,
        default="./models",
        help="Model path.",
    )
    parser.add_argument(
        "--precision",
        type=int,
        default="5",
        help="Distance measurement precision.",
    )
    args = parser.parse_args()

    # Run example
    main(args)
