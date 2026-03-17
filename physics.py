import numpy as np

def simulate_photon_stream(distance_au, laser_power_mw, weather="Clear"):
    """Simulates signal reception with atmospheric turbulence."""
    # Base signal calculation
    base_signal = laser_power_mw / (distance_au ** 2)
    
    # Turbulence Mapping
    turbulence_map = {"Clear": 0.05, "Cloudy": 0.25, "Stormy": 0.60}
    noise_level = turbulence_map.get(weather, 0.05)
    
    channels = {}
    for i in range(1, 65):
        # Scintillation: Random fluctuations caused by air density changes
        scintillation = np.random.normal(0, noise_level)
        channels[f"CH{i}"] = max(0.01, base_signal + scintillation)
        
    return channels

def get_system_health(channels):
    avg_signal = sum(channels.values()) / 64
    if avg_signal > 0.6: return "OPTIMAL"
    if avg_signal > 0.25: return "STABLE"
    return "CRITICAL"
