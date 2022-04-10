import sys
import requests


def get_page(get_url):
    """
    downloads the page specified with get_url string to index.html

    parameters:
    get_url: an url in the format of https://example.com/page1
    """

    # get_url = "https://plato.stanford.edu/cgi-bin/encyclopedia/random"

    # header to authenticate myself as user
    headers = requests.utils.default_headers()

    headers.update(
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "Referer": "https://www.google.com/",
        }
    )

    page = requests.get(get_url, headers=headers)
    print("requested URL")

    original_stdout = sys.stdout
    with open("newindex.html", "w", encoding="utf-8") as file:
        sys.stdout = file  # Change the standard output to the file we created.
        print(page.text)
        sys.stdout = original_stdout
        print("updated index.html")

    # print(page.text)

get_page("https://plato.stanford.edu/cgi-bin/encyclopedia/random")

# common user agents
# https://www.networkinghowtos.com/howto/common-user-agent-list/
