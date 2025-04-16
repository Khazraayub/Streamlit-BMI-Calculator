import streamlit as st

# Initialize history
if 'bmi_history' not in st.session_state:
    st.session_state.bmi_history = []

# Calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Get category, emoji, and message
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "🥶", "Try eating more balanced meals."
    elif 18.5 <= bmi < 24.9:
        return "Normal", "💪", "You're doing great!"
    elif 25 <= bmi < 29.9:
        return "Overweight", "🍕", "Maybe a little extra workout?"
    else:
        return "Obesity", "🍔", "Time to make some lifestyle changes!"

# BMI range visual with emojis
def show_bmi_range():
    st.subheader("📊 BMI Categories")
    st.markdown("""
    - 🥶 **Underweight**: BMI < 18.5  
    - 💪 **Normal**: 18.5 ≤ BMI < 24.9  
    - 🍕 **Overweight**: 25 ≤ BMI < 29.9  
    - 🍔 **Obesity**: BMI ≥ 30  
    """)

# App UI
st.title("BMI Calculator 💥")
st.markdown("Check your BMI and get personalized feedback with emojis! 😄")

# User inputs
name = st.text_input("👤 Enter your name:")
weight = st.number_input("⚖️ Enter your weight (kg):", min_value=1.0)
height = st.number_input("📏 Enter your height (meters):", min_value=0.1)

# Calculate Button
if st.button("🚀 Calculate BMI"):
    if name and weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        category, emoji, message = get_bmi_category(bmi)

        st.success(f"Hey {name}!")
        st.write(f"Your BMI is: **{bmi:.2f}**")
        st.write(f"Category: **{category}** {emoji}")
        st.info(message)

        # Update history
        st.session_state.bmi_history.append(f"{name} ➜ BMI: {bmi:.2f} ({category})")
        if len(st.session_state.bmi_history) > 5:
            st.session_state.bmi_history = st.session_state.bmi_history[-5:]

        # Show history
        st.subheader("🕘 Recent BMI History")
        for record in reversed(st.session_state.bmi_history):
            st.write("•", record)

        # Show categories
        show_bmi_range()
    else:
        st.warning("Please enter all required information.")
