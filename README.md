# AI Final Project - Text Classification

**Team Members:**
- Joshua Fuquen
- Chris Tham
- Annie Wang

## 📋 Project Description

This project implements two different approaches for text sentiment classification:

1. **Traditional Machine Learning Approach** (scikit-learn)
2. **Large Language Model Approach** (xAI Grok)

Both approaches classify short text reviews as positive or negative sentiment.

### 🎯 Project Goals

- Demonstrate understanding of machine learning concepts
- Compare traditional ML vs. LLM approaches
- Implement complete, runnable Python projects
- Document the development process and results

## 📁 Project Structure

```
AI_Finalproject/
├── codigo/                    # 📁 Code folder
│   ├── main.py               # Scikit-learn classifier
│   └── requirements.txt      # Dependencies for ML approach
├── main.py                   # xAI Grok LLM classifier
├── requirements.txt          # Dependencies for LLM approach
├── API_KEY_SETUP.txt         # Instructions for xAI API setup
├── .gitignore               # Git ignore file (protects credentials)
├── AI_final_Excel.xlsx      # 📊 Excel spreadsheet for analysis
├── AI_Report_finalproject.pdf # 📄 Final project report
└── README.md                # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Git
- xAI API key (for LLM version)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JoshuaFuquen/AI_Finalproject.git
   cd AI_Finalproject
   ```

2. **Install dependencies for both approaches:**

   **For scikit-learn version:**
   ```bash
   cd codigo
   pip install -r requirements.txt
   ```

   **For xAI LLM version:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Classifiers

#### Traditional ML Approach (Scikit-learn)
```bash
cd codigo
python main.py
```

#### LLM Approach (xAI Grok)
```bash
# First, set up your xAI API key (see API_KEY_SETUP.txt)
export XAI_API_KEY='your-api-key-here'
python main.py
```

## 🧠 Implementation Details

### Scikit-learn Approach
- Uses `TfidfVectorizer` for text preprocessing
- `LogisticRegression` for classification
- 80/20 train-test split
- Includes 20 training examples

### xAI Grok LLM Approach
- Uses xAI's Grok model via API
- Few-shot learning with training examples in prompt
- Temperature set to 0 for consistent results
- Classifies new reviews based on learned patterns

## 📊 Dataset

Both approaches use the same dataset of 20 short text reviews with binary sentiment labels (positive/negative).

**Sample reviews:**
- "This product is amazing! I love it so much." → positive
- "Terrible quality, very disappointed." → negative
- "Great value for the money, highly recommend." → positive

## 🔐 Security & API Keys

**IMPORTANT:** Never commit API keys to version control!

- Use `.env` files for local development
- The `.gitignore` file protects sensitive files
- Follow the instructions in `API_KEY_SETUP.txt` for xAI API setup

## 📈 Results & Evaluation

Both models are evaluated on:
- Test accuracy
- Predictions on 5 new example reviews
- Qualitative analysis of classification performance

## 🛠️ Technologies Used

- **Python 3.8+**
- **Scikit-learn** (traditional ML)
- **xAI Grok API** (LLM approach)
- **Requests** (HTTP client for API calls)
- **Git** (version control)

## 📝 Project Requirements Met

✅ Complete runnable Python project
✅ Uses appropriate ML libraries
✅ Includes dataset and preprocessing
✅ Implements training and evaluation
✅ Provides clear documentation
✅ Follows security best practices

## 🤝 Contributing

This is a final project submission. For questions or feedback, please contact the team members.

## 📄 License

This project is for educational purposes as part of an AI course final project.

---

**Course:** AI 100 Final Project
**Date:** April 2026
**Team:** Joshua Fuquen, Chris Tham, Annie Wang
