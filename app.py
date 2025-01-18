import streamlit as st
from datetime import datetime
import base64
from pathlib import Path
import random

# Cấu hình trang
st.set_page_config(
    page_title="Chúc Mừng Sinh Nhật",
    page_icon="🎂",
    layout="centered"
)

def load_external_files():
    """Load external CSS and JavaScript files"""
    # Load CSS
    with open('css/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    # Load JavaScript
    with open('js/birthday.js') as f:
        st.markdown(f'<script>{f.read()}</script>', unsafe_allow_html=True)

def get_image_base64(image_path):
    """Convert image to base64"""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def autoplay_audio(file_path: str):
    """Play audio in background"""
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

def show_love_popup():
    """Display birthday wishes popup"""
    popup_html = """
        <div class="popup-overlay" id="lovePopup">
            <div class="popup-content">
                <span class="heart-decoration heart-1">❤️</span>
                <span class="heart-decoration heart-2">❤️</span>
                <span class="heart-decoration heart-3">❤️</span>
                <span class="heart-decoration heart-4">❤️</span>
                <button class="close-popup" onclick="closePopup()">×</button>
                <div class="love-message">
                    <p>Chúc mừng sinh nhật em yêu tròn 22 tuổi! ❤️</p>
                    <p>Chúc em luôn xinh đẹp, rạng rỡ như ánh nắng ban mai, và tràn đầy hạnh phúc bên anh.</p>
                    <p>Cảm ơn em vì đã là điều tuyệt vời nhất trong cuộc sống của anh.</p>
                    <p>Anh sẽ luôn ở đây, yêu thương và đồng hành cùng em trên mọi chặng đường.</p>
                    <p>Yêu em thật nhiều! 🎂💐🎉</p>
                </div>
            </div>
        </div>
    """
    st.markdown(popup_html, unsafe_allow_html=True)

def display_images():
    """Display all memory images at once"""
    image_files = list(Path("assets/images").glob("*.jpg"))
    if not image_files:
        return
    
    captions = [
        "Khoảnh khắc đáng yêu 💖",
        "Nụ cười tỏa nắng ✨",
        "Những kỷ niệm ngọt ngào 🌸",
        "Hạnh phúc là khi có em 💝",
        "Xinh đẹp như thiên thần 👼",
        "Mãi yêu em 💕",
        "Những phút giây tuyệt vời ✨",
        "Vẻ đẹp rạng ngời 🌟"
    ]
    
    st.markdown("""
        <div class="memories-grid">
    """, unsafe_allow_html=True)
    
    for img_path in image_files:
        img_base64 = get_image_base64(str(img_path))
        st.markdown(f"""
            <div class="memory-card">
                <img src="data:image/jpg;base64,{img_base64}" alt="Memory">
                <div class="caption">{random.choice(captions)}</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def main():
    """Main application function"""
    load_external_files()
    
    if 'page' not in st.session_state:
        st.session_state.page = 'login'
    
    if 'popup_shown' not in st.session_state:
        st.session_state.popup_shown = False

    if st.session_state.page == 'login':
        st.markdown('<h1 class="birthday-title">✨ Chào mừng bạn đến với trang chúc mừng sinh nhật đặc biệt! ✨</h1>', 
                   unsafe_allow_html=True)
        
        with st.form("birthday_form"):
            name = st.text_input("💝 Họ và Tên:")
            birth_date = st.date_input("🎂 Ngày tháng năm sinh:")
            
            submitted = st.form_submit_button("Xác nhận 🌟")
            
            if submitted:
                if (name.strip() == "Ngô Khánh Linh" and 
                    birth_date == datetime(2003, 1, 18).date()):
                    st.balloons()
                    st.session_state.page = 'birthday'
                    st.experimental_rerun()
                else:
                    st.error("💔 Thông tin chưa chính xác. Vui lòng kiểm tra lại!")

    elif st.session_state.page == 'birthday':
        if not st.session_state.popup_shown:
            show_love_popup()
            st.session_state.popup_shown = True
        
        autoplay_audio("assets/music/happy-birthday.mp3")
        
        st.markdown("""
            <div style="text-align: center;">
                <h1 class="birthday-title">
                    🌟 Chúc mừng sinh nhật Ngô Khánh Linh tròn 22 tuổi! 🎉
                </h1>
                <p style="color: #e91e63; font-size: 1.2rem; margin: 20px 0;">
                    Chúc em một ngày sinh nhật tràn ngập niềm vui và hạnh phúc! 💖
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("✨ Xem những kỷ niệm đẹp ✨", key="memory_btn"):
            st.snow()
            st.balloons()
            display_images()

if __name__ == "__main__":
    main() 