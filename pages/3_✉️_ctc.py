import streamlit as st

#for google anaylytics000000000000000
GA_ID = "G-HRBHNW2DZJ"

st.components.v1.html(
    f"""
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{GA_ID}');
    </script>
    """,
    height=0,
)

#Contact form
with st.container():
    st.container()
    st.write("---")
    st.header("Get In Contact with me!")



st.markdown(
    """
    <style>
    /* Contact Form Container */
    .contact-form {
        max-width: 420px;
        background: rgba(255, 255, 255, 0.05);
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.25);
        backdrop-filter: blur(10px);
        font-family: "JetBrains Mono", monospace;
    }

    .form-group { margin-bottom: 18px; }

    .contact-form input,
    .contact-form textarea {
        width: 100%;
        padding: 12px 14px;
        border-radius: 10px;
        border: 1px solid rgba(255,255,255,0.2);
        background: rgba(0,0,0,0.4);
        color: white;
        font-size: 14px;
        outline: none;
        transition: all 0.25s ease;
    }

    .contact-form input::placeholder,
    .contact-form textarea::placeholder { color: #b5b5b5; }

    .contact-form input:focus,
    .contact-form textarea:focus {
        border-color: #00c6ff;
        box-shadow: 0 0 0 2px rgba(0,198,255,0.2);
        background: rgba(0,0,0,0.55);
    }

    .submit-btn {
        width: 100%;
        padding: 12px;
        border-radius: 12px;
        border: none;
        background: linear-gradient(135deg, #00c6ff, #0072ff);
        color: white;
        font-size: 15px;
        font-weight: 600;
        cursor: pointer;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .submit-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0,114,255,0.4);
    }

    .submit-btn:active {
        transform: translateY(0);
        box-shadow: 0 4px 10px rgba(0,114,255,0.3);
    }
    </style>

    <form action="https://formsubmit.co/krrishsp.in@gmail.com" method="POST" class="contact-form">
        <input type="hidden" name="_captcha" value="false">
        <div class="form-group">
            <input type="text" name="name" placeholder="Your Name" required>
        </div>
        <div class="form-group">
            <input type="email" name="email" placeholder="Your Email" required>
        </div>
        <div class="form-group">
            <textarea name="message" placeholder="Your Message" rows="5" required></textarea>
        </div>
        <button type="submit" class="submit-btn">Send Message 🚀</button>
    </form>
    """,
    unsafe_allow_html=True
)

