import streamlit as st
import functions

names = functions.get_names()


def add_name():
    name = st.session_state["input_name"] +"\n"
    names.append(name)
    functions.write_names(names)


st.title("My NameList App")
st.subheader("This is my NameList App")
st.write("This app could help increasing your productivity")

for index, name in enumerate(names):
    checkbox= st.checkbox(name, key=name)
    if checkbox:
        names.pop(index)
        functions.write_names(names)
        del st.session_state[name]
        st.rerun()



st.text_input(label="", placeholder="Enter a name", key="input_name",
              on_change= add_name)
st.session_state