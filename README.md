# PRODIGY_DS_05
# Traffic Accident Data Visualization

This project visualizes key aspects of a traffic accident dataset, including road surface type, weather conditions, light conditions, and causes of accidents. The data is analyzed and displayed using bar plots to highlight distributions of various accident-related variables.

## Project Overview

This project includes:
1. **Data Cleaning**: Handling missing values in the dataset.
2. **Data Visualization**: Generating bar plots to visualize the distribution of:
   - Road surface types
   - Weather conditions
   - Light conditions during the accidents
   - Causes of accidents

## Dataset

The dataset used in this project (`Traffic_Accident.csv`) includes information on various traffic accidents, such as the type of road surface, weather conditions, light conditions, and the causes of accidents.

### Example Columns:

- `Road_surface_type`: Type of road surface where the accident occurred (e.g., Dry, Wet, Icy).
- `Weather_conditions`: Weather conditions during the accident (e.g., Clear, Rainy, Foggy).
- `Light_conditions`: Lighting conditions at the time of the accident (e.g., Daylight, Night with streetlights).
- `Cause_of_accident`: Primary cause of the accident (e.g., Speeding, Distracted Driving).

### Example Rows:

| Road_surface_type | Weather_conditions | Light_conditions | Cause_of_accident |
| ----------------- | ------------------ | ---------------- | ----------------- |
| Dry               | Clear               | Daylight         | Speeding          |
| Wet               | Rainy               | Night            | Distracted Driving|

## Requirements

Ensure you have the following Python libraries installed:

- `pandas`
- `matplotlib`

You can install them using:

```bash
pip install pandas matplotlib
