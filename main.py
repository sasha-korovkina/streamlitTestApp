import streamlit as st


def main():
    st.title('Simple Streamlit App')

    # Display a text input field
    user_input = st.text_input('Enter your name', '')

    # Display a greeting message based on user input
    if user_input:
        st.write(f'Hello, {user_input}! Welcome to Streamlit.')


if __name__ == "__main__":
    main()
