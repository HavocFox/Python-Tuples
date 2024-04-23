total = 0

itineraries = {}

def tuple_taker(tuple_list):
    print("\nHere are the itineraries in the list: ")
    for item in range(1, len(tuple_list) + 1):
        itinerary = tuple_list['Itinerary', item]
        print(f"Itinerary {item}: {itinerary[0]} - From {itinerary[1]} to {itinerary[2]}")


while True:

    name_entry = input("Please enter the traveler's name. ")
    begin_entry = input("Please enter the traveler's starting location. ")
    end_entry = input("Please enter the traveler's destination. ")
    new_traveler_tuple = (name_entry, begin_entry, end_entry)
    itineraries['Itinerary', total+1] = new_traveler_tuple
    total = total + 1

    choice = input("Would you like to enter another itinerary? Y or N. ").upper()
    if choice == 'Y':
        pass
    else:
        tuple_taker(itineraries)
        print("\n")
        break