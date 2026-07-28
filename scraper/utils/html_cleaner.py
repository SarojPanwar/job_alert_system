import html
from bs4 import BeautifulSoup
import re

def clean_html(content):
    """
    Convert encoded HTML into clean plain text.
    """

    if not content:
        return ""

    # Convert &lt;p&gt; into <p>
    decoded_html = html.unescape(content)

    # Parse HTML
    soup = BeautifulSoup(decoded_html, "html.parser")

    # Extract readable text
    clean_text = soup.get_text(separator="\n", strip=True)

    # Replace non-breaking spaces
    text = clean_text.replace("\xa0", " ")

    # Remove multiple blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # Remove multiple spaces
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()
    