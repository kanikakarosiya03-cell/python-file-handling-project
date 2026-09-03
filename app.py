from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="File Handler",
    page_icon="📁",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.stApp {
    background-color: #0b0f14;
    color: #ffffff;
}

section[data-testid="stSidebar"] {
    background-color: #11161d;
    border-right: 1px solid #29313d;
}

.main-title {
    font-size: 42px;
    font-weight: 700;
    color: #ffffff !important;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 16px;
    color: #d5d9df !important;
    margin-bottom: 25px;
}

.section-title {
    font-size: 25px;
    font-weight: 600;
    color: #ffffff !important;
    margin-top: 10px;
    margin-bottom: 18px;
}

.description {
    font-size: 15px;
    color: #d5d9df !important;
    margin-bottom: 20px;
}

.card {
    background-color: #151b23;
    border: 1px solid #35404d;
    border-radius: 14px;
    padding: 24px;
    margin-bottom: 20px;
}

.file-card {
    background-color: #1a212b;
    border: 1px solid #35404d;
    border-radius: 10px;
    padding: 12px;
    margin-bottom: 9px;
    color: #ffffff !important;
}

.file-card b {
    color: #ffffff !important;
}

.sidebar-title {
    font-size: 23px;
    font-weight: 700;
    color: #ffffff !important;
    margin-bottom: 5px;
}

.sidebar-text {
    font-size: 14px;
    color: #cbd2da !important;
    margin-bottom: 20px;
}

.stTextInput label,
.stTextArea label,
.stSelectbox label,
.stRadio label,
.stCheckbox label {
    color: #ffffff !important;
}

.stTextInput input,
.stTextArea textarea {
    background-color: #1b222c !important;
    color: #ffffff !important;
    border: 1px solid #46515f !important;
    border-radius: 9px !important;
    caret-color: #ffffff !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #aeb7c2 !important;
}

.stTextArea textarea:disabled {
    background-color: #1b222c !important;
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    opacity: 1 !important;
}

div[data-baseweb="select"] > div {
    background-color: #1b222c !important;
    border: 1px solid #46515f !important;
    color: #ffffff !important;
}

div[data-baseweb="select"] span {
    color: #ffffff !important;
}

ul[data-baseweb="menu"] {
    background-color: #1b222c !important;
}

ul[data-baseweb="menu"] li {
    color: #ffffff !important;
}

ul[data-baseweb="menu"] li:hover {
    background-color: #3a424d !important;
    color: #ffffff !important;
}

.stButton > button {
    width: 100%;
    background-color: #d9dee4 !important;
    color: #10151b !important;
    border: 1px solid #d9dee4 !important;
    border-radius: 9px;
    padding: 10px 18px;
    font-weight: 600;
    font-size: 15px;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background-color: #ffffff !important;
    color: #000000 !important;
    border-color: #ffffff !important;
}

.operation-card {
    background-color: #171e27;
    border: 1px solid #3b4653;
    border-radius: 10px;
    padding: 10px;
    min-height: 64px;
    text-align: center;
    transition: all 0.2s ease;
}

.operation-card:hover {
    background-color: #3b424c;
    border-color: #858e99;
    transform: translateY(-2px);
}

.operation-card.active {
    background-color: #3b424c;
    border-color: #858e99;
}

.operation-icon {
    font-size: 17px;
    line-height: 1;
    margin-bottom: 4px;
}

.operation-title {
    font-size: 11px;
    font-weight: 700;
    color: #ffffff !important;
    line-height: 1.2;
}

.operation-subtitle {
    font-size: 10px;
    color: #c7ced6 !important;
    margin-top: 2px;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 6px;
    background-color: #11161d;
    padding: 6px;
    border-radius: 12px;
    border: 1px solid #35404d;
}

.stTabs [data-baseweb="tab"] {
    color: #ffffff !important;
    background-color: #1a212b !important;
    border-radius: 8px;
    padding: 9px 16px;
    font-size: 14px;
}

.stTabs [data-baseweb="tab"]:hover {
    background-color: #3b424c !important;
    color: #ffffff !important;
}

.stTabs [aria-selected="true"] {
    background-color: #b8bec6 !important;
    color: #10151b !important;
}

.stTabs [aria-selected="true"] * {
    color: #10151b !important;
}

.stRadio [role="radiogroup"] {
    gap: 10px;
}

.stRadio [role="radio"] {
    background-color: #1b222c !important;
    border: 1px solid #46515f !important;
    border-radius: 8px;
    padding: 8px 14px;
}

.stRadio [role="radio"]:hover {
    background-color: #3b424c !important;
}

.stRadio [role="radio"] p {
    color: #ffffff !important;
}

.stRadio [aria-checked="true"] {
    background-color: #b8bec6 !important;
    border-color: #b8bec6 !important;
}

.stRadio [aria-checked="true"] p {
    color: #10151b !important;
}

.stCheckbox label {
    color: #ffffff !important;
}

div[data-testid="stAlert"] {
    border-radius: 10px;
}

hr {
    border-color: #35404d !important;
}

</style>
""", unsafe_allow_html=True)


def get_files():
    return [
        item for item in Path(".").iterdir()
        if item.is_file() and item.name != "app.py"
    ]


def file_exists(name):
    return Path(name).exists()


with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">📁 File Handler</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-text">Manage your files easily</div>',
        unsafe_allow_html=True
    )

    st.divider()

    files = get_files()

    st.markdown("### 📂 Current Files")

    if files:
        for file in files:
            st.markdown(
                f"""
                <div class="file-card">
                    📄 <b>{file.name}</b>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.info("No files found.")

    st.divider()
    st.caption("File Handler • Streamlit App")


st.markdown(
    '<div class="main-title">📁 File Handler</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Create, read, update and delete your files from one simple interface.'
    '</div>',
    unsafe_allow_html=True
)


files = get_files()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div class="operation-card">
            <div class="operation-icon">📄</div>
            <div class="operation-title">TOTAL FILES</div>
            <div class="operation-subtitle">{len(files)} files</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="operation-card active">
            <div class="operation-icon">➕</div>
            <div class="operation-title">CREATE</div>
            <div class="operation-subtitle">New File</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="operation-card">
            <div class="operation-icon">✏️</div>
            <div class="operation-title">UPDATE</div>
            <div class="operation-subtitle">Edit File</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        """
        <div class="operation-card">
            <div class="operation-icon">🗑️</div>
            <div class="operation-title">DELETE</div>
            <div class="operation-subtitle">Remove File</div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")
st.divider()
st.write("")


tab1, tab2, tab3, tab4 = st.tabs([
    "➕ Create",
    "📖 Read",
    "✏️ Update",
    "🗑️ Delete"
])


with tab1:

    st.markdown(
        '<div class="section-title">Create a New File</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="card">', unsafe_allow_html=True)

    file_name = st.text_input(
        "File Name",
        placeholder="example.txt",
        key="create_name"
    )

    file_data = st.text_area(
        "File Content",
        placeholder="Write something here...",
        height=180,
        key="create_data"
    )

    if st.button("➕ Create File", key="create_button"):

        if not file_name.strip():
            st.warning("Please enter a file name.")

        elif file_exists(file_name):
            st.error("A file with this name already exists.")

        else:
            try:
                with open(file_name, "w", encoding="utf-8") as fs:
                    fs.write(file_data)

                st.success(
                    f"File '{file_name}' created successfully!"
                )

                st.rerun()

            except Exception as err:
                st.error(f"An error occurred: {err}")

    st.markdown('</div>', unsafe_allow_html=True)


with tab2:

    st.markdown(
        '<div class="section-title">Read File</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="description">'
        'Select a file and view its contents.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="card">', unsafe_allow_html=True)

    files = get_files()
    file_names = [file.name for file in files]

    if file_names:

        selected_file = st.selectbox(
            "Select File",
            file_names,
            key="read_file"
        )

        if st.button("📖 Read File", key="read_button"):

            try:
                with open(
                    selected_file,
                    "r",
                    encoding="utf-8"
                ) as fs:
                    content = fs.read()

                st.success("File read successfully.")

                st.text_area(
                    "File Content",
                    value=content,
                    height=300,
                    disabled=True,
                    key="read_content"
                )

            except Exception as err:
                st.error(f"An error occurred: {err}")

    else:
        st.info("No files available to read.")

    st.markdown('</div>', unsafe_allow_html=True)


with tab3:

    st.markdown(
        '<div class="section-title">Update File</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="description">'
        'Select a file and choose an operation.'
        '</div>',
        unsafe_allow_html=True
    )

    files = get_files()
    file_names = [file.name for file in files]

    if file_names:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        selected_file = st.selectbox(
            "Select File",
            file_names,
            key="update_file"
        )

        operation = st.radio(
            "Choose Operation",
            [
                "Rename File",
                "Append Content",
                "Overwrite File"
            ],
            horizontal=True,
            key="update_operation"
        )

        st.markdown('</div>', unsafe_allow_html=True)


        if operation == "Rename File":

            st.markdown(
                '<div class="section-title">Rename File</div>',
                unsafe_allow_html=True
            )

            new_name = st.text_input(
                "New File Name",
                placeholder="new_name.txt",
                key="rename_name"
            )

            if st.button(
                "✏️ Rename File",
                key="rename_button"
            ):

                if not new_name.strip():
                    st.warning("Please enter a new file name.")

                elif file_exists(new_name):
                    st.error(
                        "A file with that name already exists."
                    )

                else:
                    try:
                        Path(selected_file).rename(
                            Path(new_name)
                        )

                        st.success(
                            f"'{selected_file}' renamed to "
                            f"'{new_name}' successfully!"
                        )

                        st.rerun()

                    except Exception as err:
                        st.error(
                            f"An error occurred: {err}"
                        )


        elif operation == "Append Content":

            st.markdown(
                '<div class="section-title">Append Content</div>',
                unsafe_allow_html=True
            )

            append_data = st.text_area(
                "Content to Append",
                placeholder="Enter content you want to add...",
                height=150,
                key="append_data"
            )

            if st.button(
                "➕ Append Content",
                key="append_button"
            ):

                if not append_data.strip():
                    st.warning("Please enter some content.")

                else:
                    try:
                        with open(
                            selected_file,
                            "a",
                            encoding="utf-8"
                        ) as fs:
                            fs.write(" " + append_data)

                        st.success(
                            "Content appended successfully!"
                        )

                    except Exception as err:
                        st.error(
                            f"An error occurred: {err}"
                        )


        elif operation == "Overwrite File":

            st.markdown(
                '<div class="section-title">Overwrite File</div>',
                unsafe_allow_html=True
            )

            overwrite_data = st.text_area(
                "New File Content",
                placeholder="Enter the new content...",
                height=180,
                key="overwrite_data"
            )

            if st.button(
                "🔄 Overwrite File",
                key="overwrite_button"
            ):

                if not overwrite_data.strip():
                    st.warning("Please enter new content.")

                else:
                    try:
                        with open(
                            selected_file,
                            "w",
                            encoding="utf-8"
                        ) as fs:
                            fs.write(overwrite_data)

                        st.success(
                            "File overwritten successfully!"
                        )

                    except Exception as err:
                        st.error(
                            f"An error occurred: {err}"
                        )

    else:
        st.info("No files available to update.")


with tab4:

    st.markdown(
        '<div class="section-title">Delete File</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="description">'
        'Select a file and permanently remove it.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="card">', unsafe_allow_html=True)

    files = get_files()
    file_names = [file.name for file in files]

    if file_names:

        selected_file = st.selectbox(
            "Select File",
            file_names,
            key="delete_file"
        )

        st.warning(
            "⚠️ Deleting a file is permanent. "
            "Make sure you have selected the correct file."
        )

        confirm_delete = st.checkbox(
            "I understand that this file will be permanently deleted.",
            key="confirm_delete"
        )

        if st.button(
            "🗑️ Delete File",
            key="delete_button"
        ):

            if not confirm_delete:
                st.warning(
                    "Please confirm the deletion first."
                )

            else:
                try:
                    Path(selected_file).unlink()

                    st.success(
                        f"File '{selected_file}' deleted successfully!"
                    )

                    st.rerun()

                except Exception as err:
                    st.error(
                        f"An error occurred: {err}"
                    )

    else:
        st.info("No files available to delete.")

    st.markdown('</div>', unsafe_allow_html=True)


st.write("")
st.divider()

st.markdown(
    """
    <div style="text-align:center; color:#c0c7d0; padding:15px;">
        Built with Python 🐍 & Streamlit ⚡
        <br>
        <small>File Handler • CRUD File Management</small>
    </div>
    """,
    unsafe_allow_html=True
)