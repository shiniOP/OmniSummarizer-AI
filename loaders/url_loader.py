from urllib.parse import parse_qs, urlparse

import validators
from langchain_community.document_loaders import WebBaseLoader
from youtube_transcript_api import (
    YouTubeTranscriptApi,
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)


# Website

def extract_text_from_url(url: str) -> str:
    """
    Extract text from a website.
    """

    loader = WebBaseLoader(
        web_paths=(url,),
        header_template={
            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/138.0.0.0 Safari/537.36"
            )
        },
    )

    documents = loader.load()

    return "\n".join(
        doc.page_content
        for doc in documents
    )


# YouTube

def extract_video_id(url: str) -> str:
    """
    Extract the YouTube video ID.
    """

    parsed_url = urlparse(url)

    hostname = parsed_url.hostname or ""

    if hostname == "youtu.be":
        return parsed_url.path[1:]

    if hostname in (
        "youtube.com",
        "www.youtube.com",
        "m.youtube.com",
    ):

        if parsed_url.path == "/watch":
            return parse_qs(parsed_url.query)["v"][0]

        if parsed_url.path.startswith("/embed/"):
            return parsed_url.path.split("/")[2]

        if parsed_url.path.startswith("/shorts/"):
            return parsed_url.path.split("/")[2]

    raise ValueError("Invalid YouTube URL.")


def extract_youtube(url: str) -> str:
    """
    Extract transcript from a YouTube video.
    """

    video_id = extract_video_id(url)

    try:

        api = YouTubeTranscriptApi()

        transcript = api.fetch(video_id)

        return " ".join(
            snippet.text
            for snippet in transcript
        )

    except NoTranscriptFound:
        raise ValueError("No transcript found for this YouTube video.")

    except TranscriptsDisabled:
        raise ValueError("Transcripts are disabled for this YouTube video.")

    except VideoUnavailable:
        raise ValueError("This YouTube video is unavailable.")

    except Exception as e:
        raise ValueError(f"Failed to fetch transcript: {e}")


# Dispatcher

def extract_url_text(url: str) -> str:
    """
    Detect URL type and extract text.
    """

    if not validators.url(url):
        raise ValueError("Please enter a valid URL.")

    hostname = urlparse(url).hostname or ""

    if "youtube.com" in hostname or "youtu.be" in hostname:
        return extract_youtube(url)

    return extract_text_from_url(url)