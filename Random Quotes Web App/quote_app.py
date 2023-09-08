import streamlit as st
import requests
import time
from bs4 import BeautifulSoup
import random

st.markdown(
    """
    <style>
    /* Style the quote container */
    .quote-container {
        background-color: #f4f4f4;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.5);
    }

    /* Style the quote text */
    .quote-text {
        font-size: 24px;
        font-style: italic;
        text-align: center;
    }

    /* Style the quote author */
    .quote-author {
        margin-top: 10px;
        font-size: 18px;
        text-align: right;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define the URL of the website with quotes
quote_url = "https://quotes.toscrape.com/"  # Updated URL

# Function to scrape a random quote from the website
def get_random_quote():
    response = requests.get(quote_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # Extract quotes and authors
        quotes = soup.select("span.text")
        authors = soup.select("small.author")
        
        if quotes and authors:
            # Select a random index to get a random quote
            index = random.randint(0, len(quotes) - 1)
            quote = quotes[index].get_text()
            author = authors[index].get_text()
            return f'"{quote}" - {author}'
    return "Failed to fetch a quote."

# Main Streamlit app
def main():
    st.title("Quote App")
    st.write("Random quotes refreshed every 10 minutes.")

    # Get an initial random quote
    current_quote = get_random_quote()
    st.write("**Quote:**")
    # Stylish quote container
    st.markdown('<div class="quote-container">', unsafe_allow_html=True)
    st.markdown('<p class="quote-text">{}</p>'.format(current_quote), unsafe_allow_html=True)
    st.markdown('<div class="quote-container">', unsafe_allow_html=True)


    ## About ME:
    st.header("About ME:")
    st.write("Hi there, I'm Saadat Khalid Awan 👋")
    st.write("`Aspiring Data Scientist | Problem Solver | Lifelong Learner`")
    st.write("I'm a software engineer with a keen interest in data science. I hold a BS degree in Software Engineering and am currently learning about the field of data science.")

    st.write("Submission Date: September 8, 2023")

    # Social Media Links
    st.header("Let's Connect:")
    st.markdown(
        "[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?logo=Facebook&logoColor=white)](https://facebook.com/Saadat.Khalid.Awan) "
        "[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/saadii_awan66) "
        "[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/saadatawan) "
        "[![Medium](https://img.shields.io/badge/Medium-12100E?logo=medium&logoColor=white)](https://medium.com/@@me.saadat) "
        "[![Pinterest](https://img.shields.io/badge/Pinterest-%23E60023.svg?logo=Pinterest&logoColor=white)](https://pinterest.com/its_saadatkhalid) "
        "[![Quora](https://img.shields.io/badge/Quora-%23B92B27.svg?logo=Quora&logoColor=white)](https://quora.com/profile/Saadat-Khalid-Awan) "
        "[![TikTok](https://img.shields.io/badge/TikTok-%23000000.svg?logo=TikTok&logoColor=white)](https://tiktok.com/@@saadat.awan) "
        "[![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?logo=Twitter&logoColor=white)](https://twitter.com/saadat_96) "
        "[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?logo=YouTube&logoColor=white)](https://youtube.com/@saadatkhalidawan) "
        "[![Github](https://img.shields.io/badge/Github-%23FF0000.svg?logo=Github&logoColor=Black)](https://github.com/Saadat-Khalid/)"
    )

    # Set a timer to refresh the quote every 10 minutes
    while True:
        time.sleep(600)  # 600 seconds = 10 minutes
        current_quote = get_random_quote()
        st.write("**New Quote:**")
        st.write(current_quote)


if __name__ == "__main__":
    main()

