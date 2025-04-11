import matplotlib.pyplot as plt
import numpy as np
import pytest
from sklearn.datasets import load_digits

from optical_toolkit.visualize.visualize_images import plot_images, summarize_images


@pytest.fixture
def sample_images():
    return [np.random.rand(100, 100, 3) for _ in range(10)]


@pytest.fixture
def sample_targets():
    return [f"Class_{i % 3}" for i in range(10)]


@pytest.fixture
def digits_data():
    digits = load_digits()
    images = digits.images
    targets = digits.target
    return images, targets


def test_plot_images_basic(sample_images):
    output_path = "examples/visualizations/test_images.png"
    plot_images(sample_images, cols=5, output_path=output_path)


def test_plot_images_with_targets(sample_images, sample_targets):
    output_path = "examples/visualizations/test_images_with_targets.png"
    plot_images(
        sample_images,
        cols=5,
        targets=sample_targets,
        ordered_plot=True,
        output_path=output_path,
    )


def test_plot_images_empty_images():
    with pytest.raises(ValueError, match="The images list cannot be empty."):
        plot_images([], cols=5)


def test_plot_images_with_sklearn_digits(digits_data):
    images, targets = digits_data
    images = [images[i] for i in range(10)]
    targets = targets[:10]
    output_path = "examples/visualizations/test_sklearn_digits.png"
    plot_images(
        images, cols=5, targets=targets, ordered_plot=True, output_path=output_path
    )


def test_summarize_images(digits_data):
    images, targets = digits_data
    output_path = "examples/visualizations/test_summarize_images.png"
    summarize_images(
        images,
        targets,
        num_images_per_class=10,
        num_classes=10,
        output_path=output_path,
    )

    rows = cols = math.ceil(math.sqrt(len(manifold_types)))
    fig, axes = plt.subplots(rows, cols, figsize=(4 * cols, 4 * rows))

    axes = axes.flatten()

    for i, embedding_type in enumerate(manifold_types):
        _, fig_3d = get_embeddings(
            X, y, embedding_dims=3, embedding_type=embedding_type, return_plot=True
        )

        fig_3d.canvas.draw()
        axes[i].imshow(fig_3d.canvas.buffer_rgba())
        axes[i].set_title(f"{embedding_type.value} (3D)")
        axes[i].axis("off")
        fig_3d.savefig(
            f"examples/embeddings/3d_{embedding_type.name}_embedding.png", dpi=300
        )

    for j in range(i + 1, len(axes)):  # Hide extra subplots
        axes[j].axis("off")

    fig.tight_layout()
    fig.savefig("examples/3d_embedding_comparison.png", dpi=300)
    plt.show()
