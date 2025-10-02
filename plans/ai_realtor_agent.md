# Feature Implementation Plan: AI Realtor Agent

## 📋 Todo Checklist
- [ ] Set up project structure and initial files.
- [ ] Create and populate the property catalog data store.
- [ ] Implement the `search_properties` tool.
- [ ] Implement the `request_viewing` tool.
- [ ] Define the main ADK agent.
- [ ] Create a test runner to verify the agent's functionality.
- [ ] Final Review and Testing.

## 🔍 Analysis & Investigation

### Codebase Structure
The current codebase is empty. The plan will be to create a new directory `ai_realtor_agent` which will contain all the agent's code, tools, and data.

### Current Architecture
The architecture will be based on the Google Agent Development Kit (ADK) for Python. The agent will use a Gemini model for natural language understanding and will interact with local data stores via custom tools.

### Dependencies & Integration Points
- **Google Agent Development Kit (ADK):** The core framework for building the agent.
- **google-genai:** The Python library for interacting with the Gemini API.
- **Local Data Files:** The agent will read from a `properties.json` file and write to a `leads.json` file.
- **pytest:** For testing the tools and agent functionality.
- **Default Gemini Model:** `gemini-2.5-flash` for any gemini model.

### Considerations & Challenges
- **Data Management:** The local data stores will need to be managed carefully. For a production system, a more robust database solution would be required.
- **Error Handling:** The tools should include robust error handling to manage cases where properties are not found or lead capture fails.
- **Security:** The agent will be collecting user contact information, so it's important to handle this data securely, even in a local context.

## 📝 Implementation Plan

### Prerequisites
- Python 3.9+ venv environment set up.
- `pip` for package management.
- `google-adk` and `google-genai` libraries installed.
- A configured Google Cloud Project with the Vertex AI API enabled.
- Authentication configured (ADC or API key).

### Step-by-Step Implementation
1. **Step 1: Set up Project Structure**
   - Files to modify: Create the following directory and files:
     ```
     agents_gallery/
     └──ai_realtor_agent/
         ├── __init__.py
         ├── agent.py
         ├── tools.py
         └── data/
               ├── properties.json
               └── leads.json
     ```

2. **Step 2: Create and Populate Data Stores**
   - Files to modify: `ai_realtor_agent/data/properties.json`
   - Changes needed: Populate the `properties.json` file with a list of property objects. Each object should contain fields like `id`, `address`, `zip_code`, `price`, `bedrooms`, and `image_url`.
   - Files to modify: `ai_realtor_agent/data/leads.json`
   - Changes needed: Initialize `leads.json` as an empty list `[]`.

3. **Step 3: Implement the `search_properties` tool**
   - Files to modify: `ai_realtor_agent/tools.py`
   - Changes needed: Implement the `search_properties(zip_code: str, max_price: int)` function. This function will:
     - Load the `properties.json` file.
     - Filter the properties based on the `max_price` but allow matching on any zipcode.
     - Return a list of matching property objects.

4. **Step 4: Implement the `request_viewing` tool**
   - Files to modify: `ai_realtor_agent/tools.py`
   - Changes needed: Implement the `request_viewing(property_id: str, requested_time: str, user_name: str, user_contact: str)` function. This function will:
     - Load the `leads.json` file.
     - Append a new lead object with the provided details.
     - Save the updated list back to `leads.json`.
     - Return a confirmation message.

5. **Step 5: Define the Main ADK Agent**
   - Files to modify: `ai_realtor_agent/agent.py`
   - Changes needed:
     - Import the `search_properties` and `request_viewing` tools.
     - Create an `LlmAgent` instance.
     - Provide a detailed `instruction` prompt that guides the agent on how to use the tools to showcase properties and capture leads.
     - Add the tools to the agent's `tools` list.

6. **Step 6: Create a Test Runner**
   - Files to modify: `test_agent.py` (at the root level)
   - Changes needed: Create a simple test runner script that:
     - Initializes the `InMemorySessionService` and `Runner`.
     - Creates a session.
     - Sends a series of test prompts to the agent to simulate the conversation flow described in the design document.
     - Prints the agent's responses to the console.

### Testing Strategy
- **Unit Tests:** Create unit tests for the `search_properties` and `request_viewing` tools to ensure they function correctly.
- **Integration Test:** Use the `test_agent.py` script to perform an end-to-end test of the agent's conversational flow.
- **Manual Testing:** Use the `adk web` command to interact with the agent in a web UI for manual testing.

## 🎯 Success Criteria
- The agent can successfully find and display properties from the `properties.json` file based on user criteria.
- The agent can successfully capture viewing requests and save them to the `leads.json` file.
- The agent's conversational flow matches the sample conversation in the design document.
