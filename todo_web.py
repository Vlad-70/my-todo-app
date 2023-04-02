import streamlit as st
import todo_functions as tf

todos = tf.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    tf.save_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my Todo App")                   # Subheader
st.write("This App to increase your productivity")    # Line of text

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        tf.save_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input("", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")

# pip freeze > requirements.txt   In terminal to create dependencies
