from summarizer.chain import get_summary_chain

chain = get_summary_chain()

response = chain.invoke(
    {
        "text": """
Artificial Intelligence (AI) is transforming industries across the world.
It enables machines to perform tasks that typically require human intelligence,
such as problem-solving, decision-making, and language understanding.
AI is widely used in healthcare, finance, education, and autonomous vehicles.
""",
        "summary_length": "Short",
        "summary_style": "Paragraph",
    }
)

print(response)