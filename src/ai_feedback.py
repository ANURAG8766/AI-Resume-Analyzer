from google import genai

def get_ai_feedback(resume_text, api_key):

    client = genai.Client(
        api_key=api_key
    )

    prompt = f"""
You are an ATS Resume Expert.

Analyze this resume and provide:

1. Strengths
2. Weaknesses
3. Missing Skills
4. Resume Improvement Suggestions
5. Career Advice

Resume:

{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text