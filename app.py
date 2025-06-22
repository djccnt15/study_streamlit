from pathlib import Path

import streamlit as st

page_path = Path("src") / "domain"
auth_path = page_path / "auth"

index_page = st.Page(page_path / "index.py", title="Home")
auth_page_1 = st.Page(page=auth_path / "auth_1.py", title="Auth 1")
auth_page_2 = st.Page(page=auth_path / "auth_2.py", title="Auth 2")

pg = st.navigation(
    {
        "Home": [index_page],
        "Auth": [auth_page_1, auth_page_2],
    }
)

if __name__ == "__main__":
    pg.run()
