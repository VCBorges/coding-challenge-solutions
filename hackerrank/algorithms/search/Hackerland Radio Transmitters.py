def hackerlandRadioTransmitters(
    houses: list[int],
    transmitter_range: int,
) -> int:
    num_transmitters = 0
    houses = sorted(set(houses))
    num_houses = len(houses)
    i = 0

    while i < num_houses:
        num_transmitters += 1
        transmitter_loc = houses[i] + transmitter_range
        while i < num_houses and houses[i] <= transmitter_loc:
            i += 1

        transmitter_max_range = houses[i - 1] + transmitter_range
        while i < num_houses and houses[i] <= transmitter_max_range:
            i += 1

    return num_transmitters


first_multiple_input = input().rstrip().split()

total_houses = int(first_multiple_input[0])

transmitter_range = int(first_multiple_input[1])

houses = list(map(int, input.rstrip().split()))

result = hackerlandRadioTransmitters(houses, transmitter_range)
