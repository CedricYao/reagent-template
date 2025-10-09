# Feature Implementation Plan: Text Input QA Agent

## 📋 Todo Checklist
- [x] ~~Create the project structure for the QA agent.~~ ✅ Implemented
- [x] ~~Implement the `analyze_bug` tool.~~ ✅ Implemented
- [x] ~~Implement the QA Agent.~~ ✅ Implemented
- [x] ~~Implement unit and integration tests.~~ ✅ Implemented
- [x] ~~Final Review and Testing~~ ✅ Implemented

## 🔍 Analysis & Investigation

### Codebase Structure
The current codebase is a Python project using the Google Agent Development Kit (ADK). The project structure is minimal, containing only the basic ADK project files. I will create a new directory `agents_gallery/qa_agent` for the new agent, following the standard Python package structure.

### Current Architecture
The architecture will be based on the Google ADK framework. I will create an `LlmAgent` and a custom `FunctionTool`. The agent will be stateless in this initial version.

### Dependencies & Integration Points
The primary dependency will be the `google-adk` library. The agent will not have any external integration points in this version.

### Considerations & Challenges
- The quality of the analysis will heavily depend on the prompt used in the `analyze_bug` tool. The prompt needs to be carefully crafted to ensure the LLM provides accurate and structured responses.
- The agent's performance will be tied to the performance of the underlying LLM.

## 📝 Implementation Plan

### Prerequisites
- A working Python environment with `pip` installed.
- Access to an LLM (e.g., Gemini).

### Step-by-Step Implementation
1. **Step 1: Create Project Structure**
   - Files to create:
     - `agents_gallery/qa_agent/__init__.py`
     - `agents_gallery/qa_agent/agent.py`
     - `tests/__init__.py`
     - `tests/test_qa_agent.py`
     - `requirements.txt`
     - `README.md`
   - Changes needed: Create the directories and empty files.

2. **Step 2: Implement the `analyze_bug` Tool**
   - Files to modify: `agents_gallery/qa_agent/agent.py`
   - Changes needed:
     - Implement the `analyze_bug(prd_content: str, bug_report: str) -> dict` function.
     - Inside the function, create a detailed prompt that instructs `gemini-2.5-pro` using VertexAI and the `google-genai` library to compare the `prd_content` and `bug_report` and return a JSON object with the `verdict`, `justification`, and `evidence`.
     - The environment variables for `google-genai` library will be loaded from `.env` file and a template are in the `.env.copy` file.
     - Use the `google.adk.tools.FunctionTool` to wrap the `analyze_bug` function.

3. **Step 3: Implement the QA Agent**
   - Files to modify: `agents_gallery/qa_agent/agent.py`
   - Changes needed:
     - Create an `LlmAgent` instance named `qa_agent`.
     - Set the `name`, `description`, and `instruction` as specified in the design document.
     - Assign the `analyze_bug` tool to the agent's `tools` list.

4. **Step 4: Implement Tests**
   - Files to modify: `tests/test_qa_agent.py`
   - Changes needed:
     - Write a unit test for the `analyze_bug` tool with mock PRD and bug report content.
     - Write an integration test for the `qa_agent`. This test will use the `google.adk.runners.Runner` to execute the agent with sample inputs and verify the output.

5. **Step 5: Create `requirements.txt` and `README.md`**
   - Files to modify: `requirements.txt`, `README.md`
   - Changes needed:
     - Add `google-adk` to `requirements.txt`.
     - Write a `README.md` file explaining the agent's purpose, how to install dependencies (`pip install -r requirements.txt`), and how to run the tests (`pytest`).

### Testing Strategy
- **Unit Tests**: Test the `analyze_bug` tool in isolation to ensure it correctly calls the LLM and parses the response.
- **Integration Tests**: Test the end-to-end flow of the `qa_agent` to verify that it correctly uses the tool and returns the expected output format.

## 🎯 Success Criteria
- The `qa_agent` can be successfully invoked with a PRD and a bug report.
- The agent returns a valid JSON object with the `verdict`, `justification`, and `evidence` fields.
- All unit and integration tests pass.
