"""Page demonstrating direct usage of example_pkg."""

import streamlit as st

from example_pkg import Counter

st.header("Package Demo")
st.markdown("This page demonstrates direct usage of the `example_pkg.Counter` class.")

# Initialize session state for persistent counter
if "counter" not in st.session_state:
    st.session_state.counter = Counter()

# Display current value
st.metric("Current Value", st.session_state.counter.value)

# Controls
col1, col2, col3 = st.columns(3)

with col1:
    amount = st.number_input("Amount", min_value=1, value=1, key="amount")

with col2:
    if st.button("Increment", use_container_width=True):
        st.session_state.counter.increment(amount)
        st.rerun()

with col3:
    if st.button("Decrement", use_container_width=True):
        st.session_state.counter.decrement(amount)
        st.rerun()

# Reset button
if st.button("Reset Counter"):
    st.session_state.counter = Counter()
    st.rerun()
