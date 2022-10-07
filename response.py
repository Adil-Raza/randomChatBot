def sample_response(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello"):
        return "hi"

    if user_message in ("panda", "anupam"):
        return "Panda bhsdka"

    return f"{input_text} gandhu hai"

    return "unable to precess"
