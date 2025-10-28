import streamlit as st
import math
import pandas as pd

# =============================
# 🇮🇶 واجهة تطبيق قانون سانت ليغو المعدّل
# =============================

st.image("https://upload.wikimedia.org/wikipedia/commons/f/f6/Flag_of_Iraq.svg", width=150)

st.markdown(
    """
    <h2 style='text-align:center; color:#b30000;'>
    الانتخابات البرلمانية العراقية - قانون سانت ليغو المعدل
    </h2>
    """, unsafe_allow_html=True
)

st.write("---")

# =============================
# 📍 إدخال بيانات المحافظة
# =============================
st.subheader("📍 إدخال بيانات المحافظة")
governorate = st.text_input("اسم المحافظة:")
total_seats = st.number_input("🪑 عدد المقاعد الكلي:", min_value=1, max_value=100, value=10)
divisor = st.number_input("⚖️ القاسم الانتخابي (مثل 1.7 أو 1.9):", min_value=1.0, max_value=2.0, value=1.7, step=0.1)

st.write("---")

# =============================
# 🗳️ إدخال بيانات الأحزاب
# =============================
st.subheader("🗳️ إدخال بيانات الأحزاب")
num_parties = st.number_input("عدد الأحزاب المشاركة:", min_value=1, max_value=20, value=3)

parties = {}
for i in range(int(num_parties)):
    name = st.text_input(f"اسم الحزب رقم {i+1}:", key=f"name_{i}")
    votes = st.number_input(f"عدد الأصوات للحزب رقم {i+1}:", min_value=0, step=100, key=f"votes_{i}")
    if name:
        parties[name] = votes

# =============================
# 🧮 حساب المقاعد
# =============================
if st.button("احسب توزيع المقاعد"):
    if len(parties) == 0 or sum(parties.values()) == 0:
        st.warning("الرجاء إدخال أصوات صحيحة للأحزاب.")
    else:
        # تطبيق قانون سانت ليغو المعدّل
        results = []
        for party, votes in parties.items():
            for n in range(1, total_seats * 2):
                results.append((party, votes / (divisor + 2 * (n - 1))))

        results.sort(key=lambda x: x[1], reverse=True)
        allocated = {}

        # توزيع المقاعد الكلية
        for i in range(total_seats):
            party = results[i][0]
            allocated[party] = allocated.get(party, 0) + 1

        # =============================
        # 👩‍🦰👨‍🦱 حساب مقاعد الرجال والنساء
        # قاعدة: كل 3 رجال → امرأة واحدة (أي 1 من كل 4 نساء)
        # =============================
        data = []
        for party, seats in allocated.items():
            female_seats = seats // 4  # امرأة لكل 4 مقاعد
            male_seats = seats - female_seats
            data.append([party, seats, male_seats, female_seats])

        df = pd.DataFrame(data, columns=["الحزب", "إجمالي المقاعد", "مقاعد الرجال", "مقاعد النساء"])

        st.success(f"✅ نتائج محافظة {governorate if governorate else 'غير محددة'}:")
        st.dataframe(df, use_container_width=True)

st.write("---")

# =============================
# 🖋️ تذييل الصفحة
# =============================
st.markdown(
    """
    <div style='text-align:center; font-size:16px; color:gray;'>
    تصميم: الدكتور أسعد دبيش © 2025
    </div>
    """, unsafe_allow_html=True
)
