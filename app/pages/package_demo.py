"""Page demonstrating direct usage of example_pkg."""

import streamlit as st

from example_pkg import Counter

st.header("Package Demo")
st.caption("Direct usage of the `example_pkg.Counter` class")

if "counter" not in st.session_state:
    st.session_state.counter = Counter()

st.subheader(f"Counter: {st.session_state.counter.value}")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Decrement", icon="⬇️", width="stretch"):
        st.session_state.counter.decrement()
        st.rerun()
with col2:
    if st.button("Reset", icon="🔄", width="stretch"):
        st.session_state.counter = Counter()
        st.rerun()
with col3:
    if st.button("Increment", icon="⬆️", width="stretch"):
        st.session_state.counter.increment()
        st.rerun()
