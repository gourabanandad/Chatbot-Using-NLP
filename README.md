# Chatbot using NLP

## Overview
This repository contains a simple chatbot application that uses a JSON file for storing intents, example inputs, and responses. The chatbot is powered by natural language processing (NLP) techniques and a user-friendly Streamlit interface.

## Features
- **Text-Based Conversations**: Users can interact with the chatbot by typing messages.
- **Dynamic Chat History**: The application keeps a record of the conversation visible to the user.
- **Customizable Dataset**: Modify the JSON file to add or update intents, inputs, and responses.

## Prerequisites
- **Python Version**: Python 3.7 or higher
- **Required Libraries**:
  - `streamlit`
  - `scikit-learn`
  - `numpy`

Install the required libraries using the following command:
```bash
pip install streamlit scikit-learn numpy

.
├── app.py          # Main script for the chatbot
├── intent.json       # JSON file containing intents, texts, and responses
└── README.md               # Documentation

