import google.generativeai as genai

def generate_test_cases_with_gemini(html_source, output_file="testcases.py", api_key="AIzaSyBd07VXAwN22NwaVCGlqFzEcqkQOdBkKEk"):
    if not api_key:
        raise ValueError("❌ Gemini API key is required. Pass it as 'api_key'.")

    # Configure Gemini API
    genai.configure(api_key=api_key)

    # Initialize model 
    model = genai.GenerativeModel("gemini-2.0-flash")

    # Define prompt
    prompt = (
        "You are an expert QA engineer. I will give you a block of HTML, and you must return "
        "only the Selenium test code in Python for testing the UI functionality covered in that HTML. "
        "Do not include any explanation, introduction, or additional text—just the code block. "
        "Focus on writing functional test cases that simulate realistic user interactions like clicking buttons, "
        "filling out forms, and asserting visible text or results.\n\n"
        f"HTML:\n'''\n{html_source}\n'''\n\n"
        "Output only the Python Selenium test code inside one code block, starting with ```python and ending with ```."
    )

    try:
        response = model.generate_content(prompt)
        content = response.text.strip()
    except Exception as e:
        print(f"❌ Error calling Gemini API: {e}")
        return None

    # Strip ```python ... ``` if present
    if "```python" in content:
        content = content.split("```python")[1]
    if "```" in content:
        content = content.split("```")[0]
    content = content.strip()

    # Write to file
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Selenium test cases saved to {output_file}")
    except Exception as e:
        print(f"❌ Failed to save test cases: {e}")
        return None

    return output_file

