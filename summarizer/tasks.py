def get_task_instruction(task: str) -> str:
    """
    Returns the instruction for the selected AI task.
    """

    tasks = {

        "Summary":
        """
        Summarize the content while preserving the key ideas and important details.
        """,

        "Executive Summary":
        """
        Create a professional executive summary highlighting the objective,
        major findings, important insights, and conclusion.
        """,

        "Bullet Points":
        """
        Summarize the content into clear and concise bullet points.
        """,

        "Key Takeaways":
        """
        Extract the five to ten most important takeaways from the content.
        """,

        "Explain Like I'm 5":
        """
        Explain the content using very simple language that a beginner or
        a 10-year-old can easily understand.
        """,

        
        "Keywords":
     
        """
        Extract the 10 to 20 most important keywords and key phrases from the content.

        Return them as a bullet list.

        Do not include explanations.
        """,

        "Question & Answer":
        """
        Generate important questions along with their answers based on the content.
        """,

        "Mermaid Mind Map":
        """
        Generate a Mermaid mind map representing the main concepts and their
        relationships.

        Return ONLY valid Mermaid code.

        Example:

        mindmap
          root((Topic))
            Concept 1
              Detail A
              Detail B
            Concept 2
              Detail C
        """,
    }

    return tasks.get(
        task,
        tasks["Summary"],
    )