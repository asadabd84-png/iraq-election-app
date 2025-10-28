import streamlit as st

# =============================
# 🇮🇶 واجهة بسيطة بعلم العراق فقط
# =============================

# إظهار العلم العراقي
st.image("https://upload.wikimedia.org/wikipedia/commons/f/f6/Flag_of_Iraq.svg", width=150)

# عنوان التطبيق
st.markdown(
    """
    <h2 style='text-align:center; color:#b30000;'>
    الانتخابات البرلمانية العراقية - قانون سانت ليغو المعدل
    </h2>
    """, unsafe_allow_html=True
)

# مسافة بسيطة
st.write("---")

# رسالة أو محتوى تجريبي
st.markdown(
    """
    <div style='text-align:center; font-size:20px;'>
    <b>مرحباً بك في تطبيق توزيع المقاعد البرلمانية وفق قانون سانت ليغو المعدل.</b>
    </div>
    """, unsafe_allow_html=True
)

# مسافة للفصل
st.write("---")

# تذييل الصفحة (Footer)
st.markdown(
    """
    <div style='text-align:center; font-size:16px; color:gray;'>
    المفوضية العليا المستقلة للانتخابات - تصميم: الدكتور أسعد دبيش © 2025
    </div>
    """, unsafe_allow_html=True
)
