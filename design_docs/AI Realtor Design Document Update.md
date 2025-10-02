## **Design Document: Realtor's AI Assistant**

### **1\. Overview**

The **Realtor's AI Assistant** is a conversational agent designed to showcase a realtor's property portfolio and capture customer interest. As a standalone application, it operates without real-time external integrations, making it a robust tool for initial lead qualification.

Built on the **Google Agent Development Kit (ADK)**, the agent will leverage Google's **Gemini** models for advanced natural language understanding. All property and scheduling information is managed within the agent's local data store. The agent also uses **Vertex AI** for an innovative virtual staging feature, helping customers visualize a property's potential.

The primary goal is to provide an engaging, interactive property showcase that effectively captures user preferences and contact information for follow-up by a human realtor.

---

### **2\. Core Features & Functionality**

* **Feature 1: Curated Property Showcase**  
  * **Description:** Users can naturally ask the agent to find homes from a **pre-loaded catalog** based on criteria like **zip code** and **price point**. The agent searches its internal static database and presents the matching properties.  
  * **Example Interaction:** "Show me houses in 80301 for under $900,000."  
* **Feature 2: Viewing Request Collector**  
  * **Description:** When a user expresses interest in a property, the agent collects their preferred viewing times and contact information. Instead of booking directly, it logs this information and informs the user that a realtor will contact them to confirm the appointment. This transforms the agent into a powerful lead-generation tool.  
  * **Example Interaction:** "I'd like to see the house at 123 Pine St. Can I look at it Saturday morning?"

---

### **3\. Technical Architecture**

The system is designed around the Google ADK, which orchestrates interactions between the user, the Gemini LLM, and various local tools.
* **Use `pip` to install and manage dependencies within a `requirements.txt` file** 
* **To Reference Vertex AI and Gemini, create a env.copy file with the following content: Prompt the user for the correct project ID and location**
  ```
  GGOOGLE_GENAI_USE_VERTEXAI=TRUE
  GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID
  GOOGLE_CLOUD_LOCATION=LOCATION
  ```
* **Agent Core (Google Agent Development Kit for Python):** The central application logic built using the ADK framework. It manages the conversation state and dispatches tasks to the appropriate tools.  
* **LLM Engine (Google Gemini API):** The agent will use a Gemini model accessed via the **`google-genai` Python library**. The LLM's role is to interpret user requests and determine which tool to call with the correct parameters.  
* **Python testing (pytest):** Use the `pytest` library to create a suite of unit and integration tests to ensure the agent and its tools function as expected.
* **Internal Data Store:**  
  * **Property Catalog:** A local JSON file or an in-memory database containing a curated list of property objects (e.g., address, price, bedrooms, image URL, property ID). This is the single source of truth for the property showcase.  
  * **Lead Capture Log:** A simple database or CSV file where viewing requests (property ID, user name, contact info, requested time) are logged for realtor follow-up.  
* **Tools (ADK Tools):** These are self-contained Python functions that the LLM can invoke.  
  1. search\_properties(zip\_code: str, max\_price: int) \-\> list:  
     * Queries the **internal Property Catalog**.  
     * Filters properties based on zip\_code and max\_price.  
     * Returns a list of matching property objects.  
  2. request\_viewing(property\_id: str, requested\_time: str, user\_name: str, user\_contact: str) \-\> dict:  
     * Validates the user's input.  
     * Appends the request details to the **Lead Capture Log**.  
     * Returns a confirmation message stating that a realtor will be in touch.

---

### **4\. Sample Conversation Flow**

1. **User (Initiation):** "Hi, I'm looking for a house."  
2. **Agent (Greeting & Clarification):** "Hello\! I can show you some of our featured properties. To start, what zip code are you interested in?"  
3. **User:** "I'm looking in 80301."  
4. **Agent (Further Clarification):** "Great. And do you have a maximum price point in mind?"  
5. **User:** "Yes, let's keep it under $950,000."  
6. **Agent (Tool Call: search\_properties):** "Okay, looking through our catalog for homes in 80301 under $950,000... I've found three properties. \[Presents a summary list from the local data\]."  
7. **User:** "Tell me more about the one on Spruce Street."  
8. **Agent (Information Retrieval):** "The property at 456 Spruce St is listed for $925,000. It has 3 bedrooms, 2 bathrooms, and a newly renovated kitchen. Would you like to request a time to see it?"  
9. **User:** "Yes, please. How about Saturday at 11 AM?"  
10. **Agent (Tool Call: request\_viewing):** "Perfect. To submit your request, I'll just need your name and phone number."  
11. **User:** "My name is Alex and my number is 555-123-4567."  
12. **Agent (Confirmation):** "Thank you, Alex. I've logged your request to view 456 Spruce St on Saturday at 11 AM. **A realtor will contact you at 555-123-4567 to confirm the details.**"

---

### **5\. Assumptions & Dependencies**

* **Google Cloud Project:** A configured Google Cloud Project is required with the Vertex AI API enabled to use the Gemini and Imagen models.  
* **Authentication:** Application Default Credentials (ADC) or an API key must be configured for the google-generativeai library to authenticate with Google Cloud.  
* **Curated Dataset:** The project requires a well-structured, pre-populated dataset (e.g., a JSON file) of properties for the agent to showcase.