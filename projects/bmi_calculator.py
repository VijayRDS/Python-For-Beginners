"""
BMI Calculator - Python for Beginners
=====================================
Concepts covered:
- User input with input()
- Type conversion (float, int)
- Mathematical operations
- Conditional statements (if/elif/else)
- String formatting (f-strings)
- Functions and return values
- Exception handling (try/except)
- While loops for input validation

BMI Formula: weight (kg) / height (m)²
"""

def calculate_bmi(weight, height): ## Calculate BMI given weight in kg and height in meters
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi): #Return health category based on BMI value according to WHO standards

    if bmi < 16:
        return "Severely Underweight"
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Moderately Obese"
    elif bmi < 40:
        return "Severely Obese"
    else:
        return "Very Severely Obese"


def get_health_advice(category): #Provide basic health advice based on BMI category

    advice = {
        "Severely Underweight": "⚠️  Please consult a healthcare provider immediately.",
        "Underweight": "💡 Consider a balanced diet with more calories and consult a nutritionist.",
        "Normal weight": "✅ Great! Maintain your current lifestyle with regular exercise and balanced diet.",
        "Overweight": "💡 Consider regular exercise and a balanced diet. Small changes can make a big difference!",
        "Moderately Obese": "⚠️  Consider consulting a healthcare provider for a personalized plan.",
        "Severely Obese": "⚠️  Please consult a healthcare provider for professional guidance.",
        "Very Severely Obese": "⚠️  Please consult a healthcare provider immediately."
    }
    return advice.get(category, "Consult a healthcare provider for personalized advice.")


def get_positive_float(prompt): #Get a positive float value from user with input validation

    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("❌ Please enter a positive number!")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid number!")


def convert_height_to_meters(): #Allow users to input height in different units and convert to meters

    print("\nChoose height input method:")
    print("1. Meters (e.g., 1.75)")
    print("2. Centimeters (e.g., 175)")
    print("3. Feet and inches (e.g., 5 feet 9 inches)")
    
    while True:
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            return get_positive_float("Enter your height in meters: ")
        
        elif choice == "2":
            cm = get_positive_float("Enter your height in centimeters: ")
            return cm / 100  # Convert cm to meters
        
        elif choice == "3":
            feet = get_positive_float("Enter feet: ")
            inches = get_positive_float("Enter inches: ")
            total_inches = (feet * 12) + inches
            return total_inches * 0.0254  # Convert inches to meters
        
        else:
            print("❌ Please enter 1, 2, or 3!")


def main():
    """Main function that runs the BMI calculator"""
    print("=" * 50)
    print("🏥 BMI CALCULATOR - Learn Python Basics! 🏥")
    print("=" * 50)
    print("\nThis calculator will help you:")
    print("• Calculate your Body Mass Index (BMI)")
    print("• Understand your health category")
    print("• Get basic health advice")
    print("\n" + "=" * 50)
    
    # Get user input
    print("\n📏 Let's start with your measurements:")
    
    # Weight input
    weight = get_positive_float("Enter your weight in kilograms: ")
    
    # Height input with unit conversion
    height = convert_height_to_meters()
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)
    advice = get_health_advice(category)
    
    # Display results
    print("\n" + "=" * 50)
    print("📊 YOUR BMI RESULTS")
    print("=" * 50)
    print(f"Weight: {weight} kg")
    print(f"Height: {height:.2f} meters")
    print(f"BMI: {bmi}")
    print(f"Category: {category}")
    print(f"\n💡 Health Advice:")
    print(f"{advice}")
    
    # BMI ranges reference
    print("\n📋 BMI Categories Reference:")
    print("─" * 30)
    print("Below 18.5    → Underweight")
    print("18.5 - 24.9   → Normal weight")
    print("25.0 - 29.9   → Overweight")
    print("30.0 and above → Obese")
    
    print("\n⚠️  Note: BMI is a screening tool. Consult healthcare providers for medical advice.")
    

# Additional feature: Multiple calculations
def run_multiple_calculations():
    """Allow users to calculate BMI for multiple people"""
    while True:
        main()
        
        print("\n" + "=" * 50)
        another = input("Calculate BMI for another person? (y/n): ").lower().strip()
        
        if another not in ['y', 'yes']:
            print("\n✨ Thank you for using BMI Calculator!")
            print("🐍 Keep practicing Python - you're doing great!")
            break
        
        print("\n" + "=" * 50)


# Run the program
if __name__ == "__main__":
    main()