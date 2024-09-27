def find_busiest_intersections(vehicle_data):
    """
    This function takes a dictionary where keys are intersection names and values are vehicle counts.
    It returns a list of intersections that have the highest vehicle count.
    
    Parameters:
    vehicle_data (dict): A dictionary of intersections and their respective vehicle counts.
    
    Returns:
    list: A list of intersections with the highest vehicle count.
    """
    if not vehicle_data:
        return []

    # Find the maximum vehicle count
    max_vehicles = max(vehicle_data.values())
    
    # Collect all intersections with the maximum vehicle count
    busiest_intersections = [intersection for intersection, count in vehicle_data.items() if count == max_vehicles]
    
    return busiest_intersections


