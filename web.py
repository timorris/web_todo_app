import streamlit as st
import functions as functions

# Inject custom CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("site.css")

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state['new_todo']
    st.session_state['new_todo'] = ''
    todos.append(new_todo + '\n')
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write('<span class="blurb">This app is to increase your&#160;'
         '<strong style="font-size:1.2em;"><em>productivity</em></strong> (hopefully).</span>',
         unsafe_allow_html=True)

st.divider()

for index in range(len(todos)):
    if f"edit_mode_{index}" not in st.session_state:
        st.session_state[f"edit_mode_{index}"] = False

for index, todo in enumerate(todos):
    if st.session_state.get(f"edit_mode_{index}"):
        # Edit mode: show text input and Save button
        edited_todo_text = st.text_input(
            "Edit",
            value=todo.strip(),
            key=f"edit_input_{index}"
        )
        if st.button("Save", key=f"save_button_{index}"):
            todos[index] = edited_todo_text + '\n'
            functions.write_todos(todos)
            st.session_state[f"edit_mode_{index}"] = False
            st.rerun()
    else:
        # View mode: show checkbox, todo text, and Edit button
        col1, col2 = st.columns([0.9, 0.1])
        with col1:
            checkbox = st.checkbox(todo.strip(), key=f"todo_{index}")
            if checkbox:
                todos.pop(index)
                functions.write_todos(todos)
                # Reset all edit modes to avoid incorrect state after deletion
                for i in range(len(todos) + 1):
                    if f"edit_mode_{i}" in st.session_state:
                        st.session_state[f"edit_mode_{i}"] = False
                    if f"todo_{i}" in st.session_state:
                        del st.session_state[f"todo_{i}"]
                st.rerun()
        with col2:
            if st.button("Edit", key=f"edit_button_{index}"):
                st.session_state[f"edit_mode_{index}"] = True
                st.rerun()

st.divider()
st.text_input(label='', placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')
