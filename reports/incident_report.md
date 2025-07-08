# 🛡️ Incident Report – Unauthorized Access Attempt

**Date of Report:** 2025-07-07  
**Reported by:** Carlos Joseph Guagnelli  
**Environment:** Simulated logs (CyberRisk-Lab project)  
**Incident Type:** Multiple failed login attempts followed by suspicious login success  
**Severity:** Medium–High  
**Status:** Closed – Investigated and mitigated

---

## 🧠 Summary

During simulated log monitoring, several IP addresses from external ranges (e.g., `45.67.89.103`) showed repeated failed login attempts targeting multiple internal user accounts. One IP (`45.67.89.104`) eventually achieved a successful login using the `operator` account.

The simulated incident mimics a brute-force or credential-stuffing scenario and was used to test detection and response capabilities.

---

## 🧪 Indicators of Compromise (IoCs)

| Indicator        | Description                         |
|------------------|-------------------------------------|
| IP Address       | `45.67.89.103`, `45.67.89.104`      |
| Events Detected  | `multiple_failed_logins`, `login_success` |
| Target Accounts  | `admin`, `operator`, `j.guagnelli`  |
| Timestamps       | July 6–7, 2025                      |

---

## 🕵️ Timeline of Events

| Time               | Event                        | User          | IP             |
|--------------------|------------------------------|---------------|----------------|
| 2025-07-06 14:36   | multiple_failed_logins       | admin         | 192.168.1.18   |
| 2025-07-07 01:44   | login_failed                 | j.guagnelli   | 45.67.89.103   |
| 2025-07-07 00:19   | login_success                | operator      | 45.67.89.104   |

---

## 🛠️ Actions Taken

- 🚨 Alert triggered on multiple failed login attempts
- 🔎 Analyzed event patterns and confirmed anomaly
- 🧼 Simulated containment: account lockout & IP ban
- 📚 Documented incident for training purposes

---

## 🛡️ Recommendations

- Enforce **multi-factor authentication (MFA)** on all privileged accounts  
- Monitor repeated login failures and create **SIEM rules**  
- Limit remote login from external IPs  
- Rotate credentials regularly and audit logs proactively

---

## 📎 Related Files

- [`datasets/simulated_logs.csv`](../datasets/simulated_logs.csv)  
- [`scripts/log_simulator.py`](../scripts/log_simulator.py)  
- [`visualizations/ip_event_summary.png`](../visualizations/ip_event_summary.png)

---

> _This simulated incident was generated as part of a cybersecurity lab to demonstrate risk detection, logging analysis, and incident response capabilities._  
