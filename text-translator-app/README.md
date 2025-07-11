# 📝 Text Translator App  🖥️

This is a simple and powerful Streamlit app that uses OpenAI's language model and LangChan to translate text to language in specific ton.

## 🚀 Features

- ✂️ Translate text to language in specific ton
- 🔐 Secure API key handling using `python-dotenv`
- 📱 User-friendly web interface built with Streamlit

## 📦 Requirements

Install the dependencies listed in `requirements.txt`:

```commandline
pip install -r requirements.txt
```

## 🛠 Setup

1. **Clone the repository** (if applicable):

    ```
    git clone https://github.com/nextwebspark/llm-blogs.git
    cd llm-blogs/text-summarizer-app
    ```

   2. **Create a `.env` file** in the root directory with your OpenAI API key:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_API_MODEL=gpt-4o-mini
   ```

3. **Run the app**:

    ```
    streamlit run app.py
    ```
## 🛡️ Security Note

Do **not** share your `.env` file or API key publicly. Always add `.env` to your `.gitignore` if pushing to a remote repository.

## 📃 License

This project is licensed under the MIT License.

---

Enjoy translator smarter, not harder! ✨