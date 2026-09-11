def calculate_density(thread_count, image_width, image_height):
    """
    Estimate cobweb density from detected thread count.

    The score is normalized so that it stays between 0 and 100.
    """

    image_area = image_width * image_height

    if image_area <= 0:
        return 0

    # Adjustable formula for the demo
    raw_score = (thread_count / image_area) * 100000

    density_score = min(100, max(0, raw_score))

    return round(density_score, 2)


def get_density_level(score):

    if score < 20:
        return "LOW"

    elif score < 40:
        return "MODERATE"

    elif score < 60:
        return "HIGH"

    elif score < 80:
        return "VERY HIGH"

    else:
        return "LEGENDARY"