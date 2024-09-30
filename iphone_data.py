iPhones = {
    'iPhone15': [
        {
            'productId': ['B0CHXB1PT6'],
            'model': "iPhone 15 Pro Max",
            'color': "Natural Titanium",
            'storage': "512GB",
            'fullName': "iPhone 15 Pro Max Natural Titanium 512GB"
        },
        {
            'productId': ['B0CHX6N27Y', 'B0CHX2WQLX', 'B0CHX8JCXN', 'B0CHX41VNZ', 'B0CHX2WQLX', 'B0CHX4CRND'],
            'model': "iPhone 15 Pro",
            'color': "Black Titanium",
            'storage': "256GB",
            'fullName': "iPhone 15 Pro Black Titanium 256GB"
        },
        {
            'productId': ['B0CHX1W1XY', 'B0CHX2F5QT', 'B0CHX1W1XY', 'B0CHX2F5QT', 'B0CHX6NQMD'],
            'model': "iPhone 15 Plus",
            'color': "Blue",
            'storage': "128GB",
            'fullName': "iPhone 15 Plus Blue 128GB"
        }
    ],
    'iPhone14': [
        {
            'productId': ['B0BN7CXGWG', 'B0BN72J9M5', 'B0BN71NXTX', 'B0BDJYHP2H', 'B0BDJGX2XZ', 'B0BDJH3V3Q'],
            'model': "iPhone 14 Pro Max",
            'color': "Space Black",
            'storage': "512GB",
            'fullName': "iPhone 14 Pro Max Space Black 512GB"
        },
        {
            'productId': ['B0BN72MLT2', 'B0BN71MQYZ', 'B0BN6YVG4Y', 'B0BN7D8XBT', 'B0BDJB5KHG', 'B0BN752KC4', 'B0BN71LR2M', 'B0BN7F2TY5'],
            'model': "iPhone 14 Pro",
            'color': "Deep Purple",
            'storage': "256GB",
            'fullName': "iPhone 14 Pro Deep Purple 256GB"
        },
        {
            'productId': ['B0BN721X22', 'B0BN6Z5GN5', 'B0CG7VTBXK', 'B0BN6ZKZY5', 'B0BN71LWF2', 'B0BN733951', 'B0BN72FYFG', 'B0BXQ2V3NJ', 'B0BDK8LKPJ', 'B0BDJ1B1CS', 'B0BDK62PDX'],
            'model': "iPhone 14",
            'color': "Starlight",
            'storage': "128GB",
            'fullName': "iPhone 14 Starlight 128GB"
        }
    ],
    'iPhone13': [
        {
            'productId': ['B09G94PDVL', 'B09G98MBX1', 'B09G937QLL', 'B09G91L347', 'B09P82MT2B', 'B09P81SW94'],
            'model': "iPhone 13 Pro Max",
            'color': "Graphite",
            'storage': "512GB",
            'fullName': "iPhone 13 Pro Max Graphite 512GB"
        },
        {
            'productId': ['B09G9J5JZX', 'B09P81ZFKS', 'B09P83DFT5', 'B09G9HDN4Q', 'B09G9BFKZN', "B09G9BQS98", 'B09G9HRYFZ', 'B09G93H3BR', 'B09V4MXBSN'],
            'model': "iPhone 13 Pro",
            'color': "Sierra Blue",
            'storage': "256GB",
            'fullName': "iPhone 13 Pro Sierra Blue 256GB"
        },
        {
            'productId': ['B0CHX7NG26', 'B09P82T3PZ', 'B09P81ZM5X', 'B09G9BL5CP', 'B09G99CW2N', 'B09G9HD6PD', 'B09G9D8KRQ', 'B09V4B6K53', 'B09G9FPGTN'],
            'model': "iPhone 13 Mini",
            'color': "Pink",
            'storage': "128GB",
            'fullName': "iPhone 13 Mini Pink 128GB"
        }
    ]
}

def find_product_id(series, model_name):
    # Loop through the list of models for the specified series (e.g., 'iPhone15')
    if series in iPhones:
        for iphone in iPhones[series]:
            if iphone['model'] == model_name:
                return iphone['productId']
    return []

def find_iphone_details(series, model_name):
    # Loop through the list of models for the specified series (e.g., 'iPhone15')
    if series in iPhones:
        for iphone in iPhones[series]:
            if iphone['model'] == model_name:
                return iphone  # Return the entire dictionary with all details
    return None  # Return None if the model is not found