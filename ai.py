from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_report(statistics):

    prompt = f"""
You are a Senior Business Intelligence Analyst.

Analyze the following dataset statistics and produce an Executive Report.

Dataset Statistics:

{statistics}

Return the report using this structure:

1. Executive Summary

2. Business Insights

3. Risks

4. Opportunities

5. Recommendations
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a professional business analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content