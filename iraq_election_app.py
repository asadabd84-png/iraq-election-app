import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="الانتخابات البرلمانية العراقية - قانون سانت ليغو", layout="centered")

# تنسيق الشعار والعلم في الأعلى
col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/f/f6/Independent_High_Electoral_Commission_of_Iraq_Logo.png", width=100)
with col2:
    st.markdown("<h2 style='text-align:center; color:#d32f2f;'>الانتخابات البرلمانية العراقية - قانون سانت ليغو المعدل</h2>", unsafe_allow_html=True)
with col3:
    st.image("https://upload.wikimedia.org/wikipedia/commons/f/f6/Flag_of_Iraq.svg", width=100)

st.markdown("---")

# إدخال البيانات الأساسية
province = st.text_input("📍 اسم المحافظة:")
total_seats = st.number_input("🪑 عدد المقاعد الكلي:", min_value=1, step=1)
divisor = st.number_input("⚖️ القاسم الانتخابي (مثلاً 1.7 أو 1.9):", min_value=1.0, value=1.7, step=0.1)

st.markdown("---")

# إدخال أسماء الأحزاب والأصوات
st.subheader("🧾 إدخال بيانات الأحزاب")
num_parties = st.number_input("عدد الأحزاب:", min_value=1, step=1, value=4)

party_data = []
for i in range(num_parties):
    col1, col2 = st.columns(2)
    name = col1.text_input(f"اسم الحزب رقم {i+1}")
    votes = col2.number_input(f"عدد الأصوات للحزب {i+1}", min_value=0, step=1000)
    if name:
        party_data.append((name, votes))

# زر الحساب
if st.button("✅ احسب توزيع المقاعد"):
    if not province or not party_data or total_seats == 0:
        st.warning("⚠️ يرجى إدخال جميع البيانات المطلوبة.")
    else:
        # حساب المقاعد وفق قانون سانت ليغو
        quotients = []
        for name, votes in party_data:
            for d in range(1, total_seats * 2, 2):  # 1, 3, 5, 7, ...
                quotients.append((name, votes / (d * divisor)))

        quotients.sort(key=lambda x: x[1], reverse=True)
        seats = {name: 0 for name, _ in party_data}

        for i in range(total_seats):
            party = quotients[i][0]
            seats[party] += 1

        # كوتا النساء: كل ثالث مقعد للنساء
        results = []
        for name, num in seats.items():
            women = num // 3
            men = num - women
            results.append([name, men, women, num])

        df = pd.DataFrame(results, columns=["الحزب", "مقاعد الرجال", "مقاعد النساء", "الإجمالي"])

        st.success(f"📊 نتائج توزيع المقاعد في محافظة {province}")
        st.dataframe(df, use_container_width=True)

        # تحميل النتائج كملف CSV
        csv = df.to_csv(index=False).encode('utf-8-sig')
        st.download_button(
            label="📥 تحميل النتائج كملف CSV",
            data=csv,
            file_name=f"SainteLague_{province}.csv",
            mime='text/csv'
        )

st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>تطوير: قسم التحليل الإحصائي - وزارة التخطيط 🇮🇶</p>", unsafe_allow_html=True)
