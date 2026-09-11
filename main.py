import cv2

from web_counter import detect_web_threads
from density import calculate_density, get_density_level
from certificate import generate_certificate
from display import display_result


IMAGE_PATH = "images/test_web.jpg"


def main():

    print("==============================")
    print("   SPIDER COBWEB CERTIFIER")
    print("==============================")

    print("\nAnalyzing cobweb...")

    # Detect threads
    processed_image, thread_count = detect_web_threads(
        IMAGE_PATH
    )

    # Get image dimensions
    height, width = processed_image.shape[:2]

    # Calculate density
    density_score = calculate_density(
        thread_count,
        width,
        height
    )

    # Determine level
    level = get_density_level(
        density_score
    )

    # Generate certificate
    certificate_path = generate_certificate(
        thread_count,
        density_score,
        level
    )

    print("\nAnalysis complete!")

    print(f"Threads detected : {thread_count}")
    print(f"Density score    : {density_score}%")
    print(f"Level            : {level}")
    print(f"Certificate      : {certificate_path}")

    # Display results
    display_result(
        processed_image,
        thread_count,
        density_score,
        level
    )


if __name__ == "__main__":
    main()