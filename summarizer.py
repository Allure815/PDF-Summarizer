class TextSummarizer:
    """
    Dummy summarizer for testing without Transformers
    """

    def __init__(self):
        pass  # no model loading, works locally

    def summarize_chunk(self, text: str) -> str:
        # Return first 2 sentences as "summary"
        sentences = text.split(". ")
        summary = ". ".join(sentences[:2])
        if not summary.endswith("."):
            summary += "."
        return summary
