import math
import random


class ShapeTrainer:
    """
    Trains a ShapeRecognitionModel with stochastic gradient descent (SGD)
    and cross-entropy loss.  No external libraries required.
    """

    def __init__(self, learning_rate: float = 0.01):
        self.learning_rate = learning_rate

    # ── Loss ──────────────────────────────────────────────────────────────────

    @staticmethod
    def _cross_entropy(probs: list, target: int) -> float:
        """
        Cross-entropy loss for a single sample.
        L = -log( p[target] )
        Clamp avoids log(0).
        """
        return -math.log(max(probs[target], 1e-15))

    # ── Backward pass ─────────────────────────────────────────────────────────

    def _backward(self, model, target: int) -> None:
        """
        Compute gradients via backpropagation and update weights in-place.

        The model must have just run forward() so its cache is populated.

        Gradient derivations
        --------------------
        Softmax + cross-entropy together give a clean gradient:

            dL/d(raw_output[k]) = prob[k] - 1  if k == target
                                = prob[k]       otherwise

        Backprop through W2 / b2:

            dL/dW2[k][j] = d_out[k] * hidden[j]
            dL/db2[k]    = d_out[k]

        Backprop into hidden layer, then through sigmoid:

            dL/dhidden[j]  = sum_k( d_out[k] * W2[k][j] )
            dL/dnet_h[j]   = dL/dhidden[j] * sigmoid'(net_h[j])
                           = dL/dhidden[j] * h[j] * (1 - h[j])

        Backprop through W1 / b1:

            dL/dW1[j][i] = dL/dnet_h[j] * x[i]
            dL/db1[j]    = dL/dnet_h[j]
        """
        probs  = model._cache_probs
        hidden = model._cache_hidden
        x      = model._cache_x
        lr     = self.learning_rate

        # ── Output layer gradients ────────────────────────────────────────────
        d_out = list(probs)           # copy of probabilities
        d_out[target] -= 1.0         # subtract 1 for the true class

        for k in range(model.output_size):
            for j in range(model.hidden_size):
                model.W2[k][j] -= lr * d_out[k] * hidden[j]
            model.b2[k] -= lr * d_out[k]

        # ── Hidden layer gradients ────────────────────────────────────────────
        d_hidden = [
            sum(d_out[k] * model.W2[k][j] for k in range(model.output_size))
            for j in range(model.hidden_size)
        ]

        # Sigmoid derivative: h * (1 - h)
        d_net_h = [d_hidden[j] * hidden[j] * (1.0 - hidden[j])
                   for j in range(model.hidden_size)]

        for j in range(model.hidden_size):
            for i in range(model.input_size):
                model.W1[j][i] -= lr * d_net_h[j] * x[i]
            model.b1[j] -= lr * d_net_h[j]

    # ── Evaluation ────────────────────────────────────────────────────────────

    @staticmethod
    def _print_final_evaluation(model, data: list) -> None:
        """Print a per-sample prediction table after training completes."""
        print("\n  Final evaluation:")
        headers = " / ".join(f"{l[:3]}" for l in model.labels)
        print(f"  {'#':<4} {'actual':<10} {'predicted':<10} {'confidence':>10}   scores ({headers})")
        print("  " + "-" * 70)

        correct = 0
        for i, (x, label) in enumerate(data):
            probs     = model.forward(x)
            predicted = probs.index(max(probs))
            ok        = predicted == label
            if ok:
                correct += 1
            scores = " / ".join(f"{p * 100:5.1f}%" for p in probs)
            mark   = "OK  " if ok else "FAIL"
            print(
                f"  {i+1:<4} {model.labels[label]:<10} {model.labels[predicted]:<10}"
                f" {probs[predicted]*100:>9.1f}%   [{scores}]  {mark}"
            )

        print("  " + "-" * 70)
        print(f"  Total: {correct}/{len(data)} correct ({correct/len(data)*100:.1f}%)\n")

    # ── Training loop ─────────────────────────────────────────────────────────

    def train(self, model, training_data: list, epochs: int) -> None:
        """
        Train for a fixed number of epochs.

        training_data — list of (bitmap: list[float], label: int) tuples.
        label is an integer index into ShapeRecognitionModel.LABELS.

        Samples are shuffled each epoch so the network doesn't learn the
        order of the data instead of its content.
        """
        data = list(training_data)   # local copy we can shuffle freely

        n_classes = model.output_size

        for epoch in range(epochs):
            random.shuffle(data)

            total_loss     = 0.0
            class_correct  = [0] * n_classes
            class_total    = [0] * n_classes

            for x, label in data:
                probs = model.forward(x)
                total_loss += self._cross_entropy(probs, label)
                if probs.index(max(probs)) == label:
                    class_correct[label] += 1
                class_total[label] += 1
                self._backward(model, label)

            if (epoch + 1) % 100 == 0:
                n        = len(data)
                avg_loss = total_loss / n
                overall  = sum(class_correct) / n * 100.0
                per_class = "  ".join(
                    f"{model.labels[k]}: {class_correct[k]}/{class_total[k]}"
                    for k in range(n_classes)
                )
                print(f"  epoch {epoch+1:4d} | loss {avg_loss:.4f} | acc {overall:5.1f}%  ({per_class})")

        self._print_final_evaluation(model, data)
