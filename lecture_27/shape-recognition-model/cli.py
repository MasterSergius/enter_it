import argparse
import os


from model import ShapeRecognitionModel
from trainer import ShapeTrainer
from data import DataManager

DEFAULT_WEIGHTS = "weights.txt"
DEFAULT_DATA_DIR = "training_data"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Shape Recognition Demo")

    sub = parser.add_subparsers(dest="command", required=True)

    train_cmd = sub.add_parser("train", help="Train the model and save weights")
    train_cmd.add_argument(
        "--retrain",
        action="store_true",
        help="Train from scratch even if a weights file already exists",
    )
    train_cmd.add_argument(
        "--data",
        default=DEFAULT_DATA_DIR,
        metavar="DIR",
        help=f"Directory with training data (default: {DEFAULT_DATA_DIR})",
    )

    classify_cmd = sub.add_parser("classify", help="Classify a shape bitmap")
    classify_cmd.add_argument(
        "--input",
        default="shape.txt",
        metavar="FILE",
        help="Bitmap .txt file to classify (default: shape.txt)",
    )
    classify_cmd.add_argument(
        "--weights",
        default=DEFAULT_WEIGHTS,
        metavar="FILE",
        help=f"Weights file to load (default: {DEFAULT_WEIGHTS})",
    )

    return parser.parse_args()


def train_model(retrain: bool, data_dir: str) -> ShapeRecognitionModel:
    """Train from scratch and save weights, or skip if weights already exist."""
    if not retrain and os.path.exists(DEFAULT_WEIGHTS):
        print(f"Weights '{DEFAULT_WEIGHTS}' already exist. Use --retrain to overwrite.")
        return ShapeRecognitionModel.load(DEFAULT_WEIGHTS)

    model = ShapeRecognitionModel(
        input_size=64, hidden_size=8, labels=DataManager.LABELS
    )
    training_data = DataManager().get_training_data(data_dir)

    print("Training …")
    ShapeTrainer(learning_rate=0.01).train(model, training_data, epochs=1000)
    model.save(DEFAULT_WEIGHTS)
    print(f"Weights saved to '{DEFAULT_WEIGHTS}'.\n")
    return model


def load_model(weights_file: str) -> ShapeRecognitionModel | None:
    """Load weights from disk, or print an error and return None."""
    if not os.path.exists(weights_file):
        print(f"Weights file '{weights_file}' not found. Run 'train' first.")
        return None
    print(f"Loading weights from '{weights_file}' …")
    return ShapeRecognitionModel.load(weights_file)


def classify(model: ShapeRecognitionModel, input_file: str) -> None:
    """Load a bitmap file, print it, and print the model's prediction."""
    if not os.path.exists(input_file):
        print(f"Input file '{input_file}' not found.")
        print("Create an 8×8 text file using '*' and '.' to draw a shape.")
        return

    bitmap = DataManager.load_bitmap(input_file)
    print(f"Input '{input_file}':")
    print(DataManager.render(bitmap))
    print()
    print(f"Prediction: {model.predict(bitmap)}")


def run_command(args) -> None:
    if args.command == "train":
        train_model(args.retrain, args.data)

    elif args.command == "classify":
        model = load_model(args.weights)
        if model:
            classify(model, args.input)
