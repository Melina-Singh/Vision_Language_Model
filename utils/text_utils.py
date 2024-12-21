def format_caption(caption):
    """
    Format the caption text to make it more readable and grammatically correct.
    """
    # Remove leading and trailing whitespace
    caption = caption.strip()

    # Capitalize the first letter of the caption
    caption = caption.capitalize()

    # Ensure the caption ends with a period
    if not caption.endswith('.'):
        caption += '.'

    # Optionally, you can make the caption more human-readable
    # by replacing unnecessary words or patterns.
    # For example, if 'A' appears at the beginning and doesn't add value, remove it
    # Example: "A cat is sitting on the mat." -> "Cat is sitting on the mat."
    if caption.lower().startswith('a '):
        caption = caption[2:]

    return caption
