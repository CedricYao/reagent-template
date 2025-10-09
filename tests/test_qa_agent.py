
import unittest
from unittest.mock import patch, MagicMock
import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from agents_gallery.qa_agent.agent import analyze_bug, qa_agent

class TestQaAgent(unittest.TestCase):

    @patch("google.generativeai.GenerativeModel")
    def test_analyze_bug_unit(self, MockGenerativeModel):
        """Unit test for the analyze_bug tool with mock data."""
        # Arrange
        mock_model_instance = MockGenerativeModel.return_value
        mock_response = MagicMock()
        mock_response.text = '{"verdict": "Valid", "justification": "The bug is valid.", "evidence": "Evidence text."}'
        mock_model_instance.generate_content.return_value = mock_response

        prd_content = "The system shall do X."
        bug_report = "The system does Y instead of X."

        # Act
        result = analyze_bug(prd_content, bug_report)

        # Assert
        self.assertEqual(result["verdict"], "Valid")
        self.assertEqual(result["justification"], "The bug is valid.")
        self.assertEqual(result["evidence"], "Evidence text.")

    def test_qa_agent_integration(self):
        """Integration test for the qa_agent."""
        # Arrange
        async def run_test():
            session_service = InMemorySessionService()
            runner = Runner(
                agent=qa_agent,
                app_name="qa_agent_test",
                session_service=session_service,
            )
            session = await session_service.create_session(app_name="qa_agent_test", user_id="test_user")

            prd_content = "Feature: User login. The user should be able to log in with their email and password."
            bug_report = "Bug: User cannot log in with a valid email and password. The error message is \"Invalid credentials\"."
            
            prompt = f"""Here is the PRD content:\n{prd_content}\n\nHere is the bug report:\n{bug_report}"""

            # Act
            events = runner.run_async(user_id="test_user", session_id=session.id, new_message=types.Content(parts=[types.Part(text=prompt)]))
            
            final_response = None
            async for event in events:
                if event.is_final_response():
                    final_response = event.content.parts[0].text
                    break
            
            # Assert
            self.assertIsNotNone(final_response)
            self.assertIn("verdict", final_response.lower())
            self.assertIn("justification", final_response.lower())

        # Run the async test
        asyncio.run(run_test())

if __name__ == "__main__":
    unittest.main()
