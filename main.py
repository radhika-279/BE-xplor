from fastapi import FastAPI,Response
from fastapi.responses import JSONResponse

app = FastAPI()

terms_and_conditions = {
    "title": "Xplor Ticketing Machine - Terms and Conditions",
    "license": "Non-exclusive, non-transferable license granted for ticket sales and validation only.",
    "user_responsibilities": "Users are responsible for maintaining machine security, compliance with laws, and intended use.",
    "intellectual_property": "All intellectual property rights belong to Xplor.",
    "limitation_of_liability": "Xplor is not liable for damages or losses from machine use.",
    "indemnification": "Users agree to indemnify Xplor from any claims, damages, or losses.",
    "modification": "Terms may be modified by Xplor at any time.",
    "termination": "Xplor reserves the right to terminate access for violations.",
    "governing_law": "Terms governed by Indian law."
}
privacy_policy = {
    "title": "Xplor Ticketing Machine - Privacy Policy",
    "information_collection": "We collect ticket sales data and device usage stats.",
    "use_of_information": "Information is used to improve service and comply with legal obligations.",
    "data_sharing": "Information may be shared with trusted third parties for processing and analytics.",
    "security": "Security measures are implemented to protect user information.",
    "cookies": "Cookies are used for enhancing user experience and gathering usage statistics.",
    "third_party_links": "We are not responsible for the privacy practices of third-party websites.",
    "children_privacy": "Service not intended for children under 13.",
    "changes": "We reserve the right to update or modify the privacy policy."
}
cancellation_and_refund_policy = {
    "title": "Xplor Ticketing Machine - Cancellation and Refund Policy",
    "cancellation": "Subscriptions can be canceled anytime by contacting customer support.",
    "refunds": "Refunds for canceled subscriptions follow terms in the subscription agreement.",
    "no_refunds": "No refunds for partial months of service.",
    "cancellation_fees": "Cancellation fees may apply as specified in the subscription agreement.",
    "processing_time": "Refunds will be processed within a reasonable timeframe.",
    "refund_method": "Refunds issued using the original payment method whenever possible.",
    "exceptions": "Exceptions to policy may be considered under certain circumstances at our discretion."
}

@app.get('/terms_and_conditions')
async def get_terms_and_conditions():
    return JSONResponse(content=terms_and_conditions)

@app.get('/privacy_policy')
async def get_privacy_policy():
    return JSONResponse(content=privacy_policy)

@app.get('/cancellation_and_refund_policy')
async def get_cancellation_and_refund_policy():
    return JSONResponse(content=cancellation_and_refund_policy)

@app.get('/help')
async def get_help_section():
    return {"message": "For any assistance, contact: 8590293890"}

