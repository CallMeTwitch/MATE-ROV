# Conversion Rate
VAR = 100 / 3

# Define Motor Power Function
def motor_values(x, y, r, dead_zone = 0.1):
    # Set Numbers Below Dead Zone to Zero
    x, y, r = map(lambda x:x * (abs(x) > dead_zone), (x, y, r))

    # Return Power Needed
    return (y + x + r) * VAR, (y - x - r) * VAR, (y + x - r) * VAR, (y - x + r) * VAR