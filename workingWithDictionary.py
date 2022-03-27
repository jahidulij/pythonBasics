month_conversions = {
    "Jan": "January",
    "Feb": "february",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "Agust",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(month_conversions["Nov"])
print(month_conversions.get("Dec"))
print(month_conversions.get("Tes", "Invalid key"))