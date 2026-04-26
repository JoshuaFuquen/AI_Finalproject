# AI Text Classification using xAI Grok LLM
# This project uses an LLM (Large Language Model) as the "brain" to classify reviews
# The LLM analyzes sentiment based on training data patterns

import os
import json
from typing import List, Dict

# ============================================================================
# STEP 1: Setup and Configuration
# ============================================================================

# Import the xAI API client
try:
    import requests
except ImportError:
    print("Error: 'requests' library not found. Install it with: pip install requests")
    exit(1)

# Load API key from environment variable
API_KEY = os.getenv('XAI_API_KEY')

if not API_KEY:
    print("ERROR: XAI_API_KEY environment variable not set!")
    print("Please set your API key: export XAI_API_KEY='your-api-key-here'")
    exit(1)

# xAI API configuration
XAI_API_URL = "https://api.x.ai/v1/chat/completions"
MODEL_NAME = "grok-beta"

# ============================================================================
# STEP 2: Training Dataset
# ============================================================================

# Training examples with labels (used to teach the LLM the classification task)
training_data = [
    {"text": "This product is amazing! I love it so much.", "sentiment": "positive"},
    {"text": "Terrible quality, very disappointed.", "sentiment": "negative"},
    {"text": "Great value for the money, highly recommend.", "sentiment": "positive"},
    {"text": "Waste of money, does not work as described.", "sentiment": "negative"},
    {"text": "Excellent service and fast delivery!", "sentiment": "positive"},
    {"text": "Very poor, broke after one day.", "sentiment": "negative"},
    {"text": "Best purchase ever, could not be happier!", "sentiment": "positive"},
    {"text": "Not worth the price, very disappointed.", "sentiment": "negative"},
    {"text": "Fantastic quality, exceeded expectations.", "sentiment": "positive"},
    {"text": "Horrible experience, will not buy again.", "sentiment": "negative"},
    {"text": "Perfect! Exactly what I needed.", "sentiment": "positive"},
    {"text": "Bad quality, money wasted.", "sentiment": "negative"},
    {"text": "Love this product, works perfectly!", "sentiment": "positive"},
    {"text": "Completely useless, total waste.", "sentiment": "negative"},
    {"text": "Outstanding product, very satisfied.", "sentiment": "positive"},
    {"text": "Poor quality, very unhappy with purchase.", "sentiment": "negative"},
    {"text": "Wonderful! Would definitely recommend.", "sentiment": "positive"},
    {"text": "Awful product, complete disappointment.", "sentiment": "negative"},
    {"text": "Amazing quality and great customer service!", "sentiment": "positive"},
    {"text": "Not satisfied, looking for refund.", "sentiment": "negative"},
]

print("=" * 70)
print("AI TEXT CLASSIFICATION USING xAI GROK LLM")
print("=" * 70)
print(f"\nTraining dataset loaded: {len(training_data)} examples")
print()

# ============================================================================
# STEP 3: Create a prompt with training examples for the LLM
# ============================================================================

def create_system_prompt() -> str:
    """
    Creates a system prompt that teaches the LLM how to classify sentiment
    by providing examples from the training data
    """
    
    # Build the training examples into the system prompt
    examples_text = ""
    for example in training_data:
        examples_text += f'- "{example["text"]}" → {example["sentiment"]}\n'
    
    system_prompt = f"""You are an expert sentiment classifier. Your task is to classify 
short text reviews as either "positive" or "negative".

TRAINING EXAMPLES:
{examples_text}

CLASSIFICATION RULES:
- Positive: The text expresses satisfaction, joy, recommendation, or approval
- Negative: The text expresses dissatisfaction, disappointment, complaint, or disapproval

IMPORTANT: 
- Respond with ONLY the word "positive" or "negative"
- Do not add explanations
- Do not add punctuation
- Just the classification label"""
    
    return system_prompt

# ============================================================================
# STEP 4: Function to call xAI Grok API
# ============================================================================

def classify_with_llm(text: str, system_prompt: str) -> str:
    """
    Sends a request to xAI Grok API to classify the sentiment of the given text
    
    Args:
        text: The review text to classify
        system_prompt: The system prompt with training examples
        
    Returns:
        The classification: "positive" or "negative"
    """
    
    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": MODEL_NAME,
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": f"Classify this review: {text}"
                }
            ],
            "temperature": 0,  # Temperature 0 for consistent predictions
            "max_tokens": 10   # We only need one word response
        }
        
        response = requests.post(XAI_API_URL, headers=headers, json=payload)
        
        if response.status_code != 200:
            print(f"API Error: {response.status_code}")
            print(f"Response: {response.text}")
            return "error"
        
        # Extract the classification from the response
        result = response.json()
        classification = result["choices"][0]["message"]["content"].strip().lower()
        
        return classification
        
    except Exception as e:
        print(f"Error calling API: {e}")
        return "error"

# ============================================================================
# STEP 5: Prepare new test reviews
# ============================================================================

# 5 new example reviews to classify
test_reviews = [
    "This is the best thing I ever bought!",
    "Complete garbage, do not buy.",
    "Pretty good product for the price.",
    "Worst purchase of my life, totally useless.",
    "I am very happy with this product!"
]

print("-" * 70)
print("CLASSIFYING NEW REVIEWS WITH xAI GROK LLM")
print("-" * 70)
print()

# ============================================================================
# STEP 6: Classify new reviews using the LLM
# ============================================================================

# Create the system prompt with training data
system_prompt = create_system_prompt()

# Classify each test review
predictions = []

for i, review in enumerate(test_reviews, 1):
    print(f"Review {i}: \"{review}\"")
    
    # Get classification from LLM
    prediction = classify_with_llm(review, system_prompt)
    predictions.append(prediction)
    
    # Display result
    if prediction == "positive":
        sentiment = "✓ POSITIVE"
    elif prediction == "negative":
        sentiment = "✗ NEGATIVE"
    else:
        sentiment = "ERROR"
    
    print(f"Predicted Sentiment: {sentiment}")
    print()

# ============================================================================
# STEP 7: Summary
# ============================================================================

print("=" * 70)
print("CLASSIFICATION COMPLETE")
print("=" * 70)
print(f"\nTotal reviews classified: {len(test_reviews)}")
print(f"Results: {predictions}")
print("\nThe LLM analyzed the reviews using the training patterns learned from")
print("the training data and classified each review as positive or negative.")
