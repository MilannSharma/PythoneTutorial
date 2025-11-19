
# Define the function using match-case


def http_status(status):
    match status:
        case "200":
            return "✅ OK - Request succeeded"
        case "400":
            return "🚫 Bad Request"
        case "401":
            return "🔒 Unauthorized"
        case "403":
            return "⛔ Forbidden"
        case "404":
            return "❌ Not Found"
        case "500":
            return "💥 Internal Server Error"
        case _:
            return "❓ Unknown status code"

# Get user input
b = input("Enter an HTTP status : ")

# Call the function and print result
o = http_status(b)
print(o)

