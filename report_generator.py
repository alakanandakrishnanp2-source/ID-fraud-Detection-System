def generate_report(analysis):

    risk_score = 0

    if analysis["blur_detected"]:
        risk_score += 30

    if analysis["edge_score"] < 0.01:
        risk_score += 30

    if analysis["ela_score"] > 20:
        risk_score += 40


    if risk_score > 50:
        status = "Suspicious Document"
    else:
        status = "Likely Genuine"


    report = {

        "risk_score": risk_score,
        "status": status,
        "analysis": analysis

    }

    return report