import streamlit as st
import controller.controller as control


def display():
    if control.is_admin(st.session_state["id_user"]):
        st.title("Page admin du site")

    else:
        st.write("Vous n'êtes pas un adminisatrateur")


if __name__ == "__main__":
    display()
