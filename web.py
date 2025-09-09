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

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.divider()
st.text_input(label='', placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')
