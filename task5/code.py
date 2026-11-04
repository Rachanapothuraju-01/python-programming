
# Advanced String-Based Registration Record Analyzer

registration_ids = []

n = int(input("Enter number of records: "))

for i in range(n):
    print("\nEnter Registration Record", i + 1)

    record = input("ID,Name,Email,Phone: ")

    fields = record.split(",")

    errors = []

    if len(fields) != 4:
        print("Error: Invalid number of fields")
        continue

    reg_id = fields[0].strip()
    name = fields[1].strip()
    email = fields[2].strip()
    phone = fields[3].strip()

    # Validate ID
    if len(reg_id) != 5 or not reg_id.isalnum():
        errors.append("Invalid ID")

    # Validate Name
    if len(name) < 3 or not name.replace(" ", "").isalpha():
        errors.append("Invalid Name")

    # Validate Email
    if "@" not in email or "." not in email.split("@")[-1]:
        errors.append("Invalid Email")

    # Validate Phone
    if len(phone) != 10 or not phone.isdigit():
        errors.append("Invalid Phone")

    # Check Duplicate ID
    if reg_id in registration_ids:
        errors.append("Duplicate ID")
    else:
        registration_ids.append(reg_id)

    # Display Result
    if len(errors) == 0:
        print("Registration Successful")
        print("ID:", reg_id)
        print("Name:", name)
        print("Email:", email)
        print("Phone:", phone)
    else:
        print("Registration Failed")
        print("Error Classification:", ", ".join(errors))

print("\nRegistration Analysis Completed")

