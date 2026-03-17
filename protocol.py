def encode_packet(channel_data):
    """Packages data using the Aether-Net protocol rules."""
    best_channel = max(channel_data, key=channel_data.get)
    peak_value = channel_data[best_channel]
    
    return {
        "header": "ARISE_V2_PRO",
        "primary_ch": best_channel,
        "throughput_mhz": round(peak_value * 125, 2),
        "status": "ACTIVE" if peak_value > 0.15 else "DROPPED"
    }
