"""Main Streamlit application entrypoint."""

import streamlit as st

st.set_page_config(page_title="py-fullstack-template", page_icon="🚀")

pg = st.navigation(
    [
        st.Page("pages/package_demo.py", title="Package Demo", icon="📦"),
        st.Page("pages/api_client.py", title="API Client", icon="🌐"),
    ],
    position="top",
)

st.title("py-fullstack-template")
pg.run()
