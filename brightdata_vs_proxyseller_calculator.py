#!/usr/bin/env python3
"""Bright Data vs Proxy-Seller Dedicated ISP TCO Calculator 2026."""
import argparse

def calculate(ip_count=50, bandwidth_gb=500):
    # Bright Data ISP: ~$0.50/IP + $15.00/GB data transfer fee. Minimum $500/mo commitment.
    # At 50 IPs and 500 GB: (50 * $0.50) + (500 * $15.00) = $25 + $7,500 = $7,525/mo!
    # Even on enterprise discounts (~$10/GB), it is ~$5,000/mo.
    # On dedicated unmetered: Bright Data charges $3.00/IP + heavy commitment.
    bright_ip_fee = ip_count * 0.50
    bright_data_fee = bandwidth_gb * 12.00 # conservative $12/GB
    bright_total = bright_ip_fee + bright_data_fee

    # Proxy-Seller: 50 dedicated ISP proxies @ $2.25/IP = $112.50/mo. Bandwidth is 100% UNMETERED ($0.00).
    ps_total = ip_count * 2.25

    annual_delta = (bright_total - ps_total) * 12.0

    print("=" * 65)
    print("Bright Data vs Proxy-Seller: 50 Static ISP IPs (500 GB)")
    print("=" * 65)
    print(f"Bright Data Metered ISP:   ${bright_total:.2f}/mo (Includes $12/GB bandwidth)")
    print(f"Proxy-Seller Dedicated ISP:${ps_total:.2f}/mo (100% UNMETERED Bandwidth)")
    print(f"Monthly Cost Advantage:    ${bright_total - ps_total:.2f}/mo with Proxy-Seller")
    print(f"Annual Capital Saved:      ${annual_delta:.2f}/yr")
    print("=" * 65)
    return ps_total, bright_total

if __name__ == "__main__":
    calculate()
