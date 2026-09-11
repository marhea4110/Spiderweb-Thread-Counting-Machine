import cv2


def display_result(image, thread_count, density_score, level):

    # Resize for easier display
    display_image = cv2.resize(
        image,
        (800, 600)
    )

    # Add information to the image
    cv2.putText(
        display_image,
        f"THREADS: {thread_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.putText(
        display_image,
        f"DENSITY: {density_score}%",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.putText(
        display_image,
        f"LEVEL: {level}",
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.imshow(
        "SPIDER COBWEB CERTIFIER",
        display_image
    )

    print("\n==============================")
    print("   SPIDER COBWEB CERTIFIER")
    print("==============================")
    print(f"Visible threads : {thread_count}")
    print(f"Density score   : {density_score}%")
    print(f"Cobweb level    : {level}")
    print("==============================")

    print("\nPress any key on the image window to close.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()