import streamlit as st
import pandas as pd

# ==============================
# 🎯 إعداد واجهة التطبيق
# ==============================
st.set_page_config(page_title="الانتخابات البرلمانية العراقية", page_icon="🇮🇶", layout="centered")

# ==============================
# 🏛️ العنوان الرئيسي مع الشعارات
# ==============================
col1, col2, col3 = st.columns([1, 5, 1])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/09/Iraqi_flag.svg", width=90)
with col2:
    st.markdown("<h2 style='text-align:center; color:red;'>الانتخابات البرلمانية العراقية<br>قانون سانت ليغو المعدل (1.7)</h2>", unsafe_allow_html=True)
with col3:
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2a/IHEC_Logo.png", width=90)

# ==============================
# 🗳️ إدخال البيانات الأساسية
# ==============================
st.markdown("### 🧾 إدخال بيانات الدائرة الانتخابية")

province = st.text_input("📍 اسم المحافظة:")
total_seats = st.number_input("🎟️ عدد المقاعد الكلي:", min_value=1, value=10)
divisor = st.number_input("⚖️ القاسم الانتخابي (مثل 1.7 أو 1.9):", min_value=1.0, value=1.7, step=0.1)

# ==============================
# 🏛️ إدخال بيانات الأحزاب
# ==============================
st.markdown("### 🗂️ إدخال بيانات الأحزاب")
num_parties = st.number_input("عدد الأحزاب المشاركة:", min_value=1, value=4, step=1)

party_names = []
votes = []

for i in range(num_parties):
    c1, c2 = st.columns([3, 2])
    with c1:
        name = st.text_input(f"اسم الحزب {i+1}:")
    with c2:
        vote = st.number_input(f"عدد الأصوات للحزب {i+1}:", min_value=0, step=100)
    party_names.append(name)
    votes.append(vote)

# ==============================
# 📊 حساب المقاعد وفق قانون سانت ليغو
# ==============================
if st.button("📈 حساب النتائج"):
    data = pd.DataFrame({"الحزب": party_names, "الأصوات": votes})

    if data["الأصوات"].sum() == 0:
        st.warning("يرجى إدخال عدد أصوات صحيح لكل حزب.")
    else:
        results = []
        for idx, row in data.iterrows():
            for j in range(total_seats):
                results.append({
                    "الحزب": row["الحزب"],
                    "القيمة": row["الأصوات"] / ((2 * j) + divisor)
                })
        df = pd.DataFrame(results)
        df = df.sort_values("القيمة", ascending=False).head(total_seats)

        # حساب المقاعد
        seat_count = df["الحزب"].value_counts().reset_index()
        seat_count.columns = ["الحزب", "عدد المقاعد"]

        # توزيع المقاعد رجال / نساء
        gender_split = []
        for _, row in seat_count.iterrows():
            men = row["عدد المقاعد"] // 3 * 2 + (row["عدد المقاعد"] % 3 if row["عدد المقاعد"] % 3 < 2 else 2)
            women = row["عدد المقاعد"] - men
            gender_split.append({"الحزب": row["الحزب"], "مقاعد الرجال": men, "مقاعد النساء": women})

        gender_df = pd.DataFrame(gender_split)

        st.success(f"✅ تم حساب النتائج لمحافظة **{province or 'غير محددة'}** بنجاح!")
        st.dataframe(gender_df)

        st.markdown("### 📊 تفاصيل التوزيع الكامل:")
        st.bar_chart(gender_df.set_index("الحزب")[["مقاعد الرجال", "مقاعد النساء"]])

# ==============================
# 📄 تذييل الصفحة
# ==============================
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>© 2025 المفوضية العليا المستقلة للانتخابات - تصميم: أسعد داخل هندول</p>", unsafe_allow_html=True)
