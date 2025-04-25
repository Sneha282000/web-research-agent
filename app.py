import gradio as gr
from googleapiclient.discovery import build

# Google Custom Search credentials
api_key = "AIzaSyCnrkc1Ri6WWji_zVZDainxBbRZfv1TYck"  # Replace with your API key
cse_id = "106709730045649a5"    # Replace with your Custom Search Engine ID

# Function to perform search using Google Custom Search API
def google_search(query):
    try:
        service = build("customsearch", "v1", developerKey=api_key)  # Setup Google Custom Search API
        res = service.cse().list(q=query, cx=cse_id).execute()  # Perform search

        # Check if results are returned
        if "items" in res:
            results = [{"title": item["title"], "snippet": item["snippet"], "url": item["link"]} for item in res["items"][:3]]
            return "\n\n".join([f"**{r['title']}**\n{r['snippet']}\n🔗 [Link]({r['url']})" for r in results])
        else:
            return "No results found or blocked by Google."
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio Web Interface
demo = gr.Interface(
    fn=google_search,  # The function that will be called when the user submits a query
    inputs=gr.Textbox(lines=2, placeholder="Enter your research query..."),  # Input box for queries
    outputs=gr.Markdown(), # Text output will display the search results
    title="Web Research Agent",  # Title of the app
    description="Ask any research question. The agent will search and summarize the answer.",  # Description of the app
)

demo.launch()
