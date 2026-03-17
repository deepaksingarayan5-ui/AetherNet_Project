import numpy as np

def simulate_photon_stream(distance_au, laser_power_mw, weather="Clear"):
    """
    Refined physics for demonstration.
    Lowers base power so distance impact is visible on the 0.0-1.0 scale.
    """
    # Lowered constant (from 250 to 5.0) so 1.0 AU isn't 'over-saturated'
    base_signal = 5.0 / (distance_au ** 2) 
    
    # Increased noise range to make channels look distinct
    turbulence_map = {"Clear": 0.05, "Cloudy": 0.2, "Stormy": 0.5}
    noise_level = turbulence_map.get(weather, 0.05)
    
    channels = {}
    for i in range(1, 65):
        # Adding unique noise per channel
        scintillation = np.random.normal(0, noise_level)
        # Cap signal between 0 and 1 for the bar chart
        val = max(0.05, min(0.95, base_signal + scintillation))
        channels[f"CH{i}"] = val
        
    return channels

def get_system_health(channels):
    """Adjusted thresholds for the new power scale."""
    avg_signal = sum(channels.values()) / 64
    
    if avg_signal > 0.5: 
        return "OPTIMAL"
    elif avg_signal > 0.2: 
        return "STABLE"
    else: 
        return "CRITICAL"
