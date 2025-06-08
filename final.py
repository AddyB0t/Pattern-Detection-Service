from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import uvicorn
import re

app1 = FastAPI()

STATE_CODES = [
    'AN', 'AP', 'AR', 'AS', 'BR', 'CH', 'CT', 'DL', 'GA', 'GJ', 'HR', 'HP', 'JK', 'JH', 
    'KA', 'KL', 'MP', 'MH', 'MN', 'ML', 'MZ', 'NL', 'OR', 'PB', 'RJ', 'SK', 'TN', 'TS', 
    'TR', 'UP', 'UT', 'WB'
]

def remove_overlapping_matches(matches):
    if not matches:
        return []
    
    # Sort matches by start position
    sorted_matches = sorted(matches, key=lambda x: x.start())
    result = [sorted_matches[0]]
    
    for current in sorted_matches[1:]:
        previous = result[-1]
        # If current match overlaps with previous, keep the longer one
        if current.start() <= previous.end():
            if len(current.group()) > len(previous.group()):
                result[-1] = current
        else:
            result.append(current)
    
    return [match.group() for match in result]

def find_patterns(text):
    # Define patterns
    patterns = {
        'PAN Number': r"[A-Z]{3}[PFCHAT][A-Z]\d{4}[A-Za-z]",
        'Contact Number': r'(\+?91)?( |-)?([6-9])\d{4}( |-)?\d{5}',
        'Driving License Number': r"[A-Z]{2}( |-)?\d{1,2}( |-)?[A-Z]{1,2}( |-)?\d{4}( |-)?\d{7}",
        'Registration Number': r"[A-Z]{2}( |-)?[0-9]{2}( |-)?[A-Z]{2,3}( |-)?[0-9]{4}"
    }
    
    # Find matches for each pattern
    results = {}
    for name, pattern in patterns.items():
        matches = remove_overlapping_matches(list(re.finditer(pattern, text)))
        results[name] = matches
    
    return results

# def find_registration_number(text):
#     # Define patterns
#     patterns = {
#         'Registration Number': r"[A-Z]{2}( |-)?[0-9]{2}( |-)?[A-Z]{2,3}( |-)?[0-9]{4}"
#     }
    
#     results = {}
#     # Initialize a list to store valid registration numbers with state codes
#     valid_registrations = []
    
#     # Find all registration numbers first
#     for name, pattern in patterns.items():
#         matches = remove_overlapping_matches(list(re.finditer(pattern, text)))
        
#         # For each match, check if the state code is valid
#         for match in matches:
#             reg_num = match.group()
#             # Extract the state code (first two characters)
#             state_code = reg_num[:2]
            
#             # Check if the state code is in our list of valid state codes
#             if state_code in STATE_CODES:
#                 valid_registrations.append({
#                     "registration_number": reg_num,
#                     "state_code": state_code
#                 })
        
#         results["Valid Registrations"] = valid_registrations

#     return results["Valid Registrations"]
    



@app1.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Read the uploaded file content
        content = await file.read()
        text = content.decode("utf-8")
        
        # Process the text and find patterns
        results = find_patterns(text)
        
        # Convert results to a list format
        formatted_results = []
        for pattern_name, matches in results.items():
            if matches:  # Only add patterns that have matches
                formatted_results.append({
                    "pattern": pattern_name,
                    "matches": matches
                })
        
        return JSONResponse(content=formatted_results)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

if __name__ == "__main__":
    uvicorn.run("final:app1", host="127.0.0.1", port=8000, reload=True)

















