import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent

load_dotenv()

# The instruction now contains the logic that was previously in the tool.
# The agent will expect the PRD and bug report to be part of the user's prompt.
qa_agent_instruction = """
You are a QA agent. Your task is to analyze a bug report against a PRD and determine if the bug is valid.
The user will provide both the PRD and the bug report in their message.

Analyze the following bug report against the provided Product Requirements Document (PRD).
Determine if the bug is a valid deviation from the PRD.

Based on your analysis, provide a JSON object with the following fields:
- "verdict": (string) "Valid" or "Invalid".
- "justification": (string) A detailed explanation for your verdict.
- "evidence": (string) Specific quotes or sections from the PRD and bug report that support your justification.
"""

root_agent = LlmAgent(
    name="qa_agent",
    model="gemini-2.5-flash",
    description="A QA agent that analyzes bug reports against a PRD.",
    instruction=qa_agent_instruction,
    # The tools list is now empty as the agent handles the logic directly.
    tools=[],
)