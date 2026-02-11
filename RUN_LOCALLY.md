# How to Run Locally

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Set up Supabase Secrets:**
    -   Create a folder `.streamlit` in the root directory.
    -   Create a file `secrets.toml` inside `.streamlit`.
    -   Add your Supabase credentials:
        ```toml
        [secrets]
        SUPABASE_URL = "your-project-url"
        SUPABASE_KEY = "your-anon-key"
        ```

3.  **Run the App:**
    ```bash
    streamlit run app.py
    ```
