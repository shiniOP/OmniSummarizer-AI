##LCEL PIPELINE

from langchain_core.output_parsers import StrOutputParser

from summarizer.llm import get_llm
from summarizer.prompt import get_summary_prompt
from summarizer.tasks import get_task_instruction


#CREATE CHAIN
def get_summary_chain():
    """
    Creates and returns the AI response chain.
    """

    prompt = get_summary_prompt()
    llm = get_llm()
    parser = StrOutputParser()

    chain = prompt | llm | parser

    return chain


#GENERATE AI RESPONSE
def generate_ai_response(
    text: str,
    task: str,
    summary_length: str,
    summary_style: str,
) -> str:
    """
    Generates an AI response based on the selected task.
    """

    chain = get_summary_chain()

    task_instruction = get_task_instruction(task)

    response = chain.invoke(
        {
            "task_instruction": task_instruction,
            "text": text,
            "summary_length": summary_length,
            "summary_style": summary_style,
        }
    )

    return response