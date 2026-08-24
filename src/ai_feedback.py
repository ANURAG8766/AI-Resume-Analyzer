from google import genai

def get_ai_feedback(resume_text, api_key):

    client = genai.Client(api_key=api_key)

    prompt = f"""
Analyze this resume and provide:
1. Strengths
2. Weaknesses
3. Missing Skills
4. Resume Improvement Suggestions
5. Career Advice

Resume:
{resume_text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"Gemini Error: {str(e)}"