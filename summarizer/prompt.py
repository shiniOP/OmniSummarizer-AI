from langchain_core.prompts import PromptTemplate


def get_summary_prompt():
    """
    Returns the prompt template used for all AI tasks.
    """

    prompt = PromptTemplate(
        input_variables=[
            "task_instruction",
            "text",
            "summary_length",
            "summary_style",
        ],
        template="""
You are an expert AI assistant.

Follow the instruction below carefully.

Task:
{task_instruction}

Requirements:
- Summary Length: {summary_length}
- Output Style: {summary_style}
- Be accurate and concise.
- Do not include unnecessary information.
- Base your response only on the provided content.

Content:
{text}

Response:
"""
    )

    return prompt