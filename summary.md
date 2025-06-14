Summary: Prompt Engineering Assignment

Task Overview
This project focuses on summarizing customer complaints into short, clear, and actionable summaries using large language model prompt engineering. The aim is to develop multiple structured prompt variants, evaluate their output performance, and refine the best-performing one to improve consistency and clarity.

Use Case and Evaluation Dataset
We selected the use case of customer service complaint summarization because:
- It has clear real-world applications.
- It enables measurable quality assessment (via accuracy, tone, and actionability).
The dataset includes 5 realistic complaint inputs.

What Defines a “Good Output”?
A successful summary should:
1. Accurately identify the core issue raised by the customer.
2. Follow a consistent and readable structure (ideally including both issue and recommended action).
3. Maintain a neutral, professional tone appropriate for internal business communication.
4. Be concise (1–2 sentences) but not vague.

Prompt Design
Five prompt variants were created in Jinja2:
- Prompt 1: Instruction-first
- Prompt 2: Role-based
- Prompt 3: Format-constrained (Issue/Action format)
- Prompt 4: Friendly assistant tone
- Prompt 5: Emphasizing urgency

Each variant used the same set of test inputs and was scored using a rubric with the following criteria:
- Accuracy/Relevance
- Structure/Tone
- Task Success/Failure
  
Top-Performing Prompt: Prompt 3
Prompt 3 used a format-constrained structure:
Extract the issue and suggested action in this format:
Issue: <...>
Action: <...>
Complaint: {{ complaint }}

This version outperformed others by:
- Providing a consistent structure.
- Guiding the model to include actionable output.
- Producing readable summaries even for vague or emotional complaints.

Refinement and Re-Evaluation
Prompt 3 was refined by:
- Adding a role-based header: “You are a complaint analysis assistant...”
- Slightly softening the tone for better internal readability.

Refined version outputs were re-run and compared. Results showed:
- Increased clarity and tone consistency.
- More clearly delineated “Issue” and “Action” fields.

Final Takeaways
- Prompt structure significantly influences output quality.
- Adding format guidance and soft role instructions improves LLM reliability.
- Iterative evaluation (manual or LLM-assisted) helps tune prompt performance for mission-critical applications.
