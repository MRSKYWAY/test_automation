from test_case_generator import generate_test_cases ,generate_test_cases_with_gemini
from html_retriever import login_and_get_html

def main():
    platform_url = 'https://www.saucedemo.com/'  # Update with the actual URL
    username = "standard_user"
    password = "secret_sauce"
     
    print(f"Please log in to {platform_url} and then press Enter to continue...")
    input()  # Wait for the user to log in

    # After user logs in, get HTML source
    html_source = login_and_get_html(platform_url, username, password)

    # Save the HTML source to a file for verification
    with open('extracted_html_source.html', 'w', encoding='utf-8') as f:
        f.write(html_source)

    # AI generates test cases from HTML source
    test_cases = generate_test_cases_with_gemini(html_source)
    
    # # Execute the generated test cases
    # results = execute_test_cases()
    
    # # Log results
    # log_results(results)

if __name__ == "__main__":
    main()
