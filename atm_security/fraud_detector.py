"""
ATM Security - Fraud Detection Module
Demonstrates behavioral anomaly detection for ATM transaction security
"""

import json
from datetime import datetime
from typing import Dict, List

class ATMFraudDetector:
    def __init__(self):
        self.alert_threshold = 0.75
        self.suspicious_patterns = []

    def analyze_transaction(self, transaction: Dict) -> Dict:
        """Analyze a transaction for fraud indicators"""
        risk_score = 0.0
        flags = []

        if transaction.get("amount", 0) > 1000:
            risk_score += 0.3
            flags.append("HIGH_AMOUNT")

        if transaction.get("velocity_count", 0) > 3:
            risk_score += 0.4
            flags.append("HIGH_VELOCITY")

        if transaction.get("off_hours", False):
            risk_score += 0.2
            flags.append("OFF_HOURS")

        if transaction.get("new_location", False):
            risk_score += 0.15
            flags.append("NEW_LOCATION")

        return {
            "transaction_id": transaction.get("id"),
            "risk_score": min(risk_score, 1.0),
            "flags": flags,
            "action": "BLOCK" if risk_score >= self.alert_threshold else "ALLOW",
            "timestamp": datetime.now().isoformat()
        }

if __name__ == "__main__":
    detector = ATMFraudDetector()
    test_txn = {"id": "TXN001", "amount": 1500, "velocity_count": 4, "off_hours": True, "new_location": False}
    result = detector.analyze_transaction(test_txn)
    print(json.dumps(result, indent=2))
