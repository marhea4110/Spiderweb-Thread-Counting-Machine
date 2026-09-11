import cv2


def detect_web_threads(image_path):
    """
    Detect visible cobweb lines using OpenCV Hough Line Transform.

    Returns:
        processed_image: image with detected lines drawn
        thread_count: estimated number of visible line segments
    """

    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Could not open image: {image_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges
    edges = cv2.Canny(blurred, 50, 150)

    # Detect straight/approximately straight web segments
    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=3.14159 / 180,
        threshold=30,
        minLineLength=20,
        maxLineGap=10
    )

    thread_count = 0
    processed_image = image.copy()

    if lines is not None:

        for line in lines:
            x1, y1, x2, y2 = line[0]

            # Calculate length of detected line
            length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

            # Ignore extremely small lines
            if length >= 20:
                thread_count += 1

                cv2.line(
                    processed_image,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

    return processed_image, thread_count