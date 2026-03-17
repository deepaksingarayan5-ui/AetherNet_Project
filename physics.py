import numpy as np

def simulate_photon_stream(distance_au, laser_power_mw, weather="Clear"):
    """Simulates signal reception with a more realistic Inverse Square Law."""
    # We increased the power of the distance impact (Distance cubed)
    # to show a sharper drop-off for the demo.
    base_signal = laser_power_mw / (distance_au ** 3) 
    
    turbulence_map = {"Clear": 0.02, "Cloudy": 0.15, "Stormy": 0.45}
    noise_level = turbulence_map.get(weather, 0.05)
    
    channels = {}
    for i in range(1, 65):
        scintillation = np.random.normal(0, noise_level)
        # Signal is capped at 0 to 1.0 for the chart display
        channels[f"CH{i}"] = max(0.001, min(1.0, base_signal + scintillation))
        
    return channels

def get_system_health(channels):
    """Stricter health thresholds for a better project demo."""
    avg_signal = sum(channels.values()) / 64
    
    if avg_signal > 0.7: 
        return "OPTIMAL"
    elif avg_signal > 0.3: 
        return "STABLE"
    else: 
        return "CRITICAL"
