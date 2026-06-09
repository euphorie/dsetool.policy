def set_language(context, request):
    """Switches Plone over to the language of the context, without requiring a new HTTP
    request.
    """
    language = getattr(context, "language", "en")
    request["LANGUAGE"] = language
    binding = request.get("LANGUAGE_TOOL", None)
    if binding is not None:
        binding.LANGUAGE = language
