import streamlit as st

def calculator():
    st.title("Simple Calculator")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")

    operation = st.radio("Select Operation", ("Addition", "Subtraction", "Multiplication", "Division"))

    if st.button("Calculate"):
        if operation == "Addition":
            result = num1 + num2
            st.success("The result of {} + {} is {}".format(num1, num2, result))
        elif operation == "Subtraction":
            result = num1 - num2
            st.success("The result of {} - {} is {}".format(num1, num2, result))
        elif operation == "Multiplication":
            result = num1 * num2
            st.success("The result of {} * {} is {}".format(num1, num2, result))
        elif operation == "Division":
            if num2 == 0:
                st.error("Cannot divide by zero!")
            else:
                result = num1 / num2
                st.success("The result of {} / {} is {}".format(num1, num2, result))

if __name__ == "__main__":
    calculator()
