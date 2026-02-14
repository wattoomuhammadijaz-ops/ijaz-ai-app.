import streamlit as st
import google.generativeai as genai

# Aapki provide ki hui API Key
API_KEY = "AIzaSyD-j4eECPsggnMxuhLtJB9gLFtC94h0IiI"
genai.configure(api_key=API_KEY)

# App ka setup aur design
st.set_page_config(page_title="IJAZ AI - Waseem", page_icon="🚀")

# Sidebar mein aapka naam
st.sidebar.title("Developer Details")
st.sidebar.write("Name: **Ijaz**")
st.sidebar.info("Ye app Google Gemini AI istemal karti hai.")

# Main Screen
st.title("🚀 IJAZ WA2 AI Studio")
st.subheader("Ijaz wa2  ki Pehli AI App")
st.write("Neeche diye gaye box mein kuch bhi likhein aur AI se jawab payein.")

# Input box
user_question = st.text_input("Aap kya poochna chahte hain?", placeholder="Maslan: Python kya hai?")

# Jab button dabaya jaye
if st.button("AI se Poochein"):
    if user_question:
        try:
            with st.spinner('Soch raha hoon...'):
                # Model selection
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(user_question)
                
                # Result dikhana
                st.markdown("### ✨ AI ka Jawab:")
                st.success(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
            st.info("Check karein ke aapka internet chal raha hai aur API key sahi hai.")
    else:
        st.warning("Janab, pehle sawal to likhein!")

# Footer
st.markdown("---")
st.caption("© 2026 Wattoo AI Studio | Built with Python & Streamlit")