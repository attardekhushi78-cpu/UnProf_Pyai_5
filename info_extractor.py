import re


# ==========================================
# ⚙️ REGEX PATTERN MATCHING ENGINE (UPDATED)
# ==========================================

# 1. Email Address Pattern
EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# 2. Optimized Phone Number Pattern 
# Easily captures +91, spaces, dots, dashes, and parentheses extensions
PHONE_PATTERN = r"\+?\d{1,4}[-.\s]?\(?\d{2,4}\)?[-.\s]?\d{3,5}[-.\s]?\d{3,5}"

# 3. Date Pattern
DATE_PATTERN = r"\b\d{2}[-/.]\d{2}[-/.]\d{4}\b|\b\d{4}[-/.]\d{2}[-/.]\d{2}\b"


def extract_information(raw_text):
    """
    Applies the re module methods to sweep the text and isolate patterns.
    """
    # Using re.findall() to extract all occurrences matching our patterns
    emails = re.findall(EMAIL_PATTERN, raw_text)
    dates = re.findall(DATE_PATTERN, raw_text)
    
    # Extract phone numbers
    raw_phones = re.findall(PHONE_PATTERN, raw_text)
    
    # Clean up and format phone numbers using re.sub()
    # This standardizes different symbols into a uniform "XXX-XXX-XXXX" format
   # Extract phone numbers
    raw_phones = re.findall(PHONE_PATTERN, raw_text)
    
    cleaned_phones = []
    for phone in raw_phones:
        # Strip trailing punctuation noise from regex capture boundaries
        phone_strip = phone.strip().rstrip('.')
        digits_only = re.sub(r"[\(\)\s\.\-]", "", phone_strip)
        
        # Format if it's a standard national 10-digit string
        if len(digits_only) == 10:
            formatted = f"{digits_only[:3]}-{digits_only[3:6]}-{digits_only[6:]}"
            cleaned_phones.append(formatted)
        elif len(digits_only) > 5: # Keep international/landlines as they were
            cleaned_phones.append(phone_strip)

            
    # Pack results neatly into a dictionary structure
    return {
        "emails": list(set(emails)),          # set() removes accidental duplicate matches
        "phones": list(set(cleaned_phones)),
        "dates": list(set(dates))
    }



#  INTERFACE RUNNER LOOP


def main():
    print("⚡ Welcome to the ScholarOps Text Information Extractor")
    print("🔍 Powered by Python's Native 're' Pattern Matching Module\n")
    
    print("--- Copy & Paste Your Raw Text Below ---")
    print("(Press Enter, then Ctrl+D or Ctrl+Z followed by Enter to process the text)\n")
    
    # Read multi-line input from the terminal safely
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
            
    raw_text = "\n".join(lines)
    
    if not raw_text.strip():
        print("❌ Error: No text was provided for extraction.")
        return

    print("\n" + "="*50)
    print("📊 EXTRACTION ANALYSIS MATRIX RESULTS")
    print("="*50)
    
    results = extract_information(raw_text)
    
    # Display Emails
    print(f"\n📬 Extracted Emails ({len(results['emails'])} unique):")
    if results["emails"]:
        for email in results["emails"]:
            print(f"  ➜ {email}")
    else:
        print("  (No emails found)")
        
    # Display Phones
    print(f"\n📱 Extracted Phone Numbers ({len(results['phones'])} unique/formatted):")
    if results["phones"]:
        for phone in results["phones"]:
            print(f"  ➜ {phone}")
    else:
        print("  (No phone numbers found)")
        
    #  Display Dates
    print(f"\n📅 Extracted Calendar Dates ({len(results['dates'])} unique):")
    if results["dates"]:
        for date in results["dates"]:
            print(f"  ➜ {date}")
    else:
        print("  (No dates found)")
        
    print("\n" + "="*50)

if __name__ == "__main__":
    main()