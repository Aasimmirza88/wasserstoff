from transformers import pipeline

# Load a pre-trained summarization pipeline
summarizer = pipeline("summarization")

# Function to summarize object attributes
def summarize_attributes(texts):
    summaries = {}
    for object_id, text in texts.items():
        summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
        summaries[object_id] = summary[0]['summary_text']
    
    return summaries

# Example usage
summaries = summarize_attributes(texts)
