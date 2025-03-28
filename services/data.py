pnl_account_categories_dict = {
    "REVENUE": {
        "Revenue - Products": {
            4301001000: "Music",
            4301002000: "Sermon",
            4301003000: "Book",
            4301005000: "Apparel & Accessories",
            4301007000: "Sales Consignment",
            4301010000: "Live Sound & Installation",
            4301011000: "Recording",
        },
        "Revenue - Food and Beverage": {
            4400002000: "Food and Beverage Restaurant",
            4400003000: "Food and Beverage Catering",
        },
        "Service & Rental": {
            4601000000: "Room Rental",
            4602000000: "Lighting Equipment Rental",
            4603000000: "Sound System",
            4608000000: "Digital & Mobile Service",
            4610000000: "Multimedia",
            4611000000: "Service Subscribe",
            4604000000: "Service Charges",
        },
        "Other Revenue": {4701000000: "Management Fee", 4702000000: "Other"},
        "Sales Discount & Return": {
            4500000000: "Sales discount",
            4800000000: "Sales Return",
        },
    },
    "COGS": {
        "COGS - Products": {
            5101000000: "Music",
            5102000000: "Sermon",
            5103000000: "Book",
            5105000000: "Apparel & Accessories",
            5108000000: "Lighting",
            5109000000: "Sound System",
            5109001000: "Inventory BKA",
            5300000000: "Consignment",
        },
        "COGS - Food & Beverages": {
            5202000000: "Food and Beverage Restaurant",
            5203000000: "Food and Beverage Catering",
        },
        "COGS - Services & Rental": {
            5401000000: "Room Rental",
            5402000000: "Lighting Equipment Rental",
            5403000000: "Sound System Rental",
            5405000000: "Ministry Service",
            5410000000: "Multimedia",
            5411000000: "Upah Crew dan Material Project",
        },
        "Royalty": {
            5701000000: "Royalty Digital",
            5702000000: "Royalty Music",
            5703000000: "Royalty kotbah",
            5704000000: "Royalty Others",
        },
        "Others": {5600000000: "Others"},
    },
    "HUMAN RESOURCES": {
        "Salary and Benefit": {
            6201001010: "Basic Salary",
            6201001011: "Basic Salary",
            6201001020: "Meal Allowance",
            6201001021: "Meal Allowance",
            6201001030: "Transportation Allowance",
            6201001031: "Transportation Allowance",
            6201001040: "Communication Allowance",
            6201001200: "Over Time",
            6201001070: "Service Charge",
            6201008010: "Tax Allowance",
        },
        "Medical": {
            6201007010: "Dental",
            6201003001: "Jamsostek (JKK+JKM/Social Security Insurance)",
            6201003002: "Jamsostek (JKK+JKM/Social Security Insurance)",
            6201003010: "BPJS Kesehatan",
            6201003011: "BPJS Kesehatan",
            6201007020: "Eye Glasses",
            6201007030: "Maternity",
            6201007042: "Insurance",
            6201007043: "Inpatient",
            6201007045: "Outpatient",
            6201007040: "T. Kesehatan",
        },
        "Other": {
            6201009000: "Retirement Fee",
            6201009001: "Retirement Fee",
            6213000000: "Retirement Benefit",
            6203007000: "Place Accomodation",
            6201001050: "THR & Bonus",
            6201001051: "THR & Bonus",
            6201001060: "Incentive",
        },
        "Casual Expense": {
            6206000104: "Crew Casual",
            6206000101: "Banquet Casual",
            6206000102: "Cleaning Service Casual",
            6206000103: "Sound Engineer Casual",
            6206000105: "Engineering Casual",
            6206000106: "Security Casual",
            6206000107: "Usher Casual",
            6206000108: "Catering Casual",
        },
        "Freelance Expense": {6201001100: "Freelance", 6205001000: "Designer"},
        "Outsourcing Expense": {
            6205003000: "Security",
            6205000000: "Outsourcing / Workers Expenses",
        },
    },
    "OPERATIONAL EXPENSES": {
        "Event & Promotion": {
            6101001000: "Printing Media",
            6101002000: "Electronic Media",
            6101005000: "Special Event",
            6101008000: "Sales Promotion",
        },
        "Other Marketing and Sales Expenses": {
            6102000001: "Other M&S Expenses - Commission"
        },
        "Utility Expense": {
            6203001000: "Water",
            6203002000: "Electricity",
            6203002100: "Gas",
        },
        "Telephone & Internet Expense": {
            6203003000: "Telephone & Faximile",
            6203004000: "Internet & Hosting",
            6203011000: "Cable Vision",
        },
        "Supplies Expense": {
            6203006010: "Stationary & Supplies",
            6203006020: "Computer Supplies",
            6203006030: "Household Supplies",
            6203006040: "Hardware Equipment Supplies",
            6203005000: "Cleaning Materials",
            6203006060: "Department Supplies",
            6203006080: "Stage & Decoration Supplies",
            6203006050: "Shop Supplies",
            6203006070: "Kitchen Supplies",
            6203006090: "Department Event Expense",
        },
        "Rental Expense": {
            6203013090: "Rental - Venue",
            6203013080: "Rental - Equipment",
            6203013010: "Rental - Office",
            6203013020: "Rental - Warehouse",
            6203013030: "Rental - Photocopy",
            6203013040: "Rental - Vehicle",
            6203013060: "Rental - Store",
            6206000500: "Rental - Banquet Equipment",
            6203013070: "Rental - Rehearsal & Studio",
        },
        "General Affair Expenses": {
            6203008000: "Expedition",
            6203009000: "Printing & Photocopy",
            6203010000: "Consumption",
            6203017000: "Subscriptions & Software Program",
            6203018000: "Entertainments",
            6203020000: "Love Offering",
            6203021000: "Gift & Condolences",
            6203022000: "Resources",
            6206001000: "Accommodation & Airfare",
            6206001200: "Hospitality",
            # below was separated for some reason
            6203014000: "Plant",
            6203015000: "Uniform",
            6203016000: "Retribution",
            6206000700: "Laundry",
            6208000000: "Legal & Permit",
            6211000000: "Mailing & Stamp Expense",
        },
        "Travelling Expense": {
            6203023010: "Traveling National",
            6203023020: "Traveling International",
            6201001300: "Traveling Allowance",
        },
        "Complimentary Expense": {
            6206000801: "Complimentary Banquet",
            6206000802: "Complimentary Food and Beverage",
            6206000803: "Complimentary Other",
        },
        "Training & Seminars Expense": {
            6203025001: "Training & Seminar National",
            6203025002: "Training & Seminar International",
        },
        "Transportation Expense": {
            6203026010: "Bensin",
            6203026020: "Tol & Parkir",
            6203026030: "Kendaraan Umum",
            6203026040: "Transportation Expense",
        },
        "PPE Tax & Insurance Expense": {
            6202003100: "PPE Tax Expense",
            6202003200: "PPE Insurance Expense",
        },
        "Other General Affair Expense": {
            6203027000: "Recruitment Fee",
            6203028000: "Consultant Fee",
            6206000300: "Production Expense",
            6210000000: "Management Fee",
            6209000000: "Bad Debt Expense",
            6209100000: "Bad Debt Expense",
            7103000000: "Inventory Gain/Loss",
        },
    },
    "DEPRECIATION & MAINTENANCE": {
        "Depr - Buildings": {6202002102: "Warehouse", 6202002103: "Office"},
        "Depr Exp - Vehicle": {6202002201: "Vehicles I", 6202002202: "Vehicles II"},
        "Depr Exp - Furniture & Fixture": {
            6202002300: "Deprec Exp - Furniture & Fixture",
        },
        "Depr - Equipment*": {
            6202002401: "Equipment - Office",
            6202002402: "Equipment - Computer",
            6202002403: "Equipment - Building",
            6202002404: "Equipment - Kitchen",
            6202002405: "Equipment - Sound System",
            6202002406: "Equipment - Communication Equipment",
            6202002407: "Equipment - MultiMedia",
            6202002408: "Equipment - Production",
            6202002410: "Equipment - Banquet",
            6202002411: "Equipment - Engineering",
            6202002412: "Equipment - Lighting",
            6202002413: "Equipment - Store",
        },
        "Depreciation - Intangible Assets*": {6202002512: "Software"},
        "Deprec - Leasehold Improvement": {
            6202002700: "Deprec - Leasehold Improvement"
        },
        "Repair Maintenance": {
            6202001010: "Building",
            6202001020: "Vehicles",
            6202001030: "Equipment",
            6202001040: "Computer",
            6202001050: "Software",
        },
    },
    "OTHER INCOME / EXPENSES": {
        "Other Income": {
            7101000000: "Interest Income",
            7102000000: "Foreign Exchange Gain/Loss",
            7104000000: "Gain/Loss on Disposal of Fixed Assets",
            7105000000: "Miscellaneous Income",
            7105000001: "Miscellaneous Income - ROI",
            7106000000: "Gain/Loss on Investasi",
            7107000000: "Other Income - Rounding",
        },
        "Other Expenses": {
            7201000000: "Interest Expense",
            7202000000: "Bank Administration & Wire Expense",
            7203000000: "Merchant Fees",
            7204000000: "Miscellaneous Expense",
            7205000000: "Company Gatering",
            7206000000: "Other Expense",
            7207000000: "Other Expense - Rounding",
        },
        "Provision For Income Tax": {
            8100000000: "Current Tax",
            8200000000: "Deferred Tax",
            8300000000: "Miscelaneous Tax",
        },
    },
}


colors = ["#7776a6", "#d9224c", "#6094cc", "#36416d", "#a55073", "#75aadb", "#733c96"]
