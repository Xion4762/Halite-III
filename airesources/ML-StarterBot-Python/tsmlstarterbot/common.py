import math

# Max number of planets.
PLANET_MAX_NUM = 28

# Number of initial features per planet we compute for each planet.
PER_PLANET_FEATURES = 11

FEATURE_NAMES = [
    "health",
    "available_docking_spots",
    "remaining_production",
    "signed_current_production",
    "gravity",
    "closest_friendly_ship_distance",
    "closest_enemy_ship_distance",
    "ownership",
    "distance_from_center",
    "weighted_average_distance_from_friendly_ships",
    "is_active"]


def distance2(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def distance(x1, y1, x2, y2):
    return math.sqrt(distance2(x1, y1, x2, y2))