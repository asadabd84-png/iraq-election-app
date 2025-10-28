import streamlit as st

# =============================
# 🇮🇶 واجهة مبسطة تحتوي على العلم العراقي فقط
# =============================

# عرض العلم العراقي في الأعلى
st.image("https://upload.wikimedia.org/wikipedia/commons/f/f6/Flag_of_Iraq.svg", width=150)

# العنوان الرئيسي للتطبيق
st.markdown(
    """
    <h2 style='text-align:center; color:#b30000;'>
    الانتخابات البرلمانية العراقية - قانون سانت ليغو المعدل
    </h2>
    """, unsafe_allow_html=True
)

# فاصل بسيط
st.write("---")

# رسالة ترحيبية أو نص توضيحي
st.markdown(
    """
    <div style='text-align:center; font-size:20px;'>
    <b>مرحباً بك في تطبيق توزيع المقاعد البرلمانية وفق قانون سانت ليغو المعدل.</b>
    </div>
    """, unsafe_allow_html=True
)

# فاصل قبل التذييل
st.write("---")

# تذييل الصفحة (Footer)
st.markdown(
    """
    <div style='text-align:center; font-size:16px; color:gray;'>
    تصميم: الدكتور أسعد دبيش © 2025
    </div>
    """, unsafe_allow_html=True
)
