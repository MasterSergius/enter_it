import math
import random

from data import DataManager


class ShapeRecognitionModel:
    """
    Two-layer fully-connected neural network, pure Python.

    Forward pass:
        hidden[j]  = sigmoid( W1[j] · x  + b1[j] )
        output[k]  = softmax( W2[k] · h  + b2[k] )

    Shapes:
        W1 : hidden_size  × input_size
        W2 : output_size  × hidden_size
    """

    def __init__(self, input_size: int, hidden_size: int, labels: list):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.labels = labels
        self.output_size = len(labels)

        # Xavier uniform initialisation: keeps activations from vanishing/exploding
        # at the start of training.  Scale = sqrt(1 / fan_in).
        s1 = math.sqrt(1.0 / input_size)
        s2 = math.sqrt(1.0 / hidden_size)

        self.W1 = [
            [random.uniform(-s1, s1) for _ in range(input_size)]
            for _ in range(hidden_size)
        ]
        self.b1 = [0.0] * hidden_size

        self.W2 = [
            [random.uniform(-s2, s2) for _ in range(hidden_size)]
            for _ in range(self.output_size)
        ]
        self.b2 = [0.0] * self.output_size

        # These are populated by forward() and consumed by the trainer's backward().
        self._cache_x = None  # raw input
        self._cache_hidden = None  # post-sigmoid hidden activations
        self._cache_probs = None  # post-softmax output probabilities

    # ── Activation functions ──────────────────────────────────────────────────

    @staticmethod
    def _sigmoid(x: float) -> float:
        # Clamp prevents math.exp overflow for very large negative/positive inputs.
        x = max(-500.0, min(500.0, x))
        return 1.0 / (1.0 + math.exp(-x))

    @staticmethod
    def _softmax(values: list) -> list:
        # Subtract max for numerical stability (the result is identical).
        m = max(values)
        exps = [math.exp(v - m) for v in values]
        total = sum(exps)
        return [e / total for e in exps]

    # ── Forward pass ──────────────────────────────────────────────────────────

    def forward(self, x: list) -> list:
        """
        Run a single sample through the network.
        Caches intermediate values so the trainer can run backprop immediately
        after calling this method.

        Returns: list of output_size probabilities (sum to 1.0).
        """
        # Hidden layer: net = W1 · x + b1, then sigmoid
        hidden = []
        for j in range(self.hidden_size):
            net = sum(self.W1[j][i] * x[i] for i in range(self.input_size)) + self.b1[j]
            hidden.append(self._sigmoid(net))

        # Output layer: net = W2 · hidden + b2, then softmax
        raw_output = []
        for k in range(self.output_size):
            net = (
                sum(self.W2[k][j] * hidden[j] for j in range(self.hidden_size))
                + self.b2[k]
            )
            raw_output.append(net)

        probs = self._softmax(raw_output)

        self._cache_x = x
        self._cache_hidden = hidden
        self._cache_probs = probs
        return probs

    def render_probs(self, probs):
        """Convert fraction to human-readable percent"""
        return [
            f"{shape}: {percent}%"
            for shape, percent in zip(
                DataManager.LABELS, map(lambda x: round(x * 100), probs)
            )
        ]

    def predict(self, x: list) -> str:
        """Return the class label with the highest probability."""
        probs = self.forward(x)
        print(f"Prediction scores: {self.render_probs(probs)}")
        return self.labels[probs.index(max(probs))]

    # ── Persistence ───────────────────────────────────────────────────────────

    def save(self, filepath: str) -> None:
        """Write all weights to a plain-text file."""
        with open(filepath, "w") as f:
            f.write(" ".join(self.labels) + "\n")
            f.write(f"{self.input_size} {self.hidden_size} {self.output_size}\n")
            for row in self.W1:
                f.write(" ".join(map(str, row)) + "\n")
            f.write(" ".join(map(str, self.b1)) + "\n")
            for row in self.W2:
                f.write(" ".join(map(str, row)) + "\n")
            f.write(" ".join(map(str, self.b2)) + "\n")

    @classmethod
    def load(cls, filepath: str) -> "ShapeRecognitionModel":
        """Restore a model from a previously saved weights file."""
        with open(filepath) as f:
            lines = [l.strip() for l in f if l.strip()]

        idx = 0
        labels = lines[idx].split()
        idx += 1
        input_size, hidden_size, output_size = map(int, lines[idx].split())
        idx += 1

        model = cls(input_size, hidden_size, labels)

        model.W1 = []
        for _ in range(hidden_size):
            model.W1.append(list(map(float, lines[idx].split())))
            idx += 1
        model.b1 = list(map(float, lines[idx].split()))
        idx += 1

        model.W2 = []
        for _ in range(output_size):
            model.W2.append(list(map(float, lines[idx].split())))
            idx += 1
        model.b2 = list(map(float, lines[idx].split()))

        return model
