Prompt-Engineering-Project
This assignment aimed to build a structured, measurable approach to prompt engineering using Jinja2 templates and Python. The primary task involved designing prompt variants to summarize customer complaints into clear, concise, and actionable outputs using a large language model (LLM).
I began by identifying a realistic and evaluable use case: customer service complaint summarization. This task was chosen because it reflects real-world business communication and allows for consistent quality assessment. Then defined what a “good output” should look like—accurate issue identification, clear structure, professional tone, and actionable insight.

Five distinct Jinja2-based prompt variants were created, each varying in tone, structure, and instruction style. These included instruction-first, role-based, format-constrained, friendly assistant, and urgency-emphasizing prompts. All variants were applied to the same dataset of five realistic complaints using a Python script that generated and logged outputs to CSV files.

An evaluation rubric was developed to assess outputs based on three main criteria: (1) accuracy or relevance, (2) structure and tone, and (3) task success or failure. After running the initial evaluation, Prompt 3 (format-based) emerged as the top performer due to its clarity and consistent output structure.

I refined Prompt 3 by adding a role-based context (“You are a complaint analysis assistant”) and slightly improving formatting and tone. The refined prompt was re-run on the same dataset, and results were stored separately to enable comparison.

The project concluded with a detailed comparison between the original and refined outputs, showing improved consistency and readability. A comprehensive summary, evaluation logs, rubric files, and source code were delivered as part of the final submission.

This project demonstrated how thoughtful prompt design, structured evaluation, and iterative refinement can significantly enhance LLM output quality in mission-critical scenarios.

