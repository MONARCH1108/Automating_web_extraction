import os
import subprocess

def chatbot():
    print("\n[MonarchAI] Welcome to the High-Profile Scrapy Crawler Bot!")
    print("\nI am here to help you extract valuable data from the web. Let's get started!\n")

    # List of spiders and their respective details
    spiders = {
        "books_data": {
            "url": "https://books.toscrape.com/",
            "description": "Extracting book titles, prices, availability, and ratings."
        },
        "country_data": {
            "url": "https://www.scrapethissite.com/pages/simple/",
            "description": "Extracting country names, population, and area details."
        },
        "news_spider": {
            "url": "https://finance.yahoo.com/",
            "description": "Extracting financial news headlines and summaries."
        }
    }

    while True:
        # Get the website link from the user
        print("\n[MonarchAI] Please provide the website link you want to scrape (or type 'exit' to quit):")
        website_link = input("You: ").strip()
        if website_link.lower() == 'exit':
            print("\n[MonarchAI] Goodbye! Have a productive day ahead.")
            break

        # Match the link to a spider
        matched_spider = None
        for spider, details in spiders.items():
            if website_link.lower() == details["url"].lower():
                matched_spider = (spider, details)
                break

        if not matched_spider:
            print("\n[MonarchAI] I couldn't find a matching spider for that link. Please check the URL and try again.")
            continue

        spider_name, spider_details = matched_spider
        print(f"\n[MonarchAI] Matched spider: {spider_name}")
        print(f"[MonarchAI] This spider specializes in: {spider_details['description']}")

        # Ask for the output format
        print("\n[MonarchAI] How would you like the extracted data to be saved?")
        print("1. JSON file\n2. CSV file\n3. Text file\n4. Display in CMD prompt")
        output_choice = input("You: ").strip()

        output_command = ""
        if output_choice == "1":
            output_file = input("[MonarchAI] Enter the name for the JSON file (e.g., output.json): ").strip()
            output_command = f" -o {output_file}"
        elif output_choice == "2":
            output_file = input("[MonarchAI] Enter the name for the CSV file (e.g., output.csv): ").strip()
            output_command = f" -o {output_file}"
        elif output_choice == "3":
            output_file = input("[MonarchAI] Enter the name for the Text file (e.g., output.txt): ").strip()
            output_command = f" -o {output_file}"
        elif output_choice == "4":
            print("[MonarchAI] Data will be displayed in the CMD prompt.")
        else:
            print("\n[MonarchAI] Invalid choice. Please try again.")
            continue

        # Navigate to the correct directory
        try:
            os.chdir("structured_data/structured_data/spiders")
        except FileNotFoundError:
            print("\n[MonarchAI] Error: The directory 'structured_data/spiders' does not exist. Please check your setup.")
            return

        # Execute the Scrapy command
        command = f"scrapy crawl {spider_name}{output_command}"
        print(f"\n[MonarchAI] Executing: {command}")

        try:
            subprocess.run(command, shell=True, check=True)
            print("\n[MonarchAI] Scraping completed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"\n[MonarchAI] Error occurred while running the spider: {e}")
        finally:
            # Return to the original directory
            os.chdir("../../..")

if __name__ == "__main__":
    chatbot()
