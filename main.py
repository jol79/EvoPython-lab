
def direction(facing, turn):
    """Returns the direction based on the given facing
    and turn in degrees
    
    Notes:
        1. turn must be a multiple of 45 between -1080
            and 1080.
    """
    
    if not isinstance(turn, int) or turn % 45 != 0 or turn < -1080 or turn > 1080: return False
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    if facing not in directions: return False

    positionFacing = directions.index(facing) + 1 if turn > 0 else directions.index(facing) - 1
    steps = turn // 45 if turn > 0 else -turn // 45
    resultElement = None
    
    for step in range(steps):
        if turn < 0:
            if positionFacing < 0:
                positionFacing = len(directions) -1
            resultElement = directions[positionFacing]
            positionFacing -= 1
        if turn > 0:
            if positionFacing >= len(directions):
                positionFacing = 0
            resultElement = directions[positionFacing]
            positionFacing += 1
            
    return resultElement


if __name__ == '__main__':
    print(direction(facing='E', turn=-675))
