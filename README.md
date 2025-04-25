---
title: Web Research Agent
emoji: 🔍
sdk: gradio
sdk_version: 5.26.0
app_file: app.py
pinned: false
---

# Web Research Agent

This project is a Web Research Agent that searches the web for information based on a user's query, extracts relevant data, and presents it in an organized format.

## Features

- Performs web searches using Google Custom Search API.
- Extracts titles, snippets, and URLs from the search results.
- Displays the extracted information in a user-friendly format.
- Allows users to ask any research query and receive summarized results.

## Tools Used

- **Gradio** for the user interface.
- **Google Custom Search API** for web searching.
- **BeautifulSoup** for scraping HTML content.

## Requirements

To run this project, you need to have the following Python packages installed:

- gradio
- google-api-python-client
- requests
- beautifulsoup4

You can install these packages using:

```bash
pip install -r requirements.txt

Demo

You can try out the Web Research Agent live on Hugging Face:

[Web Research Agent Demo](https://huggingface.co/spaces/sneha0428/web-research-agent/tree/main)


Loom Walkthrough
[Loom video walkthrough](https://www.loom.com/share/a7433eff65474808a43ee3c352361367?sid=7f3cf793-986b-45b5-986d-9d5c4242e53d)