# Restaurant Recommendation Bot (FreeLance Project)

![Restaurant Recommendation Bot](restaurantbot.png)

## Overview

The Restaurant Recommendation Bot is a Streamlit-based web application designed to help users find restaurant recommendations based on their queries.

Utilizing advanced natural language processing techniques and a vector store powered by FAISS, the bot provides personalized and contextually relevant suggestions. The application leverages OpenAI embedding models to analyze user input and match it with a pre-built knowledge base of restaurant-related data.

---

## Features

* **Interactive Chat Interface**
  Users can interact with the bot through a chat interface to ask questions and receive restaurant recommendations.

* **Efficient Search**
  Uses FAISS with GPU support for fast and efficient similarity search within the vector store.

* **Persistent Vector Store**
  The vector store is created once and reused across sessions to ensure quick response times and efficient resource usage.

---

## Technologies Used

* Python
* Streamlit
* FAISS (GPU Support)
* OpenAI Embeddings
* LangChain

---

## Screenshot

The image below shows the Restaurant Recommendation Bot interface:

![Bot Screenshot](restaurantbot.png)


## Setup

### Prerequisites

- Python 3.7 or higher
- Streamlit
- FAISS
- OpenAI API key

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/restaurant-recommendation-bot.git
   cd restaurant-recommendation-bot
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Ensure the `requirements.txt` file includes the necessary libraries such as:

   ```plaintext
   streamlit
   faiss-cpu  # For CPU support
   faiss-gpu  # For GPU support, if needed
   openai
   langchain-community
   ```

4. **Set Up OpenAI API Key**

   - Replace `your-openai-api-key` with your actual OpenAI API key.
   - Update the `key` variable in the `app.py` file with your OpenAI API key.

5. **Run the Application**

   ```bash
   streamlit run app.py
   ```

   Open the provided URL in your browser to interact with the bot.

## Usage

- **Ask a Question**: Type your query into the chat input field to get restaurant recommendations.
- **Recommendations**: The bot will return suggestions based on the query and the pre-loaded data.

## File Structure

- `rag.py`: The main application file that defines the Streamlit app and handles user interactions.
- `requirements.txt`: Lists all the required Python packages.
- `vectorstore.pkl`: Stores the pre-built vector store (auto-generated and managed by the app).
- `combined_file.json`: JSON file containing the restaurant-related data.

## Deployment

To deploy the app to a cloud service like Streamlit Cloud:

1. **Create a Streamlit Cloud Account**: If you don't already have one, sign up at [Streamlit Cloud](https://streamlit.io/cloud).

2. **Deploy Your App**:
   - Go to the Streamlit Cloud dashboard.
   - Click on "New app" and connect your GitHub repository.
   - Follow the instructions to deploy the app.

3. **Update `.gitignore`**:
   - Ensure the `.gitignore` file includes `venv/` to avoid uploading the virtual environment to GitHub.

## Contributing

Feel free to fork the repository and make improvements. Contributions are welcome!
